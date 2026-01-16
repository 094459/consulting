+++
title = "Manage context rot by exploring new experimental features in Amazon Q CLI"
date = 2025-07-02
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/manage-context-rot-by-exploring-new-experimental-features-in-amazon-q-cli-10ki"
+++

Like many folk who have been spending their time with AI Coding Assistants like Amazon Q Developer and Amazon Q CLI, understanding how to manage context is one of the key things you need to develop intuition for to improve the outputs these tools give you. More recently I have started hearing about new terms such as **"[context rot](https://simonwillison.net/2025/Jun/18/context-rot/)"**, and others exploring the field of **[context engineering](https://www.philschmid.de/context-engineering)**. Understanding how to [manage your context](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html) will be key to your success. 

Imagine yourself working on some new feature or trying to refactor some code using Amazon Q CLI, when all of a sudden you start hitting context window limits. You have setup some nice [rules files](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-context-profiles.html), added important markdown docs to your context, and you are getting amazing results. A quick check of **"/usage"** gets your heart pumping as you notice you are reaching your context window limits.

In this post I am going to show you how you can enable an experimental / beta feature in [Amazon Q CLI](https://github.com/aws/amazon-q-developer-cli-autocomplete) that allows you to provide Amazon Q CLI information it needs, without consuming precious context. Sounds good right? Read on to find out more on how you can enable this, and how you can get up and running to test this for yourself.

**Introducing /knowledge**

If you have been using tools like Amazon Q Developer in the IDE, you will know that you can use a feature called **@workspace** to provide additional information with your prompt. It works by indexing the files in your local workspace. **[/knowledge](https://github.com/aws/amazon-q-developer-cli-autocomplete/pull/101)** is a new beta/experimental feature that you can now test with the [latest update](https://github.com/aws/amazon-q-developer-cli-autocomplete/releases/tag/v1.12.2). This introduces a new tool within Amazon Q CLI, that allows you to create semantic indexes of directories and files, that are used to search and use information without consuming tokens in your context window.  Those indexes are called **"knowledge bases"**.

Lets take a look at how you get access to this so you can experiment yourself. If you have not already done so, we need to enable experimental mode within Amazon Q CLI.

**Enabling experimental features in Amazon Q CLI**

To enable **"/knowledge"** we need to both enable the beta features within Amazon Q CLI as well as enable this particular feature. From the command line, enable beta features using the following commands. Make sure you close any Amazon Q CLI sessions you have open for these settings to take effect.

```
q settings app.beta true
q settings chat.enableKnowledge true
```

To verify, when you run "q settings all" you should see the following line.
```
app.beta = true
chat.enableKnowledge = true
```

How do you know whether this has worked? Open up a new Amazon Q CLI session, and from the **">"** prompt, type **"/knowledge"** and hit return, and you should see the following output.

```
> /knowledge

(Beta) Manage knowledge base for persistent context storage. Requires "q settings chat.enableKnowledge true"

Usage: /knowledge <COMMAND>

Commands:
  show    Display the knowledge base contents
  add     Add a file or directory to knowledge base
  remove  Remove specified knowledge context by path
  update  Update a file or directory in knowledge base
  clear   Remove all knowledge contexts
  status  Show background operation status
  cancel  Cancel a background operation
  help    Print this message or the help of the given subcommand(s)

Options:
  -h, --help  Print help
```

We can use the **"/knowledge show"** command to list any existing knowledge bases that have been created. As we have not created any, we just see the following:

```
> /knowledge show


No knowledge base entries found.
💡 Tip: If indexing is in progress, contexts may not appear until indexing completes.
   Use 'knowledge status' to check active operations.
```

> If you see the following when you run this command, it means that you have not configured this beta feature:
> 
> ```
> Knowledge tool is disabled. Enable it with: q settings chat.enableKnowledge true
> ```
> 
> Exit your Amazon Q CLI session, and from the command line type **"q settings chat.enableKnowledge true"**, and then retry

When you use the **"/tools"** command, you will also notice that you have a new tool (**knowledge**) that is available, and automatically trusted.

```
> /tools

Tool              Permission
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Built-in:
- execute_bash    * trust read-only commands
- fs_read         * trusted
- fs_write        * not trusted
- knowledge       * trusted
- report_issue    * trusted
- use_aws         * trust read-only commands

```

Now that we have it enabled and running, lets take a look at the workflow and how to use it.

**Workflow using /knowledge**

The workflow for working with **"/knowledge"** is pretty simple. You create knowledge bases and then you invoke them within your prompts.

*Creating and updating knowledge bases*

When you create a knowledge base, these have a global context - they will work across all your Amazon Q CLI sessions.

* You can create knowledge bases by adding files or directories
* You can update those knowledge bases - for example, when you have made changes to those files (currently these will not automatically be updated)
* You can delete knowledge bases

*Invoking in your prompt*

Once you have created a knowledge base, you can then ask Amazon Q CLI to use your knowledge bases by adding "Use the knowledge tool" to your prompt.

**Getting started - an example**

Lets walk through an example use case to see this all come together. In my use case, I have a number of markdown documents that I typically add as context (using the "/context add xxx" command). To base line this test, I first ask the following prompt without any context

>  Can you provide me with guidance on how to write tests when writing python code

It very quickly provides me with some generic (but perfectly acceptable) output (which I have trimmed)

```
> I'd be happy to help you write tests for Python code! Here's a comprehensive
guide covering the key aspects of Python testing:

## Testing Framework - pytest

While Python has a built-in unittest module, pytest is the most popular and
developer-friendly testing framework:

...
```

Like many developers, I have been curating and refining a set of documents that I use as context to help bootstrap new projects and provide more personalised and specific output. After adding these context files, when I retry the same output I get different output which is more aligned with those context documents.

```
> Can you provide me with guidance on how to write tests when writing python code

> Based on the comprehensive testing guidelines from your workspace, here's
guidance on writing tests for Python code, specifically following the patterns
established in your FastAPI projects:

## Core Testing Principles

Test behavior, not implementation - Focus on what your code does, not how it does it.
Prefer integration-style unit tests that test multiple units together functionally
rather than isolated unit tests.

Mock only external dependencies at the lowest level (database operations, API calls,
file system operations). Don't mock your own business logic.

....
```

To check my current context usage,  I run the **"/usage"** command, I get the following:

```
█ Context files: ~23990 tokens (11.99%)
```

I am currently using over 10% of my context window. Lets look at how using this new **"/knowledge"** feature can help me out. I first close my existing chat session and open up a new one and make sure that my current context is empty (using the **"/usage"** command).

```
█ Context files: ~120 tokens (0.06%)
```

The first thing I am going to do is create a new knowledge base, adding my context docs to this knowledge base. Rather than adding them individually (they are currently single markdown files) I put them in a directory called "kb-docs", and then run the following command:

```
> /knowledge add /Users/ricsue/amazon-q-developer-cli/knowledge/kb-docs

🚀 Started indexing '/Users/ricsue/amazon-q-developer-cli/knowledge/kb-docs'
📁 Path: /Users/ricsue/amazon-q-developer-cli/knowledge/kb-docs
🆔 Operation ID: b111463f.

```

You will notice that I have to use the full absolute path to the directory where I have put my markdown docs.

> **Where does it create the knowledge base?** You might be wondering where /knowledge add creates the knowledge base. In your home directory, you will see a **".semantic_search"** folder, which contains a directory that matches the data and configuration for the knowledge base. You don't need to touch these files, but I always like knowing where these things live.

I can check on the status of the indexing by running the **"/knowledge status"** command, but the indexing has already finished so there is nothing to report.

```
> /knowledge status

📚 Total contexts: 1 (1 persistent, 0 volatile)
✅ No active operations
```

And I can now use the **"/knowledge show"** to display the available knowledge bases available to Amazon Q CLI - remember these are global in nature.

```
> /knowledge show

📚 Knowledge Base Contexts:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📂 1f48abc6-f12e-42c3-b765-87b68ae15377: /Users/ricsue/amazon-q-developer-cli/knowledge/kb-docs
   Description: Knowledge context for /Users/ricsue/amazon-q-developer-cli/knowledge/kb-docs
   Created: 2025-07-02 21:08:39
   Updated: 2025-07-02 21:08:39
   Source: /Users/ricsue/amazon-q-developer-cli/knowledge/kb-docs
   Items: 7 | Persistent: Yes
```

When I check my context usage, I can see that its not changed:

```
█ Context files: ~120 tokens (0.06%)
```

When I now retry my prompt, I add the "Use the knowledge tool" to the prompt.

> Can you provide me with guidance on how to write tests when writing python code. Use the knowledge tool

The first thing we notice is that we can see that the knowledge tool has been invoked

```
🛠️  Using tool: knowledge (trusted)
 ⋮
 ● Searching knowledge base for: python testing unit tests pytest unittest across all contexts
 ⋮
 ● Completed in 0.47s
```

and then we can see that it gives similar output to when we added those files to our context. It is not the same, but the guidance is broadly similar.

```
> Based on the knowledge base, I can provide you with comprehensive guidance on writing tests in Python. While
the knowledge base contains primarily TypeScript/JavaScript testing patterns, the core principles translate
well to Python testing. Here's a complete guide:

## Core Testing Principles

Test-Driven Development (TDD) is fundamental - write tests first, then implement code to make them pass. This
ensures your code is testable and meets requirements.

### Key Testing Philosophy
• **Test behavior, not implementation** - treat your code as a black box and test through public APIs
• **100% coverage through business behavior** - achieve full coverage by testing expected business outcomes
• **No implementation detail testing** - avoid testing internal functions directly
```

**Updating files**

As you update, add, or want to remove information from those documents you will need to update your knowledge base. Currently these are not automatically updated in the index so you have to do this yourself.

When you run **"/knowledge show"**, one of the pieces of information it provides is the number of items in the index. In my example, I go to the directory and I add a new file. To make sure that /knowledge will use that, I need to update the index using the following command: **"/knowledge update"** followed by the directory of your knowledge base. Using the example above, I update my index using the following command:

```
/knowledge update /Users/ricsue/amazon-q-developer-cli/knowledge/kb-docs
```

And when I now run **"/knowledge show"** I get the following:

```
> /knowledge show

📚 Knowledge Base Contexts:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📂 a114fda9-5b61-4aa8-8218-e141b80720ad: /Users/ricsue/amazon-q-developer-cli/knowledge/kb-docs
   Description: Knowledge context for /Users/ricsue/amazon-q-developer-cli/knowledge/kb-docs
   Created: 2025-07-02 21:47:37
   Updated: 2025-07-02 21:47:37
   Source: /Users/ricsue/amazon-q-developer-cli/knowledge/kb-docs
   Items: 8 | Persistent: Yes

```
You can see that the number of items has changed (from 7 to 8). If I removed or made any changes to the files, I would need to repeat this process to make sure that the local index gets updated.


**Adding multiple knowledge bases**

So far we have just created a single knowledge base, but we can create multiple. From the same Amazon Q CLI session, I decide to create a new knowledge base for all things nodeJS. I create my new directory, and then create this new knowldege base using the following command:

```
> /knowledge add /Users/ricsue/amazon-q-developer-cli/knowledge/node-kb

🚀 Started indexing '/Users/ricsue/amazon-q-developer-cli/knowledge/node-kb'
📁 Path: /Users/ricsue/amazon-q-developer-cli/knowledge/node-kb
🆔 Operation ID: 304f00e6.
```

and now when I run the **"/knowledge show"** command, I can see I have more than one knowledge base.

```
📚 Knowledge Base Contexts:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📂 a114fda9-5b61-4aa8-8218-e141b80720ad: /Users/ricsue/amazon-q-developer-cli/knowledge/kb-docs
   Description: Knowledge context for /Users/ricsue/amazon-q-developer-cli/knowledge/kb-docs
   Created: 2025-07-02 21:47:37
   Updated: 2025-07-02 21:47:37
   Source: /Users/ricsue/amazon-q-developer-cli/knowledge/kb-docs
   Items: 8 | Persistent: Yes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📂 f0ac6673-5071-4b01-a839-fac67b65ba32: /Users/ricsue/amazon-q-developer-cli/knowledge/node-kb
   Description: Knowledge context for /Users/ricsue/amazon-q-developer-cli/knowledge/node-kb
   Created: 2025-07-02 21:53:48
   Updated: 2025-07-02 21:53:48
   Source: /Users/ricsue/amazon-q-developer-cli/knowledge/node-kb
   Items: 2 | Persistent: Yes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Deleting a knowledge base**

Ok, so you have some fun and create a bunch of knowledge bases and then decided you want to remove one of them. No worries, you can use the **"/knowledge remove"** command to do this, together with the full path you originally used when creating it. To remove the knowledge base I just created in the previous step, I would run the following command:

```
> /knowledge remove /Users/ricsue/amazon-q-developer-cli/knowledge/node-kb
```

Which generates the following output:

```
Removed context with path '/Users/ricsue/amazon-q-developer-cli/knowledge/node-kb'
``` 

**Removing ALL your knowledge bases**

If you decided you want to remove your knowledge bases, then you can use the **"/knowledge clear"** command, which will ask you to confirm this nuclear option (there is no undo) which will then proceed to remove the knowledge base. It will not delete/remove the actual files, just the index.

```
> /knowledge clear

⚠️  This will remove ALL knowledge base entries. Are you sure? (y/N): y
🛑 Cancelling any pending operations...
🗑️  Clearing all knowledge base entries...

✅ Successfully cleared 1 knowledge base entries

```

**Things to know about**

When you create a knowledge base, these persist and are global in scope.

Currently this feature limits you to 5K documents when creating knowledge bases, so if you are adding directories with large amounts of documents this is something to watch out for.

If you really want to geek out, you can take a look at the [source code](https://github.com/aws/amazon-q-developer-cli-autocomplete/pull/101/commits/e9f3615796c80f686d9a2bb61f39a0d6dad352de) which reveals a lot of potentially useful info that will allow you to optimise how you use this feature.


**Conclusion**

This was a quick post that showed how you can enable experiment features in Amazon Q CLI like **"/knowledge"** that provide new capabilities for how you can manage context, and provide supporting information with your prompts. One thing you might be wondering is when to use one vs the other. 

Using **"/context"** provides supporting information that you define automatically with your prompt. The downside to this is that it can  take up space even when the information is irrelevant to the task you're asking the model to do. Using **"/knowledge"** allows you to index large amounts of information, which is retrieved on demand by the model. However, the model might not know when to look up the missing information and you will need to guide it. Currently you also need to automatically update these indexes as you update them.

We are excited to see how developers will experiment with and use this feature, and I would love to hear from folks who make interesting discoveries.

> **Not tried Amazon Q CLI? I hope this blog post has inspired you to want to try Amazon Q CLI for yourself. You can try it for free by [signing up for a Builder ID](https://community.aws/builderid?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el) and then downloading the app [from here](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el).

Until next time folks!

Made with 🧡 by DevRel!
