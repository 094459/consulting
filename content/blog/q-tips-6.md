+++
title = "Amazon Q Developer Tips: No.6 Exploring Use Cases"
date = 2024-12-06
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no6-exploring-use-cases-hf2"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no5-break-down-large-problems-30ld).

Ok, time for today's tip....

### Tip 6 - Keep things simple: Exploring Use cases

When I speak to developers across the world, the one thing that always amazes me is how different we all approach our craft. Whilst there are commonalties in the tools we use, the methodologies and frameworks we champion, or the approach we take to writing code, I am constantly learning and picking up new ways of working, new tools, or new hacks that I can try out.

When it comes to the use of AI coding assistants, the same is true. One of the reasons I put together a talk (and now this series of blog posts) is to share some of the things I have found have helped me work more effectively with tools like Amazon Q Developer. Today's tip is around how and where you can use AI coding assistants - spoiler alert, it is not just coding!

**The software development life cycle**

As developers we spend our time across a number of different activities in order to ship code. I want to share some of the ways I am seeing developers use Amazon Q Developer across those different activities

* Analysis - At the beginning of any project, developers are often engaged in the project kick off to work with stakeholders to understand what problems are trying to be solved and what needs to be built. Developers can use generative AI tools to help them prepare for the analysis phase of development projects. We can use Amazon Q Developer to better prepare for planning meetings, and help us ask better questions. For example, Amazon Q Developer can help us better understand functional and non functional requirements that we might need to think about, or perhaps use these tools to explore different approaches and provide some initial ideas for the design stage – pros/cons. How many times have you used the phrase **IT depends** when speaking with your stakeholders during requirements gathering? You can use Amazon Q Developer to help you quickly get answers to these kinds of questions, helping you reduce the time it takes to get those decisions agreed 

* Design - During the design phase, you need to start thinking more concretely about what you are going to the architecture and how the solution is going to look. You need to find accurate, up-to-date information and guidance to help you understand potential solutions, which AWS services you might use, and how  you can use them. You could spend hours reading through AWS documentation, going through blog posts, or searching the web - Amazon Q Developer can really help you gain clarity quickly. As you begin to narrow down your choices based on the inputs you already have (functional and non functional requirements), you can find out the options you have, understand the trade-offs you need to think about, so that you can make the right design decisions. Finally, I have found Amazon Q Developer helpful as you start to define your architecture or selecting the frameworks you might want to use, think about your compute architecture, or understand how to better right size your infrastructure and ask for sizing suggestions.

* Development - as you get into the coding parts, this is where Amazon Q Developer really shines. Aside from actual code generation (using capabilities such as Amazon Q Developer Agent for software development which are invoked using [/dev](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/software-dev.html)), developers tell me that they are finding AI coding assistants like Amazon Q Developer to help improve productivity and get more done. Whether that is because they can reduce context switching by getting everything they need within the IDE (no more having to browse the web to access cheat sheets or reference documentation for example), quickly debug and fix errors that you create as you code, provide guidance on how to use libraries, and more. Beyond being more productive, tools like Amazon Q Developer can help developers improve their code craft, helping them to quickly refactor or optimise the code without having to leave the editor. Finally, as you develop, it has never been easier to quickly add documentation to your code, so there should be no excuses from now on. **HOT OFF THE PRESS** Amazon Q Developer introduced [/review](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/code-reviews.html) during re:Invent, which simplifies reviewing the code you create, looking at security vulnerabilities and code quality issues to improve the posture of your applications throughout the development cycle.

* Testing - whether it is creating unit tests for your code or generating synthetic data so that you can use to test your application, AI coding assistants can help simplify how you test your application. One area that perhaps I have not seen much written about is how you can also use Amazon Q Developer to help generate test cases, working with other testing stakeholders. I have started to experiment more with this, using other supporting technologies such as Amazon Bedrock to provide richer and more detailed test cases based on the application functional and non functional requirements. **HOT OFF THE PRESS** Amazon Q Developer introduced a new feature at re:Invent which is invoked using [/test](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/test-generation.html), that provides an AI-powered unit test generation capability that automates the creation of unit tests.

* Deploying - once you have your application working and passing tests, you are ready for deployment. Amazon Q Developer yet again provides you with more ways to help. Whether that is helping you to create documentation (**HOT OFF THE PRESS**, at re:Invent a new capability was added to Amazon Q Developer called [/doc](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/doc-generation.html) that allows you to simplify this process), generate architectural diagrams, write infrastructure as code (IaC) or deployment scripts, or even actually running those deployment scripts with the Amazon Q Developer command line capability - Amazon Q Developer makes it easier to deploy with confidence.

