+++
title = "Amazon Q Developer Tips: No.17 Choose the right tool"
date = 2024-12-17
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no17-choose-the-right-tool-7a2"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no16-how-to-tackle-llm-training-data-cutoff-497b).

Ok, time for today's tip....

### Tip 17 - Amazon Q : Choose the right tool

Amazon Q Developer provides developers with a number of tools and commands to help generate code suggestions and other guidance. In previous tips I have shared how some of these work, and provided hopefully helpful tips that will make you more effective working with these. But how do you know which tool or command to use? Today's tip is about providing you with a mental model on how to approach that.

The mental model that I use to help me assess which is the right tool or command to use is focused on five key things:

* What context do I need
* Developer experience
* Amount of effort needed
* Service limits and quota
* Boost vs Learn

**What context do I need**

Different Amazon Q Developer tools use and provide different context. For example, in-line will only use the current file you are editing (or block of code highlighted). This might be enough for the task I am carrying out. If I need more context (maybe I need to reference or understand supporting files in the project) other tools might give me better code suggestions and output, and I am more likely to use something like @workspace or Amazon Q Developer Agent for feature development (/dev).

**Developer experience**

The latency and responsiveness of the tools is different, and so has a direct impact on the developer experience. If I am in the flow and creating or editing files, the additional keystrokes and mouse movements are going to slow me down. Being able to invoke a prompt via the in-line prompt is going to be faster than using the chat interface. 

**Amount of effort needed**

If I need to make changes to a single file (perhaps the one I am in right now) versus having to make changes across multiple (maybe even all) files in the project will be a consideration. If I have a large projects with hundreds of files, then the effort saved using Amazon Q Developer Agents (/dev, /doc, /test, or /review) is something worth considering.

**Service quota**

The different tools within Amazon Q Developer have different service quotas, whether I am using the Free Tier or the Professional tier. I factor this in when I am using the different tools as I want to make sure that I do not unnecessarily use up those service quotas for stuff that might be achieved just as easily using another tool with a higher service quota.

**Boost vs Learn**

If I know what I want to do, but just need to be more productive and more efficient (boost) then I might use the in-line tools. If I am exploring or learning, then the chat interface might be my preference (learn). I have found that my use of tools frequently falls along these lines.

> If you want to know more about Boost and Learn as a mental mode, then I recommend reading [A framework to adopt generative AI assistants for builders](https://it20.info/2024/5/a-framework-to-adopt-generative-ai-assistants-for-builders/)


This might not be the best way to think about this, and there are probably lots of other approaches - but this is what works for me. Let me know what you think, or if you have your own mental model that you are using.

**Complexity vs Context**

I was going through re:Invent 2024 sessions over the last week, and another great way to look at which is the right Amazon Q Developer tool to use is thinking about this as complexity of the task you are doing against the amount of context you have or need. AWS Hero Matt Lewis put this very nice graph together.

<add Matts diagram>

I highly recommend diving deeper into this by checking out AWS Hero Matt Lewis' video from re:Invent

{{< youtube 25bzJ-4RWH8 >}}


**Try Amazon Q Developer today, and claim your free Builder ID**

That's it for today's tip. Let me know how you get on with this tip, and if you have your own drop me a message or reply. I would love to feature them here.

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
