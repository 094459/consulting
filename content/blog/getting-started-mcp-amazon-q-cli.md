+++
title = "Configuring Model Context Protocol (MCP) with Amazon Q CLI"
date = 2025-05-01
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/configuring-model-context-protocol-mcp-with-amazon-q-cli-e80"
+++

[Amazon Q CLI](https://dev.to/aws/getting-started-with-amazon-q-developer-cli-4dkd) is a next generation developer tool that brings IDE-style autocomplete and agentic capabilities to your terminal. I have spent a lot of time recently writing about this amazing tool, and so was super excited by the news today that with the [v1.9.x](https://github.com/aws/amazon-q-developer-cli/releases) release, Amazon Q CLI now supports Model Context Protocol (MCP) for tools use. 

> **What is Model Context Protocol (MCP)?** if you have not heard about MCP (where have you been?) then check out my colleague's post on this, [Standardizing AI Tooling with Model Context Protocol (MCP)](https://dev.to/aws/standardizing-ai-tooling-with-model-context-protocol-mcp-nmj)

MCP server directories are beginning to appear, and we recently published the [AWS MCP Server directory](https://awslabs.github.io/mcp/) that provides an up to date list of specialised MCP servers that help you get the most out of AWS (wherever you use MCP, not just with Amazon Q CLI).

This post will walk you through everything you need to know to get Amazon Q CLI up and running to use MCP.

**Configuration**

Amazon Q CLI acts as an MCP Client. In order to connect to MCP Servers to gain access to the tools they surface, we need to create a configuration file called the **mcp.json**. This file needs to be located in **"~/.aws/amazonq"**. This is what my directory layout looks like:

```
.aws
├── amazonq
│   ├── mcp.json
│   ├── profiles
│   ├── cache
│   ├── history
│   └── prompts
```

At the moment this file is empty, so we need to edit it and add an MCP servers to connect to. After looking at the [AWS MCP Server directory](https://awslabs.github.io/mcp/), the one that takes my fancy is the [AWS CDK MCP server](https://awslabs.github.io/mcp/servers/cdk-mcp-server/). When I click on this I get an overview of the features that this MCP Server offers, together with the available Tools. If I scroll a bit further I get the installation details, and I see the following:

```
{
  "mcpServers": {
    "awslabs.cdk-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.cdk-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

Once we have saved the file we are done. Or are we....

One thing to think about as you start exploring and integrating MCP Servers is that these are downloading and installing libraries or containerised images. As such, you will need to make sure that you have installed any dependencies. These are typically documented in the MCP Server details. In this particular case, I need to make sure I have [uv](https://github.com/astral-sh/uv#installation) and Python running, otherwise this is going to fail. Different MCP Servers will have different requirements so make sure you meet them before proceeding.

*Testing the configuration*

Every time you start Amazon Q CLI, you will now see it attempting to load up any MCP Servers that are configured. Here we can see that we get a text hint of how many MCP servers are configured (in this case, I have only configured one so it correctly lists one), and then it shows Amazon Q CLI trying to load the MCP Server up.

{% youtube RUsZlKLxKEg %}

Once completed, the Amazon Q CLI chat interface will launch.

Here are some prompts to test these MCP Servers in action. The first one uses the AWS Cost Analysis MPC Server, and the second one uses the CDK one.

> How much would it cost me to spin up an EC2 instance using an m6g instance. Check the AWS pricing page for the latest pricing updates.
> Can you identify AWS Solutions Constructs pattern to deploy Keycloak

*Running into issues*

If there are any issues with either the way you have added your MCP Server, or perhaps the details for the specific MCP Server itself then you will see errors as Amazon Q CLI starts up. For example, if you have issues with your configuration, then Amazon Q CLI will start (without any MCP Server Tools) with an error similar to:

```
WARNING: Error reading global mcp config: expected value at line 9 column 19
Please check to make sure config is correct. Discarding.
```

You might also see timeout issues if it is struggling to find and downloaded the details you have configured in your **mcp.json**, for example:

```
x awslabcdk_mcp_server has failed to load:
- Operation timed out: recv for initilization
- run with Q_LOG_LEVEL=trace and see $TMPDIR/qlog for detail
x 0 of 1 mcp servers initilized
```

You can go to $TMPDIR/qlog to find various logs generated, and you can configure Q_LOG_LEVEL with either trace, debug, info, and warn configurations to get debug output to help you troubleshoot any issues you might run into.

**Adding multiple MCP servers**

As you start looking at MCP Servers you will most likely want to add/configure a number of different MCP Servers. All you need to do is just add the specific server details in the **mcp.json** configuration between the "mcpServers" curly brackets.

```
{
  "mcpServers": {
	"mcp server details 1",
	"mcp server details 2",
	etc
  }
}
```

When you then restart Amazon Q CLI, you will see a change in the MCP Server status. I quickly added an additional AWS MCP Server to my local **mcp.json** configuration file. Here is my configuration file:

````
{
  "mcpServers": {
    "awslabs.cdk-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.cdk-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    },
    "awslabs.cost-analysis-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.cost-analysis-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR",
        "AWS_PROFILE": "your-aws-profile"
      }
    }
  }
}
````

After saving this and then restarting Amazon Q CLI, I got the following:

```
✓ awslabscdk_mcp_server loaded in 6.15 s
✓ awslabscost_analysis_mcp_server loaded in 18.40 s
✓ 2 of 2 mcp servers initialized
```

As this does affect the startup time, be careful about configuring too many MCP Servers or you might have to wait a long time before you can get started at the Amazon Q CLI prompt.


**Trusting Tools**

Ok so we have figured out how to make MCP Servers and the tools they surface available to Amazon Q CLI. By default tools are not trusted, and so when you go to use them within your Amazon Q CLI sessions you will be prompted every time it wants to use them.

You can toggle trust, changing from untrusted to trusted (and back again) using the "/tools trust" command within the Amazon Q CLI chat. Here is a short video of how we enable trust for one of the tools from the MCP Server we have added.

{% youtube -PVjDzsTAPU %}

Once trusted, as we interact with Amazon Q CLI, it will use these tools without prompting us.

**Removing MCP Servers**

You can easily remove MCP Servers by editing the **mcp.json** file and then either removing the segment within the JSON of the MCP Server you want to remove. After saving the file, the next time you restart Amazon Q CLI, that MCP Server will not load.

**Current limitations**

When configuring Amazon Q CLI to connect to MCP servers, bear in mind that it currently supports connecting to MCP servers locally (via STDIO).

MCP Servers currently only work when using Amazon Q CLI in the chat interface. They do not work as part of the command completion or command translate features of Amazon Q CLI.

**Security**

Before we conclude it is fair to say that whilst MCP is generating a lot of excitement in the developer circles, you should proceed with care. MCP Servers provide opportunities for bad actors to get access to your systems, potentially luring developers in with tantalising MCP servers that are laden with malware.

Treat MCP Servers with care. Be very careful when using the "trust tools" to automatically trust these tools by default. Make sure you scrutinise what you are allowing to be downloaded and installed into your systems.

**Get started with Amazon Q CLI**

This blog showed you how you can use some of your favourite MCP Servers when using Amazon Q CLI. I would love to hear which MCP Servers you are using. I have some amazing and exclusive Amazon Q Developer challenge coins for the best content that is created on this, so get in touch if you do create something and who knows, one of these coins could be heading your way!

I hope this blog post has inspired you to want to try Amazon Q CLI for yourself. You can try it for free by [signing up for a Builder ID](https://community.aws/builderid?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el) and then downloading the app [from here](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el).

Until next time folks!

Made with 🧡 by DevRel!
