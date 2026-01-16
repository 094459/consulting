+++
title = "Amazon Q Developer Tips: No.23 Debugging with Amazon Q"
date = 2024-12-23
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no23-debugging-with-amazon-q-11ee"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no22-amazon-q-keyboard-shortcuts-2kfc).

Ok, time for today's tip....

### Tip 23 - Amazon Q Developer : Debugging tips and tricks

I write a lot of bad code :-) that rarely works first time. Whilst the modern IDE (VSCode and Zed mainly these days) does reduce common issues such as typos and other formatting errors, I am super grateful for Amazon Q Developer. It provides me with another set of eyes and opinions as to what an error might be.

In today's tip I want to share some of the ways I am using it to help me troubleshoot issues, find bugs in my code, and help explain general weirdness that I cannot sometimes figure out for myself.

I have listed some of the ways that I find helpful, but this is a fast changing space and I am always discovering new ways to effectively bug hunt using Amazon Q. I would love to hear some of your tips if you can share.

- prompt design
- reduce files and complexity
- context and debugging

**Summarise the error message**

Error messages vary - some are clear, concise, and give you a good understanding of what the issue might be (for example, include error codes and something very specific), where as others might be very generic and provide either too much info, or not enough. Regardless, the first step is to summarise what are the key parts of the error that are relevant. What I have found works for me include:

* capturing the final error message which references any files or resources
* including line numbers and other references (file or configuration details)
* anything that appears like it might be an error code
* information on a UI screen that might be different to what is displayed in the logs

I put this into a short summary which I then provide to the prompt. It is not perfect, but I have found that over time I have got better at knowing what to include and what to exclude.

**Prompt design**

When I am trying to fix errors that come up, I have found that I re-use certain prompts/phrases that seem to work well.

> Tell me how to fix - {add summary of error}
> When doing XX in the application, I get this error - {add summary of error}
> The code generates this error - {add summary of error}
> Fix - {add summary of error}

**Provide the right context**

It is especially helpful if you are able to provide additional information and context. I try and add details about what I was doing within the application (for example, if an application has a registration page and the error happens when I try and register, I add this as additional information).

I will also try and have open in the editor the file that I think is most likely to be the root cause of the issue. This might be based on information in the error itself, or my own intuition and knowledge of the application. I will sometimes repeat the prompt with different files open that provides different context.

You can use @workspace together with the above to broaden the visibility of relevant files and code that might help narrow down where the issue is.

**Using Explain**

If I am working on troubleshooting errors with an application or code base that I do not know, I have found using Amazon Q Developers "Explain" feature super helpful. As well as using this to help me find out more about the code, I also use it together with the actual error message and details to see if this can help nudge me in the right direction to finding a fix, or provide ideas for things to look at.

**More than just code**

If I am running local build systems locally, or building and packaging up container images, I spend a lot of time in the terminal. I get my fair share of errors and what I have found is that Amazon Q Developer is really great at helping me quickly get to the root of an issue - especially errors generated from the various AWS cli tools that I use.

If you are regularly using command line tools, why not try using the Amazon Q Developer chat interface to help you fix any errors the next time they come up. 

**Chasing it's tail**

As you use Amazon Q Developer to help you fix issues with code, you might encounter a situation where the responses become circular. What I mean is that after providing a prompt and implementing the coding suggestions, you end up with a situation where subsequent prompts lead to you repeating previous coding suggestions.

When this is happened I try a few things. First, I try using /clear to clear the conversation history from the context. If that fails, I will try using @workspace to provide additional project workspace context. If that fails, I will close all project files and reopen just the ones I am focused on and retry.

There are still occasions where no amount of tweaks result in a good suggestion. When that happens I then seek alternative approaches, typically trying my preferred search engine. I have had a few times where the answer to a specific issue was found only on a single GitHub issue that didn't quite make it to the LLM.

**Try Amazon Q Developer today, and claim your free Builder ID**

That's it for today's tip. Let me know how you get on with this tip, and if you have your own drop me a message or reply. I would love to feature them here.

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
