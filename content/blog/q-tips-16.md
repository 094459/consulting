+++
title = "Amazon Q Developer Tips: No.16 How to tackle LLM training data cutoff"
date = 2024-12-16
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no16-how-to-tackle-llm-training-data-cutoff-497b"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no15-chat-orientated-programming-chop-4ekg).

Ok, time for today's tip....

### Tip 16 - Guiding Amazon Q : How to tackle LLM training data cutoff

AI coding assistants like Amazon Q Developer utilise large language models (LLMs) behind the scenes. These LLMs are training over weeks and months using vast amounts of training data. But what happens if you want to use coding libraries or technologies that came out after the period of that training?

If you struggle to get decent code suggestions when using newer libraries or technologies, then this might be an issue you run against. In today's tip I am going to share a few approaches you can take to tackle this.

**Amazon Q Developer customisation**

Amazon Q Developer provide the capability of using your own custom model using code that you supply (either in an S3 bucket or one of the supported source code repository technologies). This is only available for the Professional Tier however, you will not be able to set this up or use it when using your Builder ID.

The way it works is straight forward. You provide some source code, train a model, and then activate that model so it can be used within the Amazon Q Developer plugin. This allows you to break out of the limitations of the training data used when the LLM was being created. It is especially useful in situations where you might want to use your own code examples and standards, use updated versions of libraries or code, or perhaps use your organisations proprietary algorithmic techniques.

There are a few things you need to think about:

* Currently you can only create a customisation job with source code that is of the following: Java (.java), JavaScript (.js, .jsx), Python (.py) and TypeScript (.ts, .tsx)
* When I first started experimenting creating my own customised models, they would often generate poor evaluations or even fail. It took me some time to get my source code and examples into good shape before they would work - make sure the source code you are using is of a sufficiently good quality!
* Your data source must contain at least 2 MB, and at most 20 GB, and any single file cannot exceed 10Mb. There are no limits on the number of total files however.
* File names and individual directory names must not exceed 255 characters
* You can create a maximum of eight customisations per AWS Account, with two active at any time

The process flow is intuitive when generating your customisations, and you can assign your custom models to a subset of your developers which you might want to do based on need or perhaps you might want to test the difference between your developer groups.

Once the customisation has been completed and activated, you will now see this appear as an option in the Amazon Q Developer IDE settings. You can see what this looks like here with a customisation model I created a few months ago.

![Amazon Q Developer custom model for airflow](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4rrd7x2dc2d87i3jucle.png)

Check out this video that my colleague Ricardo Ferreira put together that walks you through the end to end process of doing this.

{{< youtube dsjXb4TvfPg >}}

**Amazon Q Developer Workspace Index**

Amazon Q Developer customisation requires developers to login using the Professional Tier, so what do you do if you are using BuilderID? The good news is that you do have options, and you can use Amazon Q Developer Workspace Index to provide similar results.

I spend some time writing code for Apache Airflow, a project that is evolving quickly with new releases being updated on a monthly basis almost. I was not getting the latest good practices when using AI coding assistants on how to write Python code, and so I looked to improve this. 

I created a local directory, downloaded and git cloned the latest "golden" examples and source code from the supporting repo, and then made sure that Amazon Q Developer workspace index had been enabled. What I found is that this provided me with different code suggestions, often improving on the original.

It is not perfect, and it tends to work better for some use cases than others so I do recommend experimenting and see how you get on. I have written about this a few times. In [Updating legacy Apache Airflow DAGs with Amazon Q Developer](https://community.aws/content/2jHORYpPR2EJ1fhVHnavFMK2X4I?lang=en) I show how I used a local clone of the Apache Airflow latest provider package to provide improved code suggestions. In [Using Amazon Q Developer to update Valkey client code](https://community.aws/content/2jSN5k83A5Wayog5Rkin4TmbLhg?lang=en) I shared how I updated some Valkey client code to use a newer approach to connecting to Valkey, using the GLIDE client. These provide details of how I approached this, including what preparation I took.


So if you find yourself in a situation where code suggestions are not what you need, consider the two approaches outlined in the post to see if they help address your issue and improve the output Amazon Q Developer generates.

**Try Amazon Q Developer today, and claim your free Builder ID**

That's it for today's tip. Let me know how you get on with this tip, and if you have your own drop me a message or reply. I would love to feature them here.

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
