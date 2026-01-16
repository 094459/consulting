+++
title = "Amazon Q Developer Tips: No.10 Personalise Amazon Qs output"
date = 2024-12-10
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no10-personalise-amazon-qs-output-243p"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no9-using-import-statements-to-direct-suggestions-2mfb).

Ok, time for today's tip....

### Tip 10 - Guiding Amazon Q : Personalise Amazon Q's output

In the previous Amazon Q Developer tip I walked you through setting up Amazon Q Developer Workspace Index, a powerful feature than enables Amazon Q Developer to index all the files in your IDE workspace, and then use that to provide useful context when using the @workspace command.

Today's tip uses  this capability.

When I am interacting with Amazon Q Developer via the chat interface, I often have to repeat or add the following to prompts to influence the output:

* Provide no explaination
* Generate all code suggestions for the Flask framework
* Use only open source libraries and projects 

These have become second nature, but it would be great to simplify this. After reading Massimo's blog post ([DIY personalization for Amazon Q Developer](https://it20.info/2024/10/diy-personalization-for-amazon-q-developer/)) I tried this out for myself and found that this is a really great tip for providing consistent or "personalised" output. 

To do this I create a folder in my local workspace - I always call this ".qdeveloper" but it does not matter what you call this. Within this folder I create a series of markdown files that I want to use to personalise the output. For example, I might want to create personalisations for database code suggestions, so I would create a file called DBA.md and in this file add the following:

```
DBA

Only when I explicitly ask for code, follow this guidance:

- Only provide SQL code unless I explicitly ask for another language
- I am an expert in SQL and I did not need a walk through
- I have a strong preference for Sqlite and PostgreSQL
```

After saving the file, I can now invoke this personalisation by using "@workspace DBA" followed by the rest of the prompt.

Check out this short video of this in action.

{{< youtube 6X9pjMPuIxQ >}}

You can see some additional examples of how I use this [here](https://github.com/094459/porto-techhub-amazon-q-workshop/tree/main/.qdeveloper). Here is an example of me personalising the output for a Java developer.
 
![example of workspace enabling personalisation for java developer](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ff9q6ntnqf63m2g2s3hvz.png)

That's it for today's tip. Let me know how you get on with this tip, and if you have your own drop me a message or reply. I would love to feature them here.

**Try Amazon Q Developer today, and claim your free Builder ID**

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---

Made with ♥ from DevRel
