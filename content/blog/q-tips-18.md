+++
title = "Amazon Q Developer Tips: No.18 Amazon Q Developer Agents - /dev"
date = 2024-12-18
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no18-amazon-q-developer-agents-dev-1i0"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no17-choose-the-right-tool-7a2).

Ok, time for today's tip....

### Tip 18 - Amazon Q Developer Agents : /dev

Amazon Q Developer provides a number of tools for developers to use. Some of these tools provide code suggestions and then leave it up to the developer to review and implement. Amazon Q Developer Agent for feature development is invoked using /dev and will us the prompt you provide, together with the context of the current project workspace, break that into tasks, and then write code for you.

I have been using this extensively and so I want to share some of the things I have learned and what has worked for me.

**Use cases**

The first and most important thing to think about is what are you trying to do with /dev. In a previous tips I shared that it is important to know the limits of what can be produced, so breaking down larger problems into a road map with simpler tasks should be something you have thought about before using /dev.

**Scaffolding**

In previous tips I shared how you can use scaffolding to influence the output that Amazon Q Developer generates, and this is true when using /dev. When Amazon Q Developer starts working, it review relevant files within the current project workspace. Having a scaffold document that provides details on the expected layout, libraries, or code that needs to be created will influence what is produced.

You can scaffold directly within the prompt however, so you do not need to create the doc. For example, this is a perfectly valid prompt that includes useful scaffolding information that Amazon Q Developer will use.

```
/dev Create a Node.js project for a basic hit counter application with the following structure:

.
├── iac/
│ ├── dynamodb-table.yml
│ └── fargate-service.yml
├── models/
│ └── counter.js
├── routes/
│ ├── healthcheck.js
│ └── increment-counter.js
├── tests/
│ ├── healthcheck.test.js
│ └── increment-counter.test.js
├── Dockerfile
├── build-and-deploy.sh
├── index.js
└── package.json
```

**Data model**

One of the things I have found works well is to build my data model first, and have this as a key project file that /dev will then use when building the rest of the application.

I have found creating the data model in either code or in SQL works equally well, so you should try this for yourself based on your own preferences. I tend to spend some time using some of the other Amazon Q Developer tools first to create the data model (in some situations) but I have spoken to developers who say that the data model is often an artefact that they are provided with by another team - so using this as an input works for these situations.

**Use your follow up questions**

You have a limited number of quota for using /dev, so you should use it wisely. When it has finished, you are provided with two options: 1/Accept Code and 2/Provide feedback and regenerate.

You should always review the output - spend time as this has used up one of your quota, and you want to make sure it is correct. I sometimes find during this review phase that it has not always done what I asked it. When this happens, I typically select the "Provide feedback and regenerate" button, and then add details of what is missing or any course corrections needed.

**Things to know**

Whilst /dev provides a great and powerful capability, there are a few things you should know before using this:

* Amazon Q filters out files or folders defined in a .gitignore file, and only uses supported file types to generate code

* The current "good practices" in the Amazon Q Developer docs [here](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/software-dev.html) state that when using /dev you should look to limit update to around five files at a time. Asking Amazon Q to make larger changes might impact the quality and manageability of the implementation of your feature. I have found that Amazon Q Developer might ignore some files, so you should be specific in your initial prompt

* The use of this feature is subject to some sizing limits, currently 50Mb of compressed source code (200Mb uncompressed) - if you are working with a large code base, you might need to split this out into logical components

**Example prompts**

A resource that I have mentioned in previous tips from AWS Community Builder Christian Bonzelet, is [https://promptz.dev](https://www.promptz.dev/). This tool helps you record and save prompts that you find helpful, but ALSO learn from others who have shared/saved their prompts too.

My colleague Nathan Peck has also put together a really nice set of example prompts that he has used with /dev which I think are worth reviewing to see how to get the best out of this powerful capability of Amazon Q Developer. Check them out [here](https://nathanpeck.github.io/q-developer-tips/).

**Try Amazon Q Developer today, and claim your free Builder ID**

That's it for today's tip. Let me know how you get on with this tip, and if you have your own drop me a message or reply. I would love to feature them here.

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
