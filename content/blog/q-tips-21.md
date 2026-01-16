+++
title = "Amazon Q Developer Tips: No.21 Amazon Q Developer Agents - /test"
date = 2024-12-21
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no21-amazon-q-developer-agents-test-37o5"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no20-amazon-q-developer-agents-review-2b6l).

Ok, time for today's tip....

### Tip 21 - Amazon Q Developer Agents : /test

Amazon Q Developer provides a number of tools for developers to use. /test is a new addition that was announced at re:Invent 2024, that will help you when adding tests to your project.

**/test**

You can ask Amazon Q Developer Agents to generate tests for you. You first have to open the code you want to add tests to, and then can test specific code/functions (highlighting the code and then using the IDE menu integration (see below), or add tests for the whole file using /test.

When invoking /test from the chat interface, you can (optionally) provide the names of the functions/classes you want to add tests for - the default behaviour is to add tests for all of these in the current open file in your editor.  This is the equivalent of highlighting a code block and then using the integrated menu option (see below).

> You cannot provide additional context to steer the direction of the tests.

The UI will show you a progress bar, and then show you the generated test code which you can review and then accept.

![Generating tests](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xtp2bicbhu7e9umg0c6s.png)

*Running tests*

One thing I have found is that running tests will typically fail, and I am able to fix these by:

* installing additional dependencies - whilst the test cases are generated, you will need to install additional libraries to run the tests. You can use Amazon Q Developer to help you here.
* adding __init__.py files - if you are running Python tests, I have found that you need to add __init__.py to your current project (at each relevant directory) to avoid the tests not failing (when using PyTest)

**IDE menu integration**

You can invoke /test from within the actual file you are editing to, as a new option has been added to the menu integration. After right clicking, you will see the new option "Generate Tests".

![IDE menu integration](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1sax58ps9vuyoi4fb3on.png)

The actual workflow then reverts to the standard /test workflow.

**Influencing test libraries**

**Pytest** and **unittest** (Python) and **JUnit** and **Mockito** (Java) are the only currently supported testing frameworks that /test supports. In my testing, it seems that PyTest tends to be the default option (a good choice in my view).

If you want to influence the use of one over the other, then I have found the way to do this is to:

1. Create a tests folder in your current project (if you do not have one)
2. Create a test file for the project file you want to add tests to - for example, tests_xxx if xxx is the name of the file you are adding tests for.
3. Add a single import statement (for example, "import unittest") and then save the file. 

When you then run /test, the tests generated will be for this library. I put together a quick video to show you this in action.

{{< youtube 1OcMXuX5KQ4 >}}
{% youtube 1OcMXuX5KQ4 %}

**Things to know about**

I have spent only a little time getting to know how /test works, probably the least of the new features. Here are some initial thoughts on things to think about that I discovered when testing this out (sorry, pun intended!):

* need to have your code open in the editor - you cannot run /test unless you have the code you want to provide tests for open in the editor. This means that you can only generate tests per file of your projects, and will need to repeat this process for each function within your project

* click on the "View Diff" button to review the code - in previous versions of the Amazon Q Developer plugin, clicking on the files that are generated when the agent has completed would automatically bring up the code diff. This behaviour has changed now, and you need to click on the "View Diff" button to see the actual code.

* Java and Python only - currently you can only use this feature if your codebase is Java or Python
 

* adding extra information in the /test prompt will generate failures - if you add some additional information in the prompt after /test, you might see the following error occur

![Test Error](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/htt47o0x3byn0x0inmfa.png)

* counts towards your service quota - as per the other agents, using this consumes one of your allocated quota for the month


> **Further reading** When it comes to testing in the generative AI era, I cannot recommend enough my colleague Danilo's blog post, [Beyond Traditional Testing: Addressing the Challenges of Non-Deterministic Software](https://dev.to/aws/beyond-traditional-testing-addressing-the-challenges-of-non-deterministic-software-583a)



**Try Amazon Q Developer today, and claim your free Builder ID**

That's it for today's tip. Let me know how you get on with this tip, and if you have your own drop me a message or reply. I would love to feature them here.

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
