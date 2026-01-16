+++
title = "Amazon Q Developer Tips: No.3 Enable Amazon Q Developer Workspace Index "
date = 2024-12-03
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/094459/amazon-q-developer-tips-no3-enable-amazon-q-developer-workspace-index-1jkb"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no2-ide-layout-52a1).

Ok, time for today's tip....

### Tip 3 - Setting yourself up for success: Enable Amazon Q Developer Workspace Index

When using AI Coding assistants like Amazon Q Developer, the most important factor to get the best output is to make sure you provide the right and most relevant context. Context refers to the supporting information provided to the underlying  foundation model which could be things  like the current open file in your IDE, or something you actually write in the prompt itself. Context helps the AI Coding assistant understand the specific situation and generate more accurate and relevant code suggestions, tailored to (hopefully) your need.

Software projects are a collection of files, and provide useful context for such code suggestions. If I want to update or create a new route in a Flask application for example, I might need to refer to multiple files. If I want Amazon Q Developer to help me put together some documentation, it is going to need to know what is going on across the entire project.

Amazon Q Developer Workspace Index allows you to index your local project, which can be used in the Amazon Q Developer Chat interface to provide that additional context by using the @workspace command. This is a very powerful capability, and one that I frequently use. 

**How to enable Amazon Q Developer Workspace Index**

It is very straight forward to enable this feature. From the Amazon Q Developer plugin settings, there are several settings related to this. The first is to enable it - it is DISABLED by default. The other options allow you to tune the indexing process based on your needs. I have found that the defaults are typically good enough. 

> If are have a Windows or Linux machine with a GPU, you can enable GPU support for the indexing process which will help improve performance. I have not tried this out though, but working on getting a GPU based Linux machine soon!
> 

Here is a quick video of me showing you how to do this.

{{< youtube 7Dbx_MBH8ww >}}


**Exploring Amazon Q Developer Workspace Index**

Indexes are created in your local ".aws/amazonq/cache" directory. You will see many subdirectories appear over time, based on your different VSCode projects that you work on.

After ENABLING the Workspace Indexing feature, you can see what is going on by checking out the logs. To access these, from the OUTPUT tab you will see the "Amazon Q Language Server". This is what mine looks like for a simple project:

```
[Info  - 09:33:40] LSP server starts
[Info  - 09:33:40] Loaded model from /Users/ricsue/.vscode/extensions/amazonwebservices.amazon-q-vscode-1.38.0/resources/qserver
[Warn  - 09:33:40] Unknown tokenizer class "CodeSageTokenizer", attempting to construct from base class.
[Info  - 09:33:40] Using number of intra-op threads: 2
[Info  - 09:33:40] Embedding provider initialized.
[Info  - 09:33:40] start building bm25 index
[Info  - 09:33:40] start bm25 index for 23 files
[Info  - 09:33:40] successfully initiaize BM25: corpusSize=15 numberOfFile=7 tokenCount=1204
[Info  - 09:33:40] successfully initiaize BM25: corpusSize=1 numberOfFile=1 tokenCount=0
[Info  - 09:33:40] bm25 indexing complete, time: 22.99ms
[Info  - 09:33:40] start building tree index for /Users/ricsue/Projects/amazon-q/q-tips
[Info  - 09:33:41] Finished parsing 7 python files. Time 31.12ms
[Info  - 09:33:41] Finished parsing 1 javascript files. Time 12.16ms
[Info  - 09:33:41] start building vector index
[Info  - 09:33:41] Starting building vector index for 23 files
[Info  - 09:33:41] Vector indexing done for 2/23 files
[Info  - 09:33:41] Vector indexing done for 4/23 files
[Info  - 09:33:41] Vector indexing done for 6/23 files
[Info  - 09:33:41] Vector indexing done for 8/23 files
[Info  - 09:33:42] Vector indexing done for 10/23 files
[Info  - 09:33:42] Vector indexing done for 12/23 files
[Info  - 09:33:42] Vector indexing done for 14/23 files
[Info  - 09:33:42] Vector indexing done for 16/23 files
[Info  - 09:33:42] Vector indexing done for 18/23 files
[Info  - 09:33:43] Vector indexing done for 20/23 files
[Info  - 09:33:43] Vector indexing done for 22/23 files
[Info  - 09:33:43] Vector index complete! Take 2.2731550830000002s. Total 23 files, 34 chunks
[Info  - 09:33:43] Vector index saved to /Users/ricsue/.aws/amazonq/cache/cache/acab9dd0a6030f048302493496c31034adf8c6a90c34d720acccfa013b8d2000-0.9-VSCode.index
```

