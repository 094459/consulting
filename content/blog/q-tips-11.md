+++
title = "Amazon Q Developer Tips: No.11 Scaffolding"
date = 2024-12-11
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no11-scaffolding-5c6m"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no10-personalise-amazon-qs-output-243p).

Ok, time for today's tip....

### Tip 11 - Guiding Amazon Q : Scaffolding your project

In the previous Amazon Q Developer tip I walked you through setting up Amazon Q Developer Workspace Index, a powerful feature than enables Amazon Q Developer to index all the files in your IDE workspace, and then use that to provide useful context when using the @workspace command. In yesterday's tip I showed you how you can use this to personalise your output.

Today's tip uses  this capability in a different way - providing a way to more consistently guide the code suggestions Amazon Q provides by using an example project layout or "scaffold". When you are working with certain technologies, or over time standardised the layout and structure of your projects, you want to get coding suggestions that align to those. The good news is that you can.

I create a folder in my project called "project" and within this I create a markdown file called "project-standards.md" and then I add details of how I want Amazon Q Developer to formulate any output and code suggestions. This is an example of one I used for bootstrapping simple Flask applications:

```
When creating new Python code, use the following guidance

Generate code using the following structure and layout
├── static/
├── models/
├── routes/
├── templates/
├── healthcheck/
├── tests/
    ├ conftest.py
├── Docker/
    ├ Dockerfile

```

You can [see an example here](https://github.com/094459/porto-techhub-amazon-q-workshop/blob/main/project/PROJECT-STD.md).

Once I save this file, and I can now use this from within the Amazon Q Developer chat interface with @workspace, or use it as part of the Amazon Q Developer Agents feature. You should see that what you define within this document is picked up and your code suggestions.

Check out this short video of this in action.

{{< youtube a536N7vCito >}}

> For the eagle eyed you will notice that in this video I called the file STD.md rather than project-standards.md - I am always experimenting and have found that creating markdown files with a more appropriate name has generated better and more consistent output

**What else can you add?**

In the example above I only added information about the layout of the project. You can add much more information an detail, and I encourage you to experiment. Some of the things that have worked well for me include:

* Adding sections around project requirements, both functional and non functional
* Being specific around libraries and frameworks you want to use
* Provide directions of what you want produced

I have found that these tend to work best when using /dev so your results and success may vary.


**Try Amazon Q Developer today, and claim your free Builder ID**

That's it for today's tip. Let me know how you get on with this tip, and if you have your own drop me a message or reply. I would love to feature them here.

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
