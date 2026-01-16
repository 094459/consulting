+++
title = "Amazon Q Developer Tips: No.7 Generating better prompts"
date = 2024-12-07
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no7-generating-better-prompts-ag5"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no6-exploring-use-cases-hf2).

Ok, time for today's tip....

### Tip 7 - Guiding Amazon Q : Generating better prompts

As you explore the world of generative AI developer tools, one thing you will need to think about is that in order to get useful output and results, you need to ensure that you provide tools like Amazon Q Developer, the right input. What do I mean?

When using AI coding assistants like Amazon Q Developer, the single most important thing to understand in order to get the best code suggestions and output is:

> **Prompt** + **Context** = **Output**

We have already looked at one side of the prompt, making sure that we are providing simple, concrete tasks that Amazon Q Developer can work with ([Amazon Q Developer Tips: No.5 Break down large problems](https://dev.to/aws/amazon-q-developer-tips-no5-break-down-large-problems-30ld)). Now we need to optimise our approach to the prompt.

**Understanding how to ask Amazon Q Developer questions**

The "Prompt"  is how tools like Amazon Q Developer know what they need to do, in the same way that when you are using a search engine, you enter terms you want to search for. It is tempting to treat the prompt like a search, but in my experience that leads to unpredictable and often poor results. Here are some things to think about that I have found improve the output from tools like Amazon Q Developer. 

* Be specific and concise - provide a detailed and concise prompt of what you want, do not use vague or ambiguous language and provide as many details as you can (version numbers, framework names, etc) as well as what you want it to do for you (write code, create documentation, help you understand, etc)

* Funnel your prompts - if the output is not what you expect, you can use follow up prompts to help steer and improve the output. Using terms like "Can you provide a more detailed response" or "Can you give a code example" are good ways you can maintain the context and memory of what has been asked before, and refine the output

* Provide feedback - if the output from your prompt is good, use the thumbs up and down to provide feedback (only relevant in the Chat interface) as this will help reduce poor suggestions you might get, or provide a good direction of travel indication to future prompts

* Rephrase your prompt -  sometimes the output you get will not be great, so do not panic, this is part of the nature of how these tools work. Sometimes, it is better to reword or re-think your prompt and try again

* Provide examples - providing examples within your prompt can help steer Amazon Q in the direction of what you need. This is especially important when using prompts to help debug errors or issues that come up during your development. Debug errors by copying the important and most pertinent part of the error messages with additional text such as  "How do I resolve this error", or "What does this mean".

* Do not include confidential data or secrets - do not include any information or data within your prompts that you would consider sensitive. Aside from tripping the AI Guardrails within Amazon Q, its most likely that your business has policies around this.

Remember these tools are non deterministic, and it is easy to forget that every time you run the same prompt, you are likely to get different results and output. That is the nature of these tools - it is a feature not a bug!

**Managing your prompts**

It is important to get into "Daily habits" of using Amazon Q that will quickly help you learn what works well, and what does not. When I first started using Amazon Q I only used it occasionally. It was not until I started using it daily that I started to better understand how to formulate my prompts, and Amazon Q start producing much better output for me.

Saving the prompts that work well for you is an important milestone that will help you start to get more consistently good output from Amazon Q. I used to use a markdown doc, but now I am beginning to use a new tool created by an AWS Community Builder, Christian Bonzelet, called [Promptz](https://promptz.dev). You can login and save your own prompts, as well as see what prompts others have created and try these out. Learning from what other developers are prompting is super helpful in accelerating your own expertise.

>> **Further reading** One of my colleagues Denis Traub explored how to use generative AI to improve prompts. It is worth reading, as this technique can be helpful if you are trying to get AI coding assistants to do something and struggling to get anywhere. I have used it for this situation on a number of occasions and it has unlocked me. Go read -> [AI-Powered Prompt Engineering: Create the Perfect Prompt - Every Single Time!](https://community.aws/content/2hVZaVgpovhzdi5ijY12ZKDPGBc/ai-powered-prompt-engineering-create-the-perfect-prompyt-every-single-time)

**When your prompts don't work**

Occasionally you will enter a prompt and receive the following response:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dlpwg15hrg4zg5m9q7ba.png)

It can sometimes be a little random when this happens, so here are a few tips to help you resolve this issue:

* Stay within the same 'conversation' as Amazon Q retains memory and context, and you are less likely to encounter this issue if it is part of a longer conversation
* Change the order of the words - sometimes you might need to revise your prompt, removing potentially confusing words
* Try a different prompt - you can keep the same intention but try using completely different words

In most cases these will resolve your issues.

**Tripping the AI Guardrails**

In this last section we take a look at something that you are probably going to encounter as you use Amazon Q Developer - the 

Occasionally as you use and interact with Amazon Q Developer in any of the different modalities (chat, /dev, @workspace, or in-line), the output may come to an stop and you will be greeted a message.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/eefjnq0g4xaoqd8mtk1j.png)

The message might take other forms, for example with an error popup appearing in the bottom right of VSCode.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6b8030a75zq7ik9a3ej7.png)

If you do these are examples of your prompts bumping against the Amazon Q Developer AI Guardrails.

If you do encounter these, then try:

* Adjust the prompt - use different words, or change the order as sometimes certain words can trigger the guardrail
* Test against different files in your repo - sometimes it can be just one file that trips the guardrails, so you can narrow down where Amazon Q is tripping up (a recent example this happened to me was due to a file containing an open source licence text which seemed to trigger the guardrail)
* Review your logs -  the Amazon Q Logs to see if you can find any information that might help you identify the root issue

The guardrails provide important protection for users of Amazon Q, and the tension between what will work and what trips them is changing all the time.

> **AWS Responsible AI Policy** You can review the AWS Responsible AI Policy [here](https://aws.amazon.com/machine-learning/responsible-ai/policy/)

**Prompts and Context**

Hopefully this has provided you with some ideas and thoughts on how to approach writing better prompts. Remember, there is no substitute for experimentation and use, so start getting into the practice of using these tools and forming your daily habits. Prompts alone though are not enough, and in tomorrow's tip we will look at how to pair your perfect prompt with the additional information it needs (context).

**Try Amazon Q Developer today, and claim your free Builder ID**

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
