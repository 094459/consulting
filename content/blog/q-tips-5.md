+++
title = "Amazon Q Developer Tips: No.5 Break down large problems"
date = 2024-12-05
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no5-break-down-large-problems-30ld"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no4-no-aws-account-needed-12lm).

Ok, time for today's tip....

### Tip 5 - Keep things simple: Break down large problems

I **LOVE** using AI coding assistants like Amazon Q Developer, and I find it hard to even think about how coding used to be. That said, AI coding assistants are not perfect, so it is important to know how to get the most out of them when using them. One of the key realisations when you start to use these on a daily basis is to reset your expectation of what they can, and more importantly, cannot do (today).

**Expectations vs Reality**

When I talk to developers about *how* they are using AI coding assistants, I see the same patterns that I have experienced myself. The initial enthusiasm that these tools will be able to generate all the code we need is quickly replaced with a more realistic sense of what they can do and what they cannot to (today).

What I have found over the past year or so is that you can get more consistently good outcomes by doing one thing: breaking down larger and more complex prompts or asks into smaller, more specific tasks. I have been using this approach effectively and I would say this has been a real game changer for me in how I use these tools to get more consistently good output and code suggestions.

How do you break down a problem? There are lots of ways you can practice this, and I certainly am not going to tell you that one way is better than the other. This is something you can try and experiment for yourself. Some of the ways I have found helpful include:

* Imagine having a conversation with someone, how would you describe the goal, and then the tasks you would need to do to achieve that goal?
* Creating a visualisation, like a mind map
* If you have experience with agile/lean practices, breaking down the goal into a minimum viable core product that provides your basic functionality that you can build upon
* Generating a hierarchy of tasks and then linking them so you have a map of your activities you need to complete

**Small and specific - the magic to getting the best of prompts**

One thing you need to ensure when doing this is that you can break down these tasks so that they are small enough to provide something that Amazon Q Developer can deliver, and that you can start thing about how to concisely articulate what you want to create.

* Small - break down larger problems and tackle one specific task, and use details to describe THAT task
* Specific - use clear and concise language - provide specific details that will help Amazon Q provide the right response: version numbers, library names, 

I have found additional benefits to this approach, some of which include:

* Iterate - smaller tasks allow you to better review the output and then provide feedback, course correct, and update as needed
* Explainability - the output generated is easier for me to understand, debug, and make my own
* Lean in - as the code base grows incrementally I feel much more in control, and I do not feel overwhelmed
* Reuse - I can capture and re-use prompts that I know work well for specific code I might need generated (see below for a great resource that helps developers manage this more easily)

**An example**

A recent example of how I broke down a larger activity into smaller more manageable tasks or steps was when I was creating an arcade scroller game for the AWS Gaming Challenge.

Rather than expecting Amazon Q Developer to create my finished game from a very detailed prompt, I took a different approach. I thought about what I wanted to create (an arcade scrolling game that moved a spaceship to avoid debris that was scrolling across the screen). I used Amazon Q Developer Agent for software development to generate the core game engine. After that I broke it down into additional tasks to improve on the created core game.  I revised the gameplay, added an increasing levels of difficulty, a scoring mechanisms, improved collision detection, a leaderboard, and so on.

{{< youtube g-adWK-hsec >}}

You can read more about this in more detail (including the way I broke down the overall challenge into a set of smaller tasks) in my blog post, [How I built an arcade scrolling game in a day with generative AI](https://dev.to/aws/how-i-built-an-arcade-scrolling-game-in-one-day-ek8)

**Getting Amazon Q to help you**

I have found that breaking problems down into smaller tasks that I can then provide prompts for, is something that I am always practicing and improving. One of the things I did early on was to ask Amazon Q Developer how it would break down building your solution. For example, I was putting together a simple demo application and I asked this prompt:

> can you tell me how you would build a gifting wish list application that would allow people to create lists and then share these with people. can you break it down step by step into tasks

It walked me through a series of steps that seemed sensible to me.

![example prompt to break down a problem](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffdfc8ed8aplntbqwfb0b.png)

**Community Resources**

Another great resource you can turn to to help you build this muscle memory has been created by AWS Community Builder Christian Bonzelet. [https://www.promptz.dev/](https://www.promptz.dev/) provides a great way to see how others are creating prompts that address a number of tasks, and I have found it helpful to get insights and ideas on how to improve my own.

> **Further reading** I highly recommend you read [A framework to adopt generative AI assistants for builders](https://it20.info/2024/5/a-framework-to-adopt-generative-ai-assistants-for-builders/) from my colleague Massimo Re Ferrè

**Try Amazon Q Developer today, and claim your free Builder ID**

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
