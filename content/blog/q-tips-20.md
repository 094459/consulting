+++
title = "Amazon Q Developer Tips: No.20 Amazon Q Developer Agents - /review"
date = 2024-12-20
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/amazon-q-developer-tips-no20-amazon-q-developer-agents-review-2b6l"
+++

In this series I will be sharing daily hints and tips to help you get ahead and start to accelerate you on your own journey with Amazon Q Developer. Each day I will share a new tip, categorised against a few themes and topics. If you have your own tips or your own experiences with tips I share, please use the comment feature or feel free to contact me directly. Check out the previous tips [here](https://dev.to/aws/amazon-q-developer-tips-no19-amazon-q-developer-agents-doc-4d1k).

Ok, time for today's tip....

### Tip 20 - Amazon Q Developer Agents : /review

Amazon Q Developer provides a number of tools for developers to use. /review is a new addition that was announced at re:Invent 2024, and if you have been using Amazon Q Developer for sometime, also reflects an important change to how it works that you need to know about.

When you initiate a /review, Amazon Q will review your code against a number of criteria. I took the following from the [docs](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/code-reviews.html)

* **SAST scanning** — Detect security vulnerabilities in your source code. Amazon Q identifies various security issues, such as resource leaks, SQL injection, and cross-site scripting.
* **Secrets detection** — Prevent the exposure of sensitive or confidential information in your code. Amazon Q reviews your code and text files for secrets such as hardcoded passwords, database connection strings, and usernames. Secrets findings include information about the unprotected secret and how to protect it.
* **IaC issues** — Evaluate the security posture of your infrastructure files. Amazon Q can review your infrastructure as code (IaC) code files to detect misconfiguration, compliance, and security issues.
* **Code quality issues** — Ensure your code is meeting quality, maintainability, and efficiency standards. Amazon Q generates code issues related to various quality issues, including but not limited to performance, machine learning rules, and AWS best practices.
* **Code deployment risks** — Assess risks related to deploying code. Amazon Q determines if there any risks to deploying or releasing your code, including application performance and disruption to operations.
* **Software composition analysis (SCA)** — Evaluate third-party code. Amazon Q examines third-party components, libraries, frameworks, and dependencies integrated into your code, ensuring third-party code is secure and up to date.

What I had not seen before is supporting materials that can help you mitigate issues that are found. The [Amazon Q Detector Library](https://docs.aws.amazon.com/codeguru/detector-library/) provides a list of things it can detect for, showing example issues as well as sharing code on how to fix those issues.

*What has changed*

Amazon Q Developer used to enable you to run security scans from the Amazon Q Developer menu. This would kick off a project scan, generating actionable findings to help developers shift left with security. This has now gone. It is replaced with something way better, /review, which performs the same thing, but has a redesigned and improved workflow (in my opinion).

**/review**

You now kick off the process by typing **/review** within the Amazon Q Developer chat interface. You are provided with two options: 1/ Review all the files in the current project workspace, or 2/ Review the current open file.

The UI has changed so that you are now more informed about what is happening during the review process. 

![Review chat interface](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ltu0kldt1z7u0rbda6cs.png)

The findings/results from the review also appear at the top of the Amazon Q Developer sidebar - above the chat window.

![Results in chat interface](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/d7ea2v1x0dlc5t8tym4t.png)

For each issue found you can drill down into the issue by clicking on the magnifying glass icon, which will bring up the details as a new side window in the IDE

![Drilling into results](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/pu0momhzywyrrrqhwz77.jpg)

From here you are now able to act up on this - asking Amazon Q Developer to generate code to fix this, asking for additional information, or ignoring the issue if this is a false positive.

{{< youtube nZNaio3tW2k >}}

> **Ignore and Ignore All** When you click on the Ignore it will make the issue disappear from the list until the next time you run the scan. If you click on the Ignore All, it will add an exception (which is stored in the Amazon Q Developer plugin settings) and will not appear in future scans.
> 


The flow is much better for me, with fewer clicks and prompts that older versions of the Amazon Q Developer plugin.

**Configuring where /review displays its output**

By default, the findings of /review will appear above the chat window in the chat interface. You can change this by clicking on the three dots (...) and then deselecting Code Review from the viewing options listed. You will still be able to view the findings by looking at the "Problems" tab, which will still take you to the files associated with the problem.  You will not however be able to view the action options, so for that reason I tend to leave the output of /review in the main chat interface window. 

You can see this in more detail in the following short video:

{{< youtube ekJflyxTMTc >}}

**Things to know about**

I have spent only a little time getting to know how /review works, so will update this tip in the future as I learn more. In the meantime, here are some initial thoughts on things to think about:

* use .gitignore to filter out files you do not want to scan - I found that the scan took a lot longer when I had virtual Python environments, as well as other hidden directories. Once I configured .gitignore the scans ran much more quickly.

* new configuration option in the Amazon Q Developer plugin settings - if you select the "Ignore all" after a review, these will now appear in the plugin settings. From here you can edit/remove these as needed (especially helpful if you did this by accident).

![Review settings](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7r91wf11xgyf1yoobf8y.png)

* you can filter issues - if you find that a review has generated a lot of findings, the UI provides the ability to filter out by severity. This will help manage the clutter/noise as well as helping you focus on the critical issues you need to fix.

* counts towards your service quota - as per the other agents, using this consumes one of your allocated quota for the month. As such I would tend to use this to review all the files in my project rather than just the single file I have open.

* classifying code issue severity - the documentation ([here](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/code-issue-severity.html)) provides a nice overview of how Amazon Q Developer /review categorises and assess the severity of issues during the scan.

**Version control with git**

The project you are working on when initiating a /review will need to be under version control, specifically git. If you are using /review against a single file, then there is no requirement for having your code in source control (git specifically)

If the project you are current reviewing is not in a git source code repository, when running a project wide /review, you might see this in the logs:

```
2024-12-12 17:29:35.365 [warning] Failed to run command `PID 99262: [git rev-parse --is-inside-work-tree]`: Error: Command exited with non-zero code: 128
2024-12-12 17:29:35.367 [info] Command: (not started) [git ls-files --others --exclude-standard]
2024-12-12 17:29:35.391 [warning] Failed to check if file is new: Error: Command exited with non-zero code: 128
2024-12-12 17:29:35.391 [info] Command: (not started) [git diff HEAD --src-prefix=a/q-review-test/ --dst-prefix=b/q-review-test/]
2024-12-12 17:29:35.428 [warning] Failed to run command `PID 99291: [git diff HEAD --src-prefix=a/q-review-test/ --dst-prefix=b/q-review-test/]`: Error: Command exited with non-zero code: 129
```

You can resolve this by initialising your local project into a local git repository.


**Logging**

When you kick off a /review, you will see some information appear in the Amazon Q Developer Logs that you might need to reference to later (for troubleshooting purposes for example). You will see items such as 

```
Amazon Q Code Review requestId: 3417f427-40ab-4f57-9ef9-17ac7a6752c9 and Amazon Q Code Review jobId: fe8b8301-fec2-46bb-bf46-8541c5b7ab4c::b3b3f6a4-7a0b-4147-aa5d-9a4955082ef3
```

Within VSCode, you will also notice a new item appear in the OUTPUT options - Amazon Q Developer Security Scan Logs, which provide details of what files were scanned

```
2024-12-13 10:41:54 [INFO]: 1 file was scanned during the last Security Scan.
2024-12-13 10:41:54 [INFO]: File scanned: /Users/ricsue/Projects/amazon-q/live/feedback/q-review-test2/app.py
```


**Try Amazon Q Developer today, and claim your free Builder ID**

That's it for today's tip. Let me know how you get on with this tip, and if you have your own drop me a message or reply. I would love to feature them here.

You can try Amazon Q Developer for free today, [by signing up for a Builder ID](https://community.aws/builderid?trk=34e0ecce-8101-42c4-840a-fe6170420294&sc_channel=el). You can also check out [my other posts](https://community.aws/@ricsueaws) on community.aws, as I have been sharing a lot of tips and use cases of how I am using Amazon Q Developer. You can also keep up to date with all the new features and improvements of Amazon Q Developer by checking out the [changelog](https://aws.amazon.com/developer/generative-ai/amazon-q/change-log/).


---
Made with ♥ from DevRel
