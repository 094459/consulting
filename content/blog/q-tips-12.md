+++
title = "Amazon Q Developer Tips: No.12 Mastering in-line prompts"
date = 2024-12-12
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no12-mastering-in-line-prompts-247k"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no11-scaffolding-5c6m).

Ok, time for today's tip....

### Tip 12 - Guiding Amazon Q : Mastering in-line prompts

One of the core features of Amazon Q Developer is the in-line editing code suggestions. Amazon Q supports a number of different ways you can enter instructions (prompts) that it will use to provide code suggestions. We can summarise these as the following:

* Function prompt
* Single line comment
* Multi line comment
* Single line prompt
* Multi line prompt
* Inline prompt

With the exception of the Inline prompt, after entering a prompt and hitting return, this will invoke Amazon Q and it will provide you with some code suggestions. 

> **Changing the Amazon Q Developer auto prompting behaviour** - by default Amazon Q Developer is configured to auto-suggest code. You can turn this behaviour on/off through by clicking on the Amazon Q link in the VSCode status bar and then toggling the behaviour. You will notice that the Amazon Q icon in the status bar will change from a triangle (play) to two vertical bars (pause) which will show you at a quick glance what you have configured.

Once Amazon Q Developer has provided some code suggestions, you can cycle through those code suggestions using the **<** and **>** arrow keys. Sometimes you might only get a single code suggestion in which case the arrow keys will do nothing. You will notice the code is shown in grey italic (depending on the theme you have setup in VSCode). You can accept the code suggestions by hitting **TAB**.

You can also just incrementally accept code (word by word) by using **OPTION** and **TAB** (or **CTRL** on a Windows or Linux based machine)


### Function prompt

Amazon Q Developer can understand your intent and provides suggestions based on the function names. The more descriptive the function name is, the better the suggestions. For example, if I open up a new file in VSCode, and type the following:

```
def get_average(numbers):
```

As I type Amazon Q Developer already anticipates what you want and provide some code suggestions. I am then able to cycle between suggestions using the < and > cursor keys, and accept with TAB or quit by hitting ESC. You can try this for yourself and see if you see the same thing.

You get better code suggestions if you define your function names more descriptively.

### Single and multi-line comments

Amazon Q Developer can understand your intent and provides suggestions based on single line comments. For example, in the IDE when I type the following:

```
# function to get the average of a set of numbers
```

When you hit return, you will see Amazon Q provide some code suggestions.

**Multi line comment**

This works the same as the previous one, except you can have the comments over a number of lines. For example, when I type the following into my IDE

```
"""
Given a list that contains some numbers and strings, 
format the list elements into a string in which the numbers are prepended with a "#" 
and check for strings and wrap in a double quote.
"""
```

When you hit enter, Amazon Q provides me with more code suggestions.


### Single and multi-line prompt

Amazon Q Developer will understand your intent and provides suggestions based on the a prompt that you provide within the file you are working on. For example, when I type the following into VSCode and then hit return.

```
# CREATE a function called get user age, ask the user to input their age, and RETURN the user's age
```

Amazon Q Developer creates code based on this single line prompt.

**Multi-line prompt**

This works exactly like the previous one, except you can put your prompts on multiple lines. For example

```
 # CREATE a function called get user age
 # ask the user to input their age
 # RETURN the user's age
```

### In-line prompt

Amazon Q Developer's in-line prompt works slightly differently and was introduced in the past few months. It provides similar capabilities to what you might traditionally have used within the Amazon Q Developer chat interface, but allows developers to maximise speed and lower friction by keeping them within the actual file they are editing.

 There are two modes you can use it in:

* From the either the position where your cursor is within the current open file
* Selecting a block of code 

The behaviour is similar. You invoke it with **COMMAND** (Mac), **CTRL** (Windows/Linux) + **I** , and this will bring up a command prompt window. You can now enter your prompt, and Amazon Q Developer will start to do its work right there within the actual file you are editing.

You will see your code blocks highlight in Green/Red based on new or changed/deleted code, with an option to Accept (Enter) or Reject (ESC) the suggestions.

I find this mode very powerful and improves the speed at which I can make updates/changes to my code. It tends to work well for specific ways you might want to work - updating existing code blocks for example, adding new functions, asking for optimisations, adding try / catch blocks, and more.


Check out this short video of this in action.

{{< youtube m7ccdXBrcxs >}}

**Things to think about when using in-line prompts**

I love using the in-line capabilities of Amazon Q Developer, but I have discovered there are a couple of things that caught me out.

* **Check for keyboard shortcut conflicts**  - If you me you have multiple plugins and extensions running in your VSCode environment, you might find that some of the Amazon Q keyboard shortcuts might not work. Check to see if you do have conflicts and then disable or amend plugins as needed.

* **Copy/pasting prompts** - When copying a prompt into your code, you may find that Amazon Q Developer does not respond and provide any code suggestions. Manually typing the same text will then work. 


**Try Amazon Q Developer today, and claim your free Builder ID**

That's it for today's tip. Let me know how you get on with this tip, and if you have your own drop me a message or reply. I would love to feature them here.

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
