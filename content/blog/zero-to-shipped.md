+++
title = "Zero to shipped - a year in review"
date = 2025-12-04
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/zero-to-shipped-a-year-in-review-3in9"
+++

## A year of Zero to Shipped

I am at [Build Stuff](https://buildstuff.events/pages/agenda) doing my live coding talk, Zero to Shipped in 30 minutes. I have done this "talk" many times this year, and as I look back to January when I did the same session at [PyCon+Web](https://www.pyconweb.com/) in Berlin, what amazes me is how far AI Coding Assistants have come in such a short period of time.

Back then I used Amazon Q Developer (pre agentic mode), and a lot has changed. At Build Stuff I did the same talk, but now I am using [Kiro](https://kiro.dev) and [Kiro CLI](https://kiro.dev/cli/). After the talk I had a lot of folk who asked me to write down the good practices so I could share with them. Whilst we wait for the video to appear, this is that post. Whether you are at Build Stuff or not, you can follow along as I share how I was able to go from Zero to Shipped in 30 minutes. The idea is to build a finished working application, that is ready to ship to AWS. I have tried different applications over the last 11 months, but at Build Stuff I created a simple fact checking application - we need more trust in the world!

> I will post an update in the future once Build Stuff release the video on Youtube

I have shared the resources I used in the talk in a new Github repo, [ai-agent-resources](https://github.com/094459/ai-agent-resources) which I will link to in the post below. I have also uploaded the contents of the finished application that I shipped to AWS in a different repo, [build-stuff-zero-to-shipped](https://github.com/094459/build-stuff-zero-to-shipped).

## Make your IDE work how you want to

After you install your next generation developer tool (for me, this is Kiro as you asked so nicely!) your first job is to tailor it to your specific developer personality. I have yet to meet two developers who worked identically - we all have our preferences and ways we like to work, so that is what we need to do first.

In Kiro we can do this using [Steering documents](https://kiro.dev/docs/steering/?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el). Steering documents are text documents saved as markdown, that live in a special directory in your project workspace. We can either add these manually ourselves, or create them via the Kiro UI.

During the talk I covered a few good practices in how to approach creating and using these to personalise your developer setup.

* keep your steering documents small and focused - whilst context windows for the large language models (LLMs) are increasingly, in my experience, smaller, focused steering documents perform much better than large ones
* keep them updated - steering documents are living documents that should be curated, edited and updated as you use them
* use multiple steering documents as needed - you can have many steering documents within your project, so choose or create ones that you need for the task at hand
* per domain steering documents to make it easier to maintain - I have found it easier to keep a number of domain specific steering documents (coding standards, deployment, api-design, etc) as this allows me to maintain and manage these documents and keep them up to date
* start small - if you are creating new steering documents, start small and build up from there - try and avoid the temptation of dumping everything, and if you do, edit ruthlessly
* use inclusion to control when steering docs are used - I demonstrated how steering documents can be created using different inclusion modes and how this affected their use within Kiro - this allows you to control with precision which steering documents you want to use for a given task

During the demo I demonstrated the before and after of using a steering document to change the output of Kiro - from generic output, to one that was highly tailored to my preferences. I created the following steering document which I use in every project I do, and sets out my consistent standards. When I look back to the first time I did this talk in January, the steering doc only have half the contents in it, and has changed considerably over the last eleven months.

```
---
inclusion: always
---

# Coding Preference

You have a preference for writing code in Python. 

## Python Frameworks

When creating Python code, use the following guidance:

- Use Flask as the web framework
- Follow Flask's application factory pattern
- Use Pydantic for data validation
- Use environment variables for configuration
- Implement Flask-SQLAlchemy for database operations

## Project Structure and Layout

Use the following project structure

├ app
	├── src
	├── src/static/
	├── src/models/
	├── src/routes/
	├── src/templates/
	├── src/extensions.py

## Local and Prod configurations

- Run local development setups on 127.0.0.1:5001
- Run production configurations via gunicorn
- Configure via env variables

## Python Package Management with uv

- Use uv exclusively for Python package management in all projects.
- All Python dependencies **must be installed, synchronized, and locked** using uv
- Never use pip, pip-tools, poetry, or conda directly for dependency management
- Use these commands - Install dependencies: `uv add <package>`,  Remove dependencies: `uv remove <package>` and Sync dependencies: `uv sync`
- Run a Python script with `uv run <script-name>.py`
- Run Python tools like Pytest with `uv run pytest` or `uv run ruff`
- Launch a Python repl with `uv run python`
- Configure [tool.hatch.build.targets.wheel] packages with the correct value for the project

```
[source](https://github.com/094459/ai-agent-resources/blob/main/kiro-steering/python-preferences.md)

## Automating developer tasks

Developers love to automate the work they do, and I have yet to meet one who did not spend time or obsess over how to improve their efficiency through automation.

I showed how Kiro helps developers with automation, allowing them to leverage the abilities of LLMs to automate some of the tasks they have to do. Kiro [Agent Hooks](https://kiro.dev/docs/hooks/?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el) is a powerful mechanism that allows you to create a prompt that Kiro will run after a given event. The events that are currently supported are when files are created, saved, or deleted, and you can apply filters so that these only run when they match a pattern you define (for example, all files ending in .py).

I demonstrated how to create an Agent Hook that adds copyright and SPDX open source headers to new files as they are created. I also shared [some other ideas here](https://github.com/094459/ai-agent-resources/tree/main/kiro-sample-hooks) of how you might use these to automate some of your development tasks.

Kiro Agent Hooks are just configuration files that live in the ".kiro/hooks" directory of your project workspace, so you can edit them directly or via Kiro. This was the one that I created 

```
{
  "enabled": true,
  "name": "Add License Headers",
  "description": "Automatically adds SPDX 2.0 headers for Apache 2.0 license and copyright notice '(C)opyright 2025 BeachGeek.co.uk' to Python files when they are created or edited",
  "version": "1",
  "when": {
    "type": "fileCreated",
    "patterns": [
      "**/*.py"
    ]
  },
  "then": {
    "type": "askAgent",
    "prompt": "Check if this Python file has the proper SPDX 2.0 license header for Apache 2.0 and the copyright notice '# (C)opyright 2025 BeachGeek.co.uk'. If missing, add them at the top of the file in the correct format: SPDX-License-Identifier: Apache-2.0 followed by the copyright line."
  }
}
```

[source](https://github.com/094459/build-stuff-zero-to-shipped/blob/main/kiro/fact-checker/.kiro/hooks/add-license-headers.kiro.hook)

During the rest of the demo we saw as this Kiro Agent Hook kicked in, adding the right copyright information and SPDX information needed as it created its own files.

## Look beyond text

Most of the time, we working with text. Source code, markdown documentation, log files and more. However, AI coding tools like Kiro are also able to understand and use images as useful context or inputs. As a developer, this is something that could be useful - have some architecture diagrams in a doc that perhaps you want to generate some code for? Maybe you have white boarded some designs - take a picture and feed that in and let Kiro take care of the rest.

During this demo I took an entity relationship diagram for a fact checking data model (you can see the [diagram here](https://raw.githubusercontent.com/094459/build-stuff-zero-to-shipped/refs/heads/main/resources/fact-checker-erd.png). Kiro allows you to upload images through the chat interface and then provide a prompt. After attaching the above picture, I used the following prompt:

```
Generate the data model in SQL from the ERD diagram. Store it in the data-model directory, in a file called fact-checker.sql
```

In a few seconds it generated the required SQL file, which you can view [here](https://github.com/094459/build-stuff-zero-to-shipped/blob/main/kiro/fact-checker/data-model/fact-checker.sql)

If you are not using images as context with your AI coding assistant today, you should start to think where it makes sense to incorporate this. I see few developers thinking of images as first class citizens, but the reality is that they work great - experiment and find out what works for you.

## Using data as context

In the first part of the demo I talked about steering documents to help setup your tool to work the way you wanted. That is only one part of the story. You also need to think about steering documents based on the task you are trying to do.

Application specific context is critical to make sure that your AI coding assistant does what you want it to do. Using data models is a great way to provide that anchor, providing a strong foundation and context for the LLM to generate code.  During the demo I showed how we can add this via the chat interface of Kiro. There are many ways that you can add context, but including a folder is one of the ways we can add precise context and steer Kiro in the direction we want.

## The importance of refining your prompt

So far during the demo we have not actually got Kiro to write any application code, we have focused on getting our intent and setup right. We can now focus on creating a prompt that we can use to start the process. I have done other talks where I [shared tips on prompt and context engineering](https://ricsuepublicresources.s3.eu-west-1.amazonaws.com/pdf/ricsue-tips-to-better-prompt.pdf) and one of the things that I recommend is to use your AI coding assistant to help you improve your initial prompt via meta prompting.

During the demo we started off with the following prompt:

```
Build a simple Fact Checking application. 

- Use the data model in the "data-model/fact-checker.sql"
- Generate a web application that can be used in a browser
- Users will need to register with an email address to login
- When Users login, a Dashboard will be displayed that provides a simple explanation of what the application does, and displays any available Facts that have been created
- From the home Dashboard, Users will be able to click on any existing Facts to fact check. They will also be able to Create a new Fact or Create a new Category
- When Users are viewing Facts, they will have the ability to click on two buttons - Fact or Fake
- When Users are viewing Facts, they can also provide supporting info
-  Provide a simple web design that can be updated easily using CSS
```

However, before using this, I add the following at the beginning:

```
Can you review the following prompt and suggest areas where it should be improved. I want the prompt in EARS format. Here is the prompt:
```

You might be asking yourself, what is this EARS thing? Easy Application Requirements Syntax (EARS), is a mature approach to defining requirements that came out of Rolls Royce over 20 years ago. Why EARS? As it turns out, it produces output that is easy to understand and specific. And it turns out that LLMs seem to work well with context provided in this format.  The key takeaway here is that if you are not using this technique today, you should. You should spend time and experiment to see what works for your task or use case.

If you run this yourself, you will see that Kiro will suggest how to improve the original prompt as well as providing it in a new format - the EARS format. You can check the output if you run this yourself from the chat interface. After providing you with this improved starting prompt, Kiro is super keen to start writing code. Hold off though, we don't want to unleash it yet.

## A step towards spec driven development

In days gone by we might have yielded to our inner Vibe and gone ahead and got Kiro to generate some code. We can do better though, and a technique that I have seen work very well is to create a document from this. From the Kiro chat interface, using a prompt like the following:

```
Can you write the new improved prompt to a new file called "code_plan.md" in a planning directory
```

Will take the output from our meta prompt and then write it out to a document (in this case, called code_plan.md). Why do this I can hear you thinking to yourself. It turns out that by capturing our starting prompt as a document, we provide our AI coding assistant with a better anchor point going forward. We are no longer tied to this conversation or context window, and we can refer back to this document throughout the subsequent activities.

This is a technique that has been used by developers over the past year, and you might hear it sometimes referred to as prompt driven development. This is kind of a first tentative step towards spec driven development, which we will come to later on.

## Finally, writing some code

What was once exciting, using the AI coding tool to generate code has now become routine and normalised. By setting up everything so far, we have created a smooth path for the model to generate good code that does what we want.

It takes about 4-5 minutes to finish, but we soon have our application ready. After starting it and checking out the functionality, we have reached an important milestone - a working app. 

## Check yo self.

As Ice Cube once sang, you need to "Check Yo Self!" when you use AI coding assistants to generate code. Whilst they are getting better, they still hallucinate and can still produce code that might container bad practices so you need to be on the ball. Some AI coding assistants provide an integrated security scanning tool (for example, Amazon Q Developer within VS Code has a /review feature that fires off a scan of your project). Increasingly though I am seeing this enabled via Model Context Protocol (MCP) servers that integrate tools that help you.

During the demo I show how to integrate a really nice open source project from AWS called [Automated Security Helper](https://github.com/awslabs/automated-security-helper), that runs a collection of open source tools that provide security and quality checks of the code. To add this to your AI coding assistant, its as simple as adding it as an MCP server

```
{
  "mcpServers": {
    "ash": {
      "command": "uvx",
      "args": [
        "--from=git+https://github.com/awslabs/automated-security-helper@v3.1.2",
        "ash",
        "mcp"
      ],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

And then once loaded, we have a [new set of tools](https://github.com/awslabs/automated-security-helper?tab=readme-ov-file#available-mcp-tools) that our AI coding assistant can use:

* scan_directory	- Perform a complete security scan
* scan_directory_with_progress	 - Start a scan with real-time progress tracking
* get_scan_progress	- Get current progress of a running scan
* get_scan_results	- Get final results of a completed scan
* list_active_scans	- List all active and recent scans
* cancel_scan	- Cancel a running scan
* check_installation -Verify ASH installation and dependencies, super helpful to troubleshoot any setup issues

we can use prompts like the following, to start using these tools:

```
Please run ASH on the "app/src" folder and analyze the results
```

This starts a scan, and Kiro initiates a scan and beings it work. During this time, it is worth talking about these new tools and trust. By default new tools added by MCP servers are not trusted. As Kiro starts using the different Ash tools, you will be prompted to run these. As tempting as it is to trust tools automatically, you should take care and only trust those tools you have reviewed and understand how they will interact with your system.

![Example screenshot form Kiro running Ash](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fg61aedgzzq5lxtcruh22.png)

After a few minutes, I get the results in the chat interface - all systems go (so far!)

```
ASH Security Scan Results - Analysis
Excellent news! The ASH security scan completed successfully with zero security findings.

Scan Summary:

Status: Completed ✓
Duration: ~60 seconds
Total Findings: 0
Actionable Issues: 0
Scanners Run (6 passed):

Bandit (Python security) - PASSED ✓
Semgrep (Static analysis) - PASSED ✓
Checkov (Infrastructure security) - PASSED ✓
Detect-secrets (Secret detection) - PASSED ✓
npm-audit (JavaScript dependencies) - PASSED ✓
cdk-nag (CDK security) - PASSED ✓
Severity Breakdown:

Critical: 0
High: 0
Medium: 0
Low: 0
Info: 0
What This Means:

The Fact Checker application code is clean with no detected security vulnerabilities. The scanners checked for:

Python code security issues (SQL injection, XSS, insecure functions)
Hardcoded secrets or credentials
Infrastructure misconfigurations
Dependency vulnerabilities
Common security anti-patterns
The application follows security best practices including password hashing with werkzeug, parameterized database queries via SQLAlchemy ORM, and proper authentication with Flask-Login.
```

This looks great, no additional work we need to do. If there were findings, you can then use your AI coding assistant to work through these. Good practice is that you should manage these one at a time - as tempting as it is to get all of the issues addressed in one go, experience has shown that your mileage will vary based on the complexity of the issue and the size of your project.

You can also do other tests. Another great MCP server is the A11y MCP server that provides a way for you to scan and generate reports on how accessible your application is. I add the following MCP configuration:

```
   "a11y": {
      "command": "npx",
      "args": ["a11y-mcp"],
      "disabled": false
    }
```

I then start my application so that it can be accessed over http, and kick start off an assessment with the following prompt:

```
Use the a11y MCP server to audit http://127.0.0.1:5001 for accessibility issues. Generate an issues_log.md file to document any issues.
```

After a few minutes, it generates its findings for me.

```
Key Findings:

The application has 1 serious accessibility issue - insufficient color contrast on primary buttons and links. The current blue color (#3498db) only provides a 3.15:1 contrast ratio, but WCAG 2.1 AA requires 4.5:1.

Quick Fix: Change the primary blue from #3498db to #2874a6 in the CSS file to achieve 4.51:1 contrast ratio and meet WCAG AA standards.

The good news is that the application passed 26 other accessibility tests, showing a solid foundation with proper HTML structure, form labels, semantic markup, and keyboard navigation support.
```

I can now ask Kiro to just go ahead and remediate these outstanding issues:

```
Please resolve outstanding accessibility issues and rescan
```

And after some changes, and re-running the report generator, this times gives the application a clean bill of health. Because I asked it to create and document this in an "issues_log.md" file, I now have an audit trail.

```
# Accessibility Audit Report - Fact Checker Application

**Audit Date:** December 4, 2025  
**Tool:** axe-core via a11y MCP Server  
**Standards:** WCAG 2.0 Level A, AA, WCAG 2.1 Level AA, Best Practices  
**Base URL:** http://127.0.0.1:5001

---

## Executive Summary

✅ **ALL ISSUES RESOLVED** - The accessibility audit now shows **0 violations**. All identified issues have been fixed and the application passes all WCAG 2.1 AA accessibility tests.

### Overall Statistics
- **Total Issues:** 0 ✅
- **Passed Tests:** 26
- **Incomplete Tests:** 0
- **Pages Audited:** 2

### Resolution Summary
- Fixed color contrast issues by updating primary blue from #3498db to #2874a6
- Added underlines to links to distinguish them from surrounding text
- All pages now meet WCAG 2.1 AA standards

```

Depending on your workflow, task, or work environment, you may need to use a combination of MCP servers to help you move beyond just the writing of the code and to making sure the code is fit for purpose.

Before leaving though, I disabled the MCP servers - they can fill your context window quickly, so use and then turn them off when you do not need them!

## Brownfield development

Whilst Kiro was generating code, I switched to a different use case, specifically how to use tools like Kiro when working with existing code bases. Developers will typically do most of their work on existing applications, and so understanding how you can use tools like Kiro to help you with situational awareness is important. After all how many times have you been handed a project and it had perfect, up to date documentation? Yeah, exactly :-) Even if you do have documentation, providing additional insights are super useful.

Using a [book sharing application](https://github.com/094459/build-stuff-zero-to-shipped/tree/main/brownfield/book-sharing-app) that I had developed a while ago, I showed how you can use Kiro to generate context files using a feature called "Generate Steering docs" from the IDE.

After about 2-3 minutes Kiro had produced three steering documents:

* product.md - a breakdown of what this application does (and yeah, it got all the details for this book sharing site pretty spot on)
* tech.md - a technical summary, including libraries and tools with versions - it got everything right and didnt seem to miss much
* structure.md - an overview of the layout of the project - again, this was accurate

Kiro uses these as steering when we ask it to do something. So I asked to add a new feature:

```
Create a new feature that adds a Contact Us page to this application - keep it simple, just email address and telephone number
```

After less than five minutes Kiro had added this new code, keeping the conventions of the existing codebase.

## Reverting via Checkpoints

Before switching back to the main thread of building our Fact Checking application,  what do you do if AI coding tools generate code that you don't like? Perhaps the new code has introduced breaking changes that need to be fixed, but after spending some time and even more changes you are in a worse situation than when you started.

This is a common scenario and so it is important to think about your strategies of not just how you use AI coding assistants to write code but how you approach undoing or removing code.

Whilst the temptation to ask your AI coding assistant to "undo" or "revert" is strong, I would caution against this - there are better options!

* using source control - you are hopefully using source control within your repo, and so if you get yourself stuck, use source control to revert back to your last known change and start again
* use checkpoints - some AI coding assistants like Kiro support the ability to revert back to a previous checkpoint - allowing you to undo concretely any of the changes made

Both of these represent better options than using AI coding assistants to make the changes for you. Once thing to bear in mind if you use source control is that you will need to update the AI coding assistant and tell it what you have done. It its "memory" (context window) it still think those changes were golden. I often use a prompt like "I have made some manual changes, please re-read the source files before proceeding" as a way to ensure that the context window is updated.

## Creating specialised agents

Ok back to our application, which is running and has passed its security and accessibility checks so we are good to try and deploy this. Whilst I could probably get Kiro to do this, this feels like the kind of work best done in the terminal. Luckily I have just the tool I need in [Kiro CLI](https://kiro.dev/cli/?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el). The same agentic AI power, but in the terminal.

Kiro CLI provides a mechanism to customise the behaviour of how it works through something called [Custom Agents](https://kiro.dev/docs/cli/custom-agents/?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el). This is in essence a json configuration file that defines the characteristics for our CLI AI coding assistant - it allows you to configure a system prompt, define tools (via MCP configuration), configure default permissions and trust for those tools, define context resources you want to automatically load and more. There is not enough time to do Kiro CLI justice when I do this live, but I have a hands on workshop you can follow if you are interested (see at the end).

After opening up a terminal in the same directory as the IDE project, I create a "devOps" custom agent using the following configuration.

```
{
  "name": "devops",
  "description": "Kiro CLI agent used for packaging and deploying apps",
  "prompt": "You are a Senior DevOps Engineer and Backend Solutions Developer with expertise in Terraform, Python, Bash scripting, and AWS Cloud Services.",
  "mcpServers": {
    "Finch": {
      "command": "uvx",
      "args": ["awslabs.finch-mcp-server@latest"],
      "disabled": false
    },
     "AWS Docs": {
      "url": "https://knowledge-mcp.global.api.aws",
      "disabled": false
    },
    "Terraform": {
      "command": "uvx",
      "args": ["awslabs.terraform-mcp-server@latest"],
      "disabled": false
    }
  },
  "tools": [
    "*"
  ],
  "toolAliases": {},
  "allowedTools": [],
  "resources": [
    "file://.kiro/steering/**/*.md"
  ],
  "hooks": {},
  "toolsSettings": {},
  "useLegacyMcpJson": true,
  "model": null
```

Reviewing this configuration you will see a few things. First we define a role or persona for this custom agent to use (DevOps person). We provide it the same context resources as when we were building our application. Finally we add three MCP servers - AWS Docs, Finch, and Terraform. We will see why in a moment.

After I create this, and restart Kiro CLI, I now have my super duper DevOps agent ready to help me package up this application and ship it to AWS. Before I do that, I have to make some decisions.

* I want to deploy to my nearest AWS region - as I am in Lithuania, the eu-north-1 Stockholm region is closest
* I want to package up this application as a container image, but I use Finch as my container development environment on my local machine not docker
* Even though I love open source, Amazon ECS is still my favourite container orchestration service so I decide I want to deploy my container to Amazon ECS
* I am using a Mac M1 machine which is using an Arm based processor - the container image needs to be built so that its multi-architecture, although my preference is for Amazon ECS to use AWS Graviton based instances as they are super awesome
* I decide that I will use Terraform for infrastructure as code - whilst I typically use CDK as I prefer writing iac as code, for demo purposes Terraform allows me to deploy more quickly
* I want to make sure that I test locally before building the infrastructure - I want to be able to test on a local container before green lighting the infrastructure build

These are not necessarily the best solutions if I was running this for real, but when you are time constrained in a demo (30 mins) then these are solid choices.

I craft a detailed prompt like the following:

```
Using the AWS Knowledge base MCP Server for the latest doc updates, review this application and update so that it can:
- deployed on Amazon ECS in the eu-north-1 region
- I want the simplest deployment, with basic capacity and a public URL that I can access anywhere on the web
- My local setup is Arm, ensure the Amazon ECS cluster uses Arm based instances
- Use the Terraform MCP server to generate IaC
- I am using Finch not Docker (use the Finch MCP server when needed)
- Make sure you build the container image first before building the Terraform infr
- Make sure that the listening port is adjusted so that it will work when running in a container 
- Create a script that allows local testing before it runs the Terraform infrastructure build
- Make sure you copy the SQLite database 
```

Kiro CLI starts working away, and in a similar way to how we saw in the Kiro IDE - when Kiro CLI tries to use a tool that is not trusted, we are asked for permission. You will be prompted several times as it builds the scripts and writes Terraform HCL. After about 2-3 minutes though, we have our first candidate.

## Deploying with confidence

The final part of the session showed me deploying the application to AWS. The deployment took around 5-6 minutes, and the demo Goddess was on my side and with seconds to spare, I showed the application running in the Clouds. Zero to shipped within 30 (or so) minutes.

## A peek into the future with spec driven development

Whilst the deployment script was running, I walked through how you might approach building the same application using a different approach to Vibe coding. Spec driven development follows a more structured approach, building from intent and creating requirements documents. From that technical designs are generated before a detailed implementation plan.

If you are interested then Gunnar Grosch and myself recently did a talk at Øredev on using Kiro for spec driven development.

{{< youtube FO7aeKI9Vnk >}}

## Conclusion

If you have attended the Zero to Shipped talk, I hope you found it useful. I hope that you were able to apply some of the techniques to your setup. I hope that it encouraged you to explore and experiment and improve how these tools work for you. We are still at the very early stages of how these tools are transforming the work of developers, and we are discovering and learning new things ALL the time.

You can get started with Kiro today for free. [Download it from this link](https://kiro.dev/downloads/?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el) and then login using GitHub or your [Builder ID](https://builder.aws.com/start?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el). When you initially sign up you get a very generous 500 credits which are renew every month (50 for the free tier). 

I have created a couple of workshops if you want to get deeper into Kiro. The [Kiro CLI workshop](https://github.com/094459/aqd-cli-workshop) will walk you through getting started with the terminal based Kiro CLI tool, and provides a comprehensive overview as well as advanced topics. My [spec driven development](https://github.com/094459/sdd-workshop) workshop dives more into using Kiro in spec driven mode.

I want to say a big thank you to the organisers of Build Stuff, who have put together a really amazing event with a super engaged developer audience. It is really great to see more developer focused events like this on the conference circuit, and if you get the chance to either speak or attend, I would not hesitate to recommend it. I will be sure to be back in 2026 (if they have me!)
