+++
title = "Amazon Q Developer Tips: No.19 Amazon Q Developer Agents - /doc"
date = 2024-12-19
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no19-amazon-q-developer-agents-doc-4d1k"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no18-amazon-q-developer-agents-dev-1i0).

Ok, time for today's tip....

### Tip 19 - Amazon Q Developer Agents : /doc

Amazon Q Developer provides a number of tools for developers to use. /doc is a new addition that was announced at re:Invent 2024, and provides a simplified approach to generating documentation. 

You invoke using the /doc and then press enter (when I first used it I thought it worked like /dev and I could add some additional information in the prompt, but this is not how this worked). After hitting enter again, you have two choices: 1/ Create a new README file, or 2/ Update an existing one.

You will typically use /doc towards the end of your coding activities within your project. You want to make sure that as much of it is complete and working, that you have already added appropriate tests as needed, and completed remediating any issues that came up when using /review, for example. If you make changes after, you are going to need to potentially update the docs to reflect those changes.

*Creating a new README*

If you have not created a README file, then selecting this option will start the workflow for creating your README. You will select a directory in which you want the /doc agent to use as it's root, and from where it will start working to understand and then document your code. 

Once kicked off, it will start scanning, summarising, and then generating your README file. The UI does a nice job of showing you where its at, and in my experience this process only takes a few minutes.

You have the opportunity of reviewing the README once complete, which you should check. If it is not quite what you wanted, use the "Make Changes" button, which will provide you a prompt to provide some follow up information - for example, include something that was missed, add a new section, or fix something you saw was wrong. Do this now to avoid using one of your quota.

*Updating an existing README*

You can use /doc to update an existing README that you have. For example, maybe you have made a code update to add a new feature, or changed how the application works. When invoking /doc and selecting the Update feature, you are provided with a couple of options.

* Update the README with recent code changes  - this is especially useful when you have made changes, which will then update the existing README to reflect those updates
* Make a specific change - you provide additional details with a prompt, for example adding something to the README that was omitted when it when it was initially created

**Things to know about**

I have spent only a little time getting to know how /doc works, so will update this tip in the future as I learn more. In the meantime, here are some initial thoughts on things to think about:

* How big is your project? - /doc does a really good job of putting together documentation (README) but works better with a smaller set of files. If you are generating documentation for an existing codebase, you can use the "directory" feature to set that as the root of where Amazon Q Developer will explore to get what it needs to create the documentation. Try and break down your project into different areas from a doc perspective (backend, data, api, etc) and then generate docs for each of those areas).
* Service quota - /doc is subject to limited invocations based on whether you are using the Free Tier or Professional Tier. Currently when using any of the agents (/doc, /dev, /test, or /review) they all count towards your single quota, which is currently set to ten. The [pricing page](https://aws.amazon.com/q/developer/pricing/) is currently being updated so hopefully by the time you read this it should be good.
* Excluding files - /doc filters out files or folders defined in a .gitignore file. If you want to exclude any files or folders from being reviewed for documentation generation, you can include them in a .gitignore file in your project or workspace.
* Will not add doc strings  within your files - /doc does not current document your actual project files, only creates project documentation. If you need to do this, you can use /dev to update your project files, or (my preference) is to add these as you develop (see below).

**Generating documentation without /doc**

My view is that this capability will soon become an essential tool that developers use. I did want to share however, a few other ways that you can use other Amazon Q Developer tools to help you create and update documentation in your projects. These might come in handy, so always good to know.

*Using the chat interface*

You can use the chat interface to generate documentation or doc strings for either the current file you are working on (making sure you have that file open in the editor), or you can use @workspace to generate documentation across multiple files within your workspace. This tends to work well, as you are creating a single file (README.md for example) and can copy the contents into this file. However, if you ask to provide documentation at a more granular level (for example, at each function) then you are going to need to update a lot of files.

*Using in-line prompting*

One of my favourite ways to document as I code is to use the in-line prompt (COMMAND + I) and then use the prompt "document this code block", which then quickly adds the required documentation as I go along. This is still super useful when using the /doc feature as it provides more context and details which it can incorporate within the README it generates, so whether you are using /doc or not, this is a good habit to get into, and one that Amazon Q Developer simplifies.

**Adding diagrams to your documentation**

Another thing I have started to experiment with is using Amazon Q Developer to help me create architecture diagrams that I can include in the documentation. A recent example is how I used Amazon Q to help me document my data model for some demo applications I have been developing live in my talk "From zero to shipped in 30 minutes". After Amazon Q Developer has created the initial data model, I follow up with the following prompt:

> Create a mermaid diagram of this sql code that I can display in a markdown doc

Which outputs in the chat interface the mermaid code, which I can then easily incorporate into documentation (the first time I had to ask Amazon Q how to do this with a prompt "Add the markdown to display this")

![data model diagram done by amazon q](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/j2zursbwid0w6802f5ur.png)

I have tried this on other well know data sets, like the New York Taxi data set which anyone who works in analytics will be familiar with. I loaded up the schema in my local VSCode, opened up the file and then asked the same prompt. I was happy with the output.

![NYC-taxi schema](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/12nvlhq7aohbewddsw6a.png)

> **Tip!** You can also go the other way around, you can get Amazon Q Developer to **GENERATE** SQL from a diagram. This is super handy if all you have is the documented schema but not the source


**Try Amazon Q Developer today, and claim your free Builder ID**

That's it for today's tip. Let me know how you get on with this tip, and if you have your own drop me a message or reply. I would love to feature them here.

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
