+++
title = "Amazon Q Developer Tips: No.13 Generating perfect functions"
date = 2024-12-13
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no13-generating-perfect-functions-h1i"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no12-mastering-in-line-prompts-247k).

Ok, time for today's tip....

### Tip 13 - Guiding Amazon Q : Generating perfect functions

In the previous tip I shared the different ways and techniques for generating code from function names, comments, and prompts. Once you have created code within the file you are editing, Amazon Q Developer retains this in context. You can use this to help simplify future code blocks and functions you can create.

As you create your first block of code or function, take time to make sure this is defined in as much detail as you need. Add documentation to your function (using the in-line prompt to quickly add documentation as per the previous tip), ensure you have the appropriate level of error handling, and any other things you need to add. Once you are happy with the FIRST code block or function, you are done.

When you now go to create further code blocks and functions, Amazon Q Developer will use this first code as a template, carrying on over the same level of detail as you added - documentation, error handling, etc. This will save you a LOT of time and typing, as well as provide better and more consistency in your code. I call this creating "perfect functions" - not in that they are coded perfectly, but in that they provide a blueprint for you to autogenerate more code within the file you are editing.

Check out this short video of this in action.

{{< youtube MIC7ya2NJfg >}}


**Try Amazon Q Developer today, and claim your free Builder ID**

That's it for today's tip. Let me know how you get on with this tip, and if you have your own drop me a message or reply. I would love to feature them here.

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
