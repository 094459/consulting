+++
title = "Building a digital badge system with the help of Kiro (and Amazon ECS Express Mode)"
date = 2026-01-15
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/building-a-digital-badge-system-with-the-help-of-kiro-and-amazon-ecs-express-mode-2i0o"
+++

I have been working on a new digital badge demo application that you can use to generate and then issue digital certificates. You have probably seen these in your LinkedIn newsfeed - those digital badges saying that you have completed this or that activity or training course. I have been using Kiro to create this demo application, leveraging the [Strands Agent](https://strandsagents.com/latest/) framework to make adding generative AI a trivial exercise (seriously, if you have not tried it yet do yourself a favour and check it out).

I needed to deploy this application to AWS, and my preference has been for many years now, to deploy via containers.  The week before re:Invent, AWS launched [Amazon ECS Express Mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-overview.html?trk=fd6bb27a-13b0-4286-8269-c7b1cfaa29f0&sc_channel=el), the latest way to deploy your container applications on AWS. Amazon ECS has been my favourite container way to run container application since forever, and so I wanted to check this out. 

This blog post is my "unboxing" post, where I share my first experiences using this new feature to deploy this application.

## Getting Started

I have been developing this application using [Kiro](https://kiro.dev?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el) and so the first step I took was to think about how to prepare the application for deployment to Amazon ECS Express Mode.

I would typically know what to look out for and how to do this. If my memory was feeling a little hazy, I would take a look at the docs for a refresher. These days, it is all about having that knowledge integrated with your AI coding tools via MCP tools, so I added the [Amazon ECS MCP Server](https://awslabs.github.io/mcp/servers/ecs-mcp-server#configuration) to my Kiro session. 

This is what my project mcp.json looked like:

```
{
  "mcpServers": {
    "awslabs.ecs-mcp-server": {
      "command": "uvx",
      "args": ["--from", "awslabs-ecs-mcp-server", "ecs-mcp-server"]
    }
  }
}
```

## Application readiness evaluation

My next step is to ask Kiro for an assessment of what deploying to Amazon ECS Express would look like for this project. From a new Vibe coding session in Kiro, I ask the following in the chat interface:

> Using the Amazon ECS MCP Server - provide me with a readiness check for deploying this application to Amazon ECS Express Mode

I explicitly mention the MCP Server - this is something that I have just started to get into the habit of doing as I have found that omitting it can sometimes lead to the MCP tools not being invoked. After being prompted to trust the MCP Server tools (search_documentation), Kiro swiftly produces a nice report for me to review. 

Reviewing the report I see there are three findings that need me to make updates.

![Report of findings](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Flpgaelzpn37pmt5s452s.png)

After asking Kiro to make the changes needed, the next part of the report provides me with a contextually specific checklist for how to get this code deployed to Amazon ECS Express Mode. It includes details about what IAM policies need to be created, reviewing what services that my application is using and adding those permissions (scoped down to follow least privilege best practice). Kiro also generates a deployment script that looks very comprehensive to me.

Reviewing the script though I notice a potential issue. The application requires a BASE_URL that is used throughout the application, and during local development this has been pretty straightforward - 127.0.0.1:5001! As I will not know what the DNS will be once this is deployed on Amazon ECS Express Mode, I have a chicken and egg situation. 

As I am not sure how to proceed, I ask Kiro.

> I don't know what to configure for BASE_URL as I don't have a DNS registered and I don't know what the DNS of this application will be when it is deployed on Amazon ECS Express. Can you help me.

Kiro makes changes to the application code and deployment script to handle this.

![Fixing issues](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fcjp843husowmn6qc7n9s.png)

## Deploying to Amazon ECS Express

I ran the script, and it just ran. It deployed. Things were provisioned. Services started. But...it was taking a little too long, and so I decided to go and check the CloudWatch logs to see what was happening. And there it was:

```
exec /bin/sh: exec format error
```

I had forgotten that my mac produces arm based images. I have been in this situation before, and it is typically a quick update to change the architecture type from amd64 to aarch64. However, I am in for a surprise.

![To Arm or just Armless?](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fiygpvoog5p0h0k3rgdfz.png)

I do double check the api docs and the official documentation to confirm this, but I thought it was kind of cool that the MCP server was able to catch this. (For now) Amazon ECS Express Mode uses amd64 instance types for the initial deployment. Kiro has already taken care of business for me, updating my build script to create amd64 images.

> **Note!** After speaking with folk who know more, you **CAN** use aarch64 instances with Amazon ECS Express mode. After you have created your service, you can modify the task definition file (yup, those of you familiar with Amazon ECS will know that this is the key configuration file - task.json - where you define what you need to deploy your container) and change to support AWS Graviton instance types. Behind of scenes its AWS Fargate that is running the show.

The script was not perfect. For example, after the initial successful deployment, the first time I used the script to update the application, it generated this error

```
An error occurred (InvalidParameterException) when calling the CreateExpressGatewayService operation: Unable to Start a service that is still Draining.
```

Kiro was able to quickly adjust the deployment script (it was trying to create the same service every time rather than use the update service method). You can check all the code, I share the repo at the end of this post.

## What did I learn?

The first thing I learned was that Amazon ECS Express Mode provides an opinionated set of defaults to make it quick to deploy a container workload. However, it is still Amazon ECS, so you still get access to everything as if it were a traditional set of Amazon ECS resources. This means that post deployment, [configuring things like custom domains and certs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-advanced-customization.html?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el) are no problem, and in fact are made easier because the timeline deployment view kind of guides you to the things you care about. You still get access to task definition json file if you need or want to make changes.

The second thing that surprised me was that by default Amazon ECS Express Mode went with amd64 instance types rather than arch64. Given that more and more workloads are being deployed on AWS Graviton instance types, it would be nice to see if this is an option that can be set in the service creation API. As it stands, given the first learning, it was pretty straightforward to update the cluster to switch to AWS Graviton instances.

The final thing I learned was that the Amazon ECS MCP Server is pretty awesome. It provided me with everything I needed and understood working with Amazon ECS Express Mode - given how new this was, I was not sure how Kiro was going to handle it. 


## Conclusion

Whilst Kiro did most of the hard work in generating the code, as a developer you should need to make sure that you are orchestrating things. Whether this is reviewing the output and spotting gaps, asking (via prompts) the right questions to get clarity, your role is still critical in getting that working code. 

My experience using Amazon ECS Express Mode was great, and I really like how easy and simple it makes it to deploy your applications to AWS. Combined with Kiro and the Amazon ECS MCP Server, I now have a new default approach for building and deploying applications.

I have shared the **code in [this GitHub repo](https://github.com/094459/digital-badge-vending-demo)** where you can try this out for yourself. Its a little rough around the edges, but might give folks some ideas of how they might be able to create even better versions of this. 

I have also put together a short video of this in action which you can see here.

{{< youtube W50hGJnOuqo >}}

### Get started today

Check out [Amazon ECS Express Mode documentation pages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-overview.html?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el)

You can get started with Kiro CLI today for free. [Download it from this link](https://kiro.dev/downloads/?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el).  I have created a workshop if you are new to Kiro CLI and the [Kiro CLI workshop](https://github.com/094459/aqd-cli-workshop) will walk you through getting started with the terminal based Kiro CLI tool, and provides a comprehensive overview as well as advanced topics.

Finally, if you did find this post interesting, helpful, or useful, I would love to get your feedback. Please [use this 30 second feedback form](https://pulse.aws/survey/OZ7QIXA7) and I will be forever grateful.

Made with ♥ from DevRel
