+++
title = "Amazon Q Developer Tips: No.15 CHat Orientated Programming (CHOP)"
date = 2024-12-15
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no15-chat-orientated-programming-chop-4ekg"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no14-navigating-through-your-prompt-history-3mel).

Ok, time for today's tip....

### Tip 15 - Guiding Amazon Q : CHat Orientated Programming (CHOP)

CHat Orientated Programming or CHOP is the abbreviation that describes the emerging method of using AI coding tools together with context and prompts to generate code. 

Developers who are new to AI coding assistants sometimes struggle with the nature of CHOP, treating the chat interface as a proxy for search. Whilst this might yield good results occasionally, my own testing and experience found that this limits the potential of these tools. I get much better code suggestions (relevancy, quality, for example) when I treat this as a conversation. What does this mean?

* Treat this as a funnel - when using the chat interface, it is important to start with an initial prompt and then funnel follow on prompts to help direct and narrow down what you are looking for.
*  Conversation history - as you work back and forth in the Amazon Q chat interface, under the covers Amazon Q is retaining a history of the conversation and retains context. Whilst it may be tempting to close the chat tab, or open new ones, maintaining this context can be key to getting better responses. You can clear the conversation history by using the /clear command. Use this if you feel that the conversation has run its course, or has become circular.


**Available Amazon Q Developer tools**

The chat interface also exposes a number of tools (channels, interfaces) that allow you to invoke additional capabilities within the context of your conversation. It is important to understand what tools are available and how these work, in order to apply the best tool for the task you are trying to carry out (more about that in tomorrow's tip). 

From the Amazon Q Developer chat interface, you can access the available tools by using the / key. In addition, you can access Amazon Q Developer commands by accessing the @ sign (currently only @workspace exists).

> Massimo Re Ferre has put together the ultimate Amazon Q Developer cheat sheet which you can access [here](https://it20.info/misc/html-pages/amazon-q-ide-table.html). It provides a useful overview of all the Amazon Q Developer tools together with information such as context availability, supported languages, links to documentation and more. 

**CHOP considerations**

When using the Chat interface, there are some things you should be aware of to help improve your success when working with it.

*Max size*

You can enter a maximum of 4000 characters into the chat interface. Bear this in mind if you are using the integration with the VSCode menu to send highlighted code to the Amazon Q chat interface (Amazon Q > Send to Prompt). If you are working on a particularly large file, you might exceed your limit and have no space for a prompt. You will notice that there is a counter underneath the chat interface to help you know how close you are getting to your limit.

*Chat interface Tabs*

You can have a maximum of ten chat windows currently.

*Provide feedback*

Use the thumbs up / thumbs down to provide feedback within the conversation and to help steer future code suggestions and output.

*Copy and Pasting code*

When Amazon Q produces code in the chat interface, you will notice that there are two icons at the bottom of any code block which allow you to COPY the code into the clipboard, or INSERT INTO CURSOR, which will try and PASTE the code where your cursor is. The caveat here is that the cursor needs to be within a file in the IDE - it will not send that into the Terminal within VSCode or anywhere else.

Using these two buttons provides a simple and quick way of getting code from the chat interface and into your code.

*View and Apply Diff*

When using the Amazon Q Developer in-menu integration (right click and then selecting Amazon Q from the menu) the output will be sent to the Amazon Q Developer chat interface. In recent updates to the Amazon Q plugin, they have changed what this output looks like, and you will notice that VIEW DIFF and APPLY DIFF replace the "Insert into cursor" and "Copy" buttons. These work in the same way that using the in-line prompting works, and allow you to directly view the code differences between what you have and what the Amazon Q chat output is suggesting. You can then use the APPLY DIFF to automatically update the content.

You can see this in the following short video

{{< youtube zgs5_1NCEQw >}}

**Trust but verify**

AI Coding assistants do an amazing job in producing coding suggestions that you can use, but they do not always get it right. In fact, regardless of how good the suggestions are, you should always **trust but verify** the output. To help me I have a couple of things I do to make this manageable.

*Work in smaller chunks of code*

The first is to try and limit the amount of code that I *need to understand* that Amazon Q Developer produces. This helps from an explainability perspective, but also makes debugging much easier.

*Review checklist*

I have started to use a mental model and workflow when reviewing the code suggestions that kind of looks like this:

1. Review the output of the code - does it seem to fit what I asked it to do
2. Check the logic - review the logic of the code to see if it makes sense
3. Good practices - ensure that the code is adopting good coding practices, and not implementing any anti-patterns - this can be subjective sometimes, so you need to use what you are comfortable with
4. Error handling - look to make sure the code has error handling,
5. Four eyes - I use the Explain feature within Amazon Q as a kind of additional check to see what it thinks about the code

Over time I have gotten better at following this mental model, and can review code suggestions much more quickly than when I first started.

**Managing your prompts**

I have already featured this resource in previous tips bit its worth repeating in case you missed it. As your use of Amazon Q Developer increases and you become more familiar with CHOP, phrases and prompts that work for you will become second nature. How you manage these along your journey is key, and AWS Community Builder Christian Bonzelet has put together [https://promptz.dev](https://www.promptz.dev/) to both help you record and save prompts that you find helpful, but ALSO learn from others who have shared/saved their prompts too.


**Try Amazon Q Developer today, and claim your free Builder ID**

That's it for today's tip. Let me know how you get on with this tip, and if you have your own drop me a message or reply. I would love to feature them here.

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
