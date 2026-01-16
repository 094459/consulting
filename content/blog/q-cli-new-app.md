+++
title = "Using Amazon Q Developer CLI to build applications from the command line"
date = 2025-03-09
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/using-amazon-q-developer-cli-to-build-applications-from-the-command-line-27mg"
+++

I have been writing a lot recently about AI Coding Assistants, and I have been mostly using Amazon Q Developer within VSCode. This week though, saw a very nice update to the Amazon Q Developer CLI, a separate download that provides you with Amazon Q within your command line. It is available for MacOS and various flavours of Linux (you can  download it from [here](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el).

I wanted to see how good the recent update is, so I decided to try and build a quick web application from the command line. I created a new directory on my mac, and then I added two files:

* [fact-checker.yaml](https://gist.github.com/094459/33cc291e0657d0b25812df7057978f88) - a data model for a simple fact checking application
* [spec.md](https://gist.github.com/094459/bf583505f11c2e1a1932f1db6f5e0610) - a scaffold document that outlines how I like to structure my projects

When I look at the structure of my directory, it looks like this:

```
├── data-model
│   └── fact-checker.yaml
└── spec
    └── SPEC.md
```

From the command line, I now type:

```
q chat
```

And I enter the following prompt:

```
> Build a simple fact checking app
```

You can see what happens in this short video - I sped up some parts (x2) to make the video shorter.

{{< youtube cfPMfcCfgwg >}}

It took around 12 minutes to complete, and I was super impressed. After it generated the code you can see I ask it to create a virtual Python environment, install the dependencies, and then run the application. After an initial error, Amazon Q Developer CLI figures out what it needs to do and I have my app up and running.

For the eagle eyed out there, you will notice that when I create a new fact, there is an issue with the formatting of the buttons. So I decided to go back and get Amazon Q Developer CLI to see if it could fix it.

In less than five minutes I had a much improved UI.

{{< youtube q-9_-BcyBsg >}}

Whilst I will still be using Amazon Q Developer in the IDE, this improved capability within the command line is going to be exciting to explore. Watch this space for more blog posts coming.

**Try Amazon Q Developer today, and claim your free Builder ID**

You can try Amazon Q Developer CLI for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el) and then downloading the app from [here](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el).