When I start adding new files, you will see these being added to the index

```
[Info  - 09:34:25] Adding file to vector index: /Users/ricsue/Projects/amazon-q/q-tips/flask/app.py
[Info  - 09:34:27] Adding file to vector index: /Users/ricsue/Projects/amazon-q/q-tips/flask/app.py
[Info  - 09:34:31] repomap query time: 0.58ms
```

You will also see useful info in the Amazon Q Logs as and when you invoke @workspace. You can use this to see and compare how your prompts are generating useful context that helps your code suggestions and output.

**Using @workspace**

Once you have it enabled and the indexes built, you can now start using it within the Amazon Q Developer Chat interface by using the "@workspace" command. You can place this at the beginning, in the middle, or at the end of the prompt in the chat interface.

It is as simple as that!

If you want to dive deeper, check out Will Matos' blog, [AWS announces workspace context awareness for Amazon Q Developer chat](https://aws.amazon.com/blogs/devops/aws-announces-workspace-context-awareness-for-amazon-q-developer-chat/).


**Things to know**

There are a few things you should be aware of when using this.

1. Files vs Search - You can use @workspace to ask about specific files in your workspace (for example, "@workspace update current data model based on data\model.sql") but its understanding of what a "file reference" (e.g data\model.sql) is based on the concept of a search result from the local index, rather than a directory listing or file handle.  

2. What files are indexed - Non-essential files like binaries and those specified in .gitignore are intelligently filtered out during the index process, and you will notice this as you add files to your project - not every file will appear. The initial indexing process takes approximately 5–20 minutes for workspace sizes up to 200 MB, but I have found that as I typically enable this within my IDE for new projects, the index build is negligible.

3. Continuously updated indexes -  The created index is persisted to disk, allowing fast loading on subsequent openings of the same workspace. If the index is over 24 hours old, it is automatically refreshed by re-indexing all files. To prevent resource overhead, indexing stops at either a hard limit on size or when available system memory reaches a minimum threshold. After initial indexing, the index is incrementally updated whenever you finish editing files in the IDE by closing the file or moving to another tab.

4. Recreating your project indices - Occasionally you might see error when trying to use @workspace. It might error when referring to a specific file that exists for example, or it might report a Fais indexing issue. If this happens you can try restarting the index process (go into the plugin settings and disable/re-enable) and then try again (don't worry if you see additional Amazon Q Langauge Server logs appear).  If you still get issues, you can try recreating the index. You can find the location of the index of the project you are currently in by looking at the Amazon Q Language Server logs. Here is an extract from mine:

```
[Info  - 16:02:49] bm25 indexing complete, time: 0.92ms
[Info  - 16:02:49] start building tree index for /Users/ricsue/Projects/amazon-q/workshop/q-developer-workshop-supporting-repo/q-developer-workshop-demo-code
[Info  - 16:02:49] Finished parsing 1 python files. Time 15.07ms
[Info  - 16:02:49] start building vector index
[Info  - 16:02:49] Starting building vector index for 3 files
[Info  - 16:02:50] Vector index complete! Take 0.09364341600000001s. Total 3 files, 5 chunks
[Info  - 16:02:50] Vector index saved to /Users/ricsue/.aws/amazonq/cache/cache/eee4a16ba650a3c2a0cab92dd904c065feb5976341f32c94cd0be7fe5fcdd94a-0.9-VSCode.index
[Info  - 16:41:47] Adding file to vector index: /Users/ricsue/Projects/amazon-q/workshop/q-developer-workshop-supporting-repo/q-developer-workshop-demo-code/.qdeveloper/MY-PREFERENCES.md
From this we can see that /Users/ricsue/.aws/amazonq/cache/ is the location where the Workspace Index will generate these indexes. These can be deleted as the index process will recreate them.To do this:
```

In this case, this project's index is "cache/eee4a16ba650a3c2a0cab92dd904c065feb5976341f32c94cd0be7fe5fcdd94a-0.9-VSCode.index". Exit from VSCode and then from a terminal, locate the directory where this index is and delete it - don't worry, it will be recreated when you restart VSCode.

**Use Amazon Q Developer Workspace Index today!**

Amazon Q Developer Workspace Index is a powerful feature and capability that you will find yourself using on a regular basis. You will see some of the cool things this unlocks in future tips, so watch out for those!

That's it for this tip, but keep posted for a new tip that I will publish tomorrow. Until then, happy coding with Amazon Q!

**Try Amazon Q Developer today, and claim your free Builder ID**

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
