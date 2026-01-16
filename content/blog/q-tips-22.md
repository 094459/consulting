+++
title = "Amazon Q Developer Tips: No.22 Amazon Q Keyboard shortcuts"
date = 2024-12-23
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no22-amazon-q-keyboard-shortcuts-2kfc"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no21-amazon-q-developer-agents-test-37o5).

Ok, time for today's tip....

### Tip 22 - Amazon Q Developer : Amazon Q Keyboard shortcuts

You can use keyboard shortcuts with Amazon Q Developer to improve the developer experience, and its good to know that you can access every feature this way.

**Keyboard shortcuts**

Here are the ones that I use the most:

> If you are using Windows, replace COMMAND + OPTION with CTRL + ALT

* **COMMAND** + **OPTION** + **I** - using this within VSCode moves the current cursor focus to the Amazon Q Developer chat window. I use this one a lot, especially as I have the Amazon Q Chat interface on the right hand side. When starting VSCode, this panel is normally closed, so this shortcut brings it back (and is easier than clicking on the Amazon Q status bar at the bottom of VSCode.

The following are the keyboard shortcuts from the VSCode menu integration. I use these a lot - I select the block of code I am interested in, and then right than right click, etc, I just use these shortcuts to save effort.

* **COMMAND** + **OPTION** +  **E** - Explain
* **COMMAND** + **OPTION** +  **F** - Fix
* **COMMAND** + **OPTION** +  **A** - Optimise
* **COMMAND** + **OPTION** + **U** - Refactor
* **COMMAND** + **OPTION** +  **Q** - Send to prompt
* **COMMAND** + **OPTION** +  **T** - Generate tests

When working with files, then these shortcuts are essential:

* **COMMAND** + **OPTION**  + **I** - inline prompt/chat
* **COMMAND** + **OPTION**  + **C** - invoke Q if you have turned off Amazon Q automatic suggestions

> **Tip!** Not related to Amazon Q Developer, but one of the best keyboard shortcuts I use which I discovered after much searching, was how to switch between multiple instances of VSCode. If you have multiple VSCode instances up, then switching between then (using the Windows > VSCode instance) can be tedious. Using **COMMAND** and **`** on my Mac keyboard allows me to quickly switch between instances in the same way as COMMAND + TAB allows you to switch between applications. 

**Viewing every Amazon Q Developer shortcut**

To view the complete list of keyboard shortcuts, from VSCode, you press SHIFT + COMMAND and P, which will then bring up VSCodes command palette. Type "Keyboard" and you should see "Keyboard Shortcuts" appear. 

Select that and from the search, type "Amazon Q" and you should now see all the keyboard short cuts available. This is useful to know as this post will age and become out of date as new features are added, so its good to know how to get to this page to check out the complete and latest version based on the version of the Amazon Q Developer plugin you are using.

![View Amazon Q Keyboard shortcuts](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/g5pwy2scy6v3zo7098vw.png)

If you prefer a text version of this, then from the VSCode command palette, from the search bar type "Keyboard " and from the list that appears select "Open Default Keyboard shortcuts JSON" and you will now see a JSON file that you can edit by hand.

**Changing or updating shortcuts**

I have found that as I have multiple extensions/plugins installed into my VSCode, that they can clash with the default Amazon Q Developer plugin shortcuts. It is useful therefore to know how you can change this - it is very easy.

From the Keyboard Shortcut screen (see the previous section) if you move the mouse pointer to the left of the Command column, you will see it change to a pencil. Clicking on this brings up a dialog asking you to enter the desired change of keys. As you press key combinations they will appear.

![Changing Keyboard shortcuts](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fkpm6bhlqg3qctmt05pd.png)

If you get stuck, you can press ESC to go back.

As you enter key combinations, it is clever enough to tell you whether the choice you have selected clashes with something else (and helpfully provides a link for you).

**Try Amazon Q Developer today, and claim your free Builder ID**

That's it for today's tip. Let me know how you get on with this tip, and if you have your own drop me a message or reply. I would love to feature them here.

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
