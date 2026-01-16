+++
title = "Amazon Q Developer Tips: No.9 Using import statements to direct suggestions"
date = 2024-12-09
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no9-using-import-statements-to-direct-suggestions-2mfb"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no8-understanding-context-2305).

Ok, time for today's tip....

### Tip 9 - Guiding Amazon Q : Using import statements to direct suggestions

In the previous Amazon Q Developer tip I shared some of the ways that the Amazon Q Developer AI coding assistant uses context as consideration when generating its output and coding suggestions.

One of the ways that Amazon Q Developer understands context is by reviewing the current open file's import statements. If you are starting a new file, you can influence and guide Amazon Q Developer by ensuring that you add any relevant library imports before you prompt.

Check out this short video that shows this in action. When I provide an initial prompt to Amazon Q Developer with no additional context (just the prompt) I get one result. When I add a single line to add library imports into a new file and try again, you can see that Amazon Q Developer has picked this up and provides me with a completely different code suggestions.

{{< youtube V3bDeDgLiWM >}}

That's it for today's tip. Let me know how you get on with this tip, and if you have your own drop me a message or reply. I would love to feature them here.

**Try Amazon Q Developer today, and claim your free Builder ID**

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
