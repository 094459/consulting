+++
title = "Amazon Q Developer Tips: No.8 Understanding Context"
date = 2024-12-08
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no8-understanding-context-2305"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no7-generating-better-prompts-ag5).

Ok, time for today's tip....

### Tip 8 - Guiding Amazon Q : Understanding Context

When using AI coding assistants like Amazon Q Developer, the single most important thing to understand in order to get the best code suggestions and output is:

Prompt + Context = Output

In the previous tip, we looked at ways to understand and improve how you approach to writing better prompts ([Amazon Q Developer Tips: No.7 Generating better prompts](https://dev.to/aws/amazon-q-developer-tips-no7-generating-better-prompts-ag5)), in this tip we will look at the context.

**What is context**

Context is one of the most important thing you will need to understand to get the best out of using generative AI tools like Amazon Q Developer. It will make the difference between code suggestions and output that are not helpful and that do not help you with your tasks vs useful and good outputs that you can use within your projects.

Context is the information that is provided to the underlying large language model (LLM) in order to provide you with an answer based on the input (prompt) you provide. You can think about this as having conversations with your colleagues about how to architect or build something, with the additional information you provide to either help them understand or need to provide a better answer.

**Context and Modality**

It is important to understand that how Amazon Q gets context is dependant on how you are using it. If you are using the inline editing modality, the characteristics of what Amazon Q needs to do (be very fast, and provide instance responses) means that the context is very small (the prompt itself). If you are in the chat interface, then the responses do not have to be immediate, and so the context can be larger. 

As Amazon Q Developer will use context differently depending on which Amazon Q Developer tool you are using, you should think about this when you come to think which tool you might want to use to perform a specific task. You will find that with constant use, this thinking becomes second nature and intuitive.

**Examples of context**

Here are some of the ways that Amazon Q Developer gathers and uses context.

*Import statements*

You can influence the suggestions that Amazon Q provides you by adding the libraries you want to use at the start of your code. For example, if I ask Amazon Q to create code for a python web framework, with a blank project file, I might get Flask, FastAPI, or DJango. If I first add 'from flask import Flask' at the top of the page, it will almost always provide me with Flask code*

*I say nearly, as it is impossible to be 100% certain with non deterministic systems

*Open Files or tabs*

The first place that Amazon Q looks for context when using Chat interface is the files you have open within the IDE. It can be a good idea to just keep the key files open you need to help focus Amazon Q. As you start using Amazon Q it will soon become nature to bring up and close open files which you will provide as additional input into your prompts in the chat interface. A good example of this is that if you are fixing problems, you should try and isolate the relevant code and keep that as the open/highlighted tab when prompting.

In addition, Amazon Q is smart enough to understand that important context can be obtained from key files. If you are working with Java projects, it will read your pom.xml for example.

*Scaffolding*

We can help steer the output of how Amazon Q works by providing scaffolds. There are two ways we can do this: 1/ Provide details in a markdown doc in our project directory, and refer to these in our prompts, and 2/ Provide them directly within the prompt itself. When using Amazon Q Developer Agents (such as /dev for example), you can provide additional info within the prompt to help scaffold the code that is created. We will see some more examples of this in future tips.

*Command line context*

If you are using Amazon Q Developer via the command line, you should be aware that you can provide additional context when using it using the @git, @env, or @history. Check out this blog post, [Generating Accurate Git Commit Messages with Amazon Q Developer CLI Context Modifiers](https://aws.amazon.com/blogs/devops/generating-accurate-git-commit-messages-with-amazon-q-developer-cli-context-modifiers/), which dives into this in more detail.

*All the files in your project*

You can use Amazon Q Developer Workspace Index to index your project workspace, which enables all the files within your projects to be accessible as context. It is important to know that this functions like a search rather than an actual directory listing. When using @workspace, the search returned will provide relevant context together with your prompt. You can refer to file explicitly though, and this is useful if you need to refer to multiple files when asking a question. We are going to see a lot of tips that make use of this feature.

*Conversation history*
 
 As you use the Amazon Q Developer chat interface remember that this is not just a one time prompt. Amazon Q Developer retains a history of the conversation, meaning that you can refine and "funnel" follow up questions to get improved code suggestions. Do not close chat interfaces unnecessarily as you will lose that history and context. You can open up several chat interface tabs by clicking on the "+" icon in the chat interface. Each of these will be new conversations with new history and context. You can open up to ten of these chat conversations - this should be plenty for most projects you are working on.

*Providing feedback*

The use of feedback (thumbs up/down) can help shape context as it provides positive reinforcement, as well as reduce future occurrences of suggestions you have down voted.

**Additional things to think about**

*Size limits*

The Amazon Q Chat interface has a maximum of 4000 characters (at the time of writing this, November 2024) which is the maximum input that Amazon Q Developer can process. This is important to know as context is not infinite, and if you are working with very large files, or have lengthy prompts with additional information you might experience inconsistent outputs. A good example of this is when using the "Amazon Q > Send to Prompt" feature which might leave no space for your actual prompt.

This might influence how you structure your projects - for example, breaking projects into small files can often work well (see next consideration).

*Small files*

Because context sizes are so important, and they are of a finite size, you might find better results by breaking down your project into smaller files. This will allow those files to reside within the context space available.

*Project workspace*

If you are wanting to work in a project (for example Python) but have a lot of other code in your workspace (perhaps because you are working in a mono repo environment) the responses you can get from Amazon Q may not be what you expect. You might get Javascript or Python despite the project you are working in being in the other language. The best way to tackle this is to try and setup your IDE so that it is just working in a subfolder of your mono repo and avoid files within your local workspace that are a distraction.

*Customisation*

Amazon Q Developer allows you to provide your own code to help influence code suggestions. This is currently only available with the Professional Tier, and not in scope within this workshop. It is good to know that this capability is very powerful, allow developers to have a number of customised models that they can use depending on the different custom code they want to use. Check out [this video](https://www.youtube.com/watch?v=dsjXb4TvfPg) for more info.

*Viewing context in the logs*

If you want to get low level and see this working, you can check the logging of the Amazon Q Developer plugin and see this in action.

**Try Amazon Q Developer today, and claim your free Builder ID**

In this tip I provided an overview of how important context is when using Amazon Q Developer. In future tips I will dive into some specific examples of these and show you how to get the best outcomes for the tasks you are doing.


You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