* Maintaining - a lot of developers I speak with work with code bases that they did not create, typically being asked to update or resolve issues. Understanding that code can be daunting, especially if there is little documentation available. Amazon Q Developer can help developers with maintaining code bases in a number of ways. First, one of the core capabilities in Amazon Q Developers is the "Explain" feature, that allows you to either select some code or even your whole project, and get Amazon Q Developer to provide a summary and explanation of what the code does. If needed, you can drill down into areas that you need more detail about. Another way I am seeing developers use Amazon Q Developer to help is to identify how to resolve issues or errors that the code generates, often being able to provide code changes to address those changes. For code that might not have any documentation, you can use Amazon Q Developer to retrospectively update your project to add documentation within the code as well as creation of user guides or README docs. Finally, Amazon Q Developer Agent for code transformation, [/transform](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/transform-in-IDE.html), takes the heavy lifting from updating Java applications to newer versions of Java. **HOT OFF THE PRESS** This has now extended to .NET and mainframe applications, as well as providing help with modernising VMware workloads.

As you can see, Amazon Q Developer is more than just helpful during the hands on coding aspects of the work we do. I can do way more. But lets look at even more use cases

**Innovation**

Aside from the day to day activities that developers undertake, one of the more interesting areas I have seen AI coding assistants like Amazon Q Developer have an impact is in the area of innovation. Specifically in a few areas:

* Increased experimentation - using Amazon Q Developer has significantly reduced the friction in getting started, allowing me to experiment with new libraries, tools, or approaches where typically I might have added it to my "to do" list. 

* Learning new things - learning about new libraries, tools, and frameworks, is a core part of innovation, and Amazon Q Developer makes it super easy to quickly learn and then try. Recently I wanted to write some code to export data from CloudWatch logs, but I thought I would ask Amazon Q for some suggestions. It provided me with two new ways that I was not familiar with. Thanks to Amazon Q, I was able to try these two new ways in 10-15 mins. Whilst I didn’t end up using them, I now have more knowledge, and can use these in perhaps other use cases where they are a good fit.

* Create working prototypes more quickly - you can use Amazon Q Developer to quickly put together prototypes for your customers. Rather than simple wireframes or simple point and click prototypes that are often produced in the early stages of innovation, you can now put more function prototypes with minimal effort. I have been showing how you can do this as part of my "From zero to shipped in 30 minutes" series of talks, creating all sorts of sample applications (check then out if you want - [voting app](https://github.com/094459/q-developer-voting-app), [weather forecaster](https://github.com/094459/q-developer-weather), [micro blogging app](https://github.com/094459/q-developer-microblog), [a fun quiz](https://github.com/094459/q-developer-quiz) and a [wish list application](https://github.com/094459/q-developer-wishlists))    

Amazon Q Developer is a great tool to help developers innovate and add value to the business.

**Automation**

Another use case I have found tools like Amazon Q Developer invaluable has been in automating the things I do. I am sure that many of you have seen this xKcd diagram.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nsx6uu4q58q6mpskp8yr.png)

The tension between the effort required to automate something, and the work required has now significantly shifted thanks to tools like Amazon Q Developer. Automating a task has become almost a trivial task, as it has never been simpler to quickly put together code to help you automate your manual tasks. 

These small tasks are ideally suited to tools like Amazon Q Developer, and I have found that whether it is creating simple Python scripts, creating bash/shell scripts, or even using Amazon Q Developer command line to simplify those commands I just can never remember all the options and switches for, I am automating and simplifying the tasks I need to get done.

A good example of this recently was when I was working with a colleague on a simple demo they needed to put together. There was a lot of data, but it was in the wrong format. It was around 400-500 images and meta data which I could have updated by hand. I started up VSCode, opened up the Amazon Q Developer chat and within around five minutes had created two Python scripts to massage the data into the format I needed.

> **Further reading** I have written about this several times this year, and you can dive deeper by reading "[Writing simple Python scripts faster with Amazon Q](https://community.aws/content/2aop9BhphR0eA8Y95CEuvrRXogq/writing-simple-python-scripts-faster-with-amazon-q)" where I show how I was able to do a quick automation typical of how Amazon Q Developer is lowering the barrier to automation, and "[How I used Amazon Q Developer to move faster with data](https://community.aws/content/2jK26brVpXufp1eH7rN5mjkfydk/how-i-used-amazon-q-developer-to-move-faster-with-data)" where I refine the automation further.

Amazon Q Developer helps you automate and scale as a developer - there really is no excuse now for lack of automation.

**Open Sourcing your code**

Another use case that I have written about ([Using Amazon Q Developer to help me open source my code](https://community.aws/content/2fnnbbW7axhnDiiWhcfjDmvVgkj?lang=en)) is providing some practical help when it comes to applying changes to your project if you want to make it open source.

> **Remember!** You should always consult your stakeholders when doing this and engage the appropriate legal guidance beforehand


**What use cases will you use Amazon Q Developer for?**

In this quick post I have shared some of the use cases where you can use AI coding tools like Amazon Q Developer, and I hope this will help inspire some of you to apply the same approach. Let me know if you come up with some really cool automation, or some experimentation or MVP you created, using Amazon Q Developer.

**Try Amazon Q Developer today, and claim your free Builder ID**

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
