+++
title = "Writing simple Python scripts faster with Amazon Q"
date = 2024-01-11
draft = false
tags = []
categories = ["Technical"]
+++

*The future is here folks! I share my experiences using Amazon Q in the IDE, and how I was able to write more quickly and with less friction.*

Some of you might be familiar with the AWS open source newsletter, a weekly publication that features a curated set of content for open source developers on AWS. I rely on a number of folk to share with me interesting open source projects that I feature, but I wanted to see if I could create an automated script that I could run on a weekly schedule that would find new open source projects for me to review. 

I have been exploring how I can use Amazon Q in VScode to help simplify these kinds of tasks, so I thought I would share my experiences. 

> tldr; It was amazing, and I was very impressed in how it both helped me to create exactly what I needed, but also how it helped correct and address issues that came along the way.

The goal I had was quite simple - I wanted to initially create a simple python function that displays all the new and updated open source projects within a set of GitHub organisations, so I can review these. Once this is working, I then want to run these on a scheduled basis and drop me a link to the output that is created. (That bit I will do in another post)

> **Note!** In this post you will see the dialog between Amazon Q and VSCode as inline quotes like the following:
> 
> > this stuff is what Amazon Q responded with

**Getting started**

From within VScode I created a new Python virtual environment (python -m venv find-oss-projects), activated this (source find-oss-projects/bin/activate), and then created my project directory and starting file (mkdir src && cd src && touch app.py) and was now ready to begin. I had [already setup Amazon Q](https://community.aws/content/2Yu3nix1YGNOQ6uxmaaipFceLEa/setting-up-amazon-q-in-vscode-using-iam-identity-centre), so you can look at that post if you want to follow along too.

Before starting to create some prompts in the Amazon Q sidebar, I opened up my app.py file. Amazon Q uses the existing files opened as part of the context when responding to your prompts, as well as allowing you to insert code suggestions directly from the chat dialog. 

> I want to create a simple python script that will crawl GitHub and list the new repositories for a given time frame

Which provided me a good summary, but didn't show me the code. I added an additional response.

> can you show me the code please

and Amazon Q provided me with the code (which worked) as well as some additional details.

```
import requests
response = requests.get('https://api.github.com/search/repositories', params={'q': 'created:>2021-03-01',  })
repos = response.json()['items']
for repo in repos:
  print(repo['name'])

```
Running this failed, which was expected as this was a fresh Python environment with no libraries installed. When I asked Amazon Q about the error, it provided useful info as well as the command needed to fix.

> I get the following error running that code - ModuleNotFoundError: No module named 'requests'

It responded with

> Based on the error message you provided, it looks like you may not have the 'requests' module installed in your Python environment. The code is making use of the 'requests' library to interface with the GitHub API. But if you see a 'ModuleNotFoundError' for 'requests', that means Python cannot find that module/package on your system.
> 
> To resolve it, you need to install the 'requests' package. You can do that with pip by running:
>
>```
> pip install requests
> ```

**Improving the script**

This was a great start, but what I really wanted this script to do is to crawl through some specific GitHub organisations for interesting projects to review. So I create a new prompt:

> can you tell me how to create a python script that lists all repos within a GitHub organisation please

And Amazon Q quickly returned the following:

> Here is an example of how to create a Python script that lists all repositories within a GitHub organization:
>
>First, you'll need to use the GitHub API to search repositories within an organization. The endpoint is GET /orgs/{org}/repos.
>
> For example:

>```
>import requests
>org = 'github' 
>response = requests.get(f'https://api.github.com/orgs/{org}/repos')
>```

> This will return all public repositories for the given organization. You can then extract the repository names and other attributes from the JSON response:

>```
>repos = response.json()
>for repo in repos:
>  print(repo['name'])
>
>```

> To make it more reusable, you could accept the organization name as a command line argument. You may also want to handle pagination if the organization has more than 30 repos.
> 
> Let me know if any part needs more explanation! As Amazon Q, my goal is to help you work with APIs and build scripts to automate tasks. Feel free to ask if you have any other questions.


This again provided working code which I was able to easily add to my file. Each time I used the "Insert at cursor" link that accompanies the code snippets, which made life super easy. 

I want to keep on building this up. The next step is to actually update this so that I only get projects created or updated in the last week.

> can you adjust the code so that it only shows the projects created in the last week

It very quickly returned the following:

>Here is how you can adjust the code to only show repositories created in the last week:
>
>First, you'll need to use the GitHub API to search for repositories. The API endpoint for searching repositories is GET /search/repositories. This allows you to filter repositories by various criteria in the query parameters, including creation date. [1]

> For example, to find repositories created in the last week you could do:
>
>```
>import requests
>
>response = requests.get('https://api.github.com/search/repositories', params={
  'q': 'created:>2021-03-01', 
>})
>```
>The 'created:>2021-03-01' filter will return only repositories created after March 1st, 2021. You can then loop through the response JSON and extract the repository name and other details you want from each result. Something like:
>
>```
>repos = response.json()['items']
>
>for repo in repos:
>  print(repo['name'])
> 
>```
> To make it more reusable, you could accept the time frame as a command line argument or config value rather than hardcoding the dates. You may also want to handle pagination in the API response if there are more than 30 results. Let me know if any part needs more explanation! As Amazon Q, I aim to help developers like yourself work with APIs and build useful tools.

This was great, but what I really wanted was it to show me the whole code, so I tried this prompt:

> can you show me the code please

And it then just lists the code, with some additional documentation.

> Sure, here is the code from the Python file that was shown:
> 
> ```
> import requests
>
>response = requests.get('https://api.github.com/search/repositories', params={
  'q': 'created:>2021-03-01',  
>})
>
>repos = response.json()['items']
>
>for repo in repos:
>  print(repo['name'])
> ```
>  

So the script is looking better but we are not quite there yet. At the moment, this provides me with repos across all GitHub orgs which is not what I need. I need to fine tune it so I work through a series of  prompts:

> - can you tell me how to create a python script that lists all repos within a GitHub organisation please
> - can you adjust the code so that it only shows the projects created in the last week

Which helps generate some promising looking code:

> Here is how you can adjust the code to only show repositories created in the last week:
>
> ```
> import requests
> import datetime
>
> org = 'github'
> one_week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
>
> response = requests.get(
>  f'https://api.github.com/orgs/{org}/repos', 
>  params={'since': one_week_ago.strftime('%Y-%m-%d')}
> )
>
> repos = response.json()['items']
>
> for repo in repos:
>  print(repo['name'])  
>
>```
> The key changes:
> 1. Import datetime to work with dates
> 2. Calculate one week ago as a datetime object
> 3. Pass the 'since' parameter to the API with the date as a string in YYYY-MM-DD format
>
>This will filter the results to only include repositories created since one week ago. Let me know if you have any other questions!

**Help! Amazon Q to the rescue!**

Copying this code and then running it generated an error, so I see if Amazon Q can help me troubleshoot this issue:

> That code generates the following error: TypeError: list indices must be integers or slices, not str

And sure enough, it comes back with a fix for me:

> Based on the error message, it looks like you are getting a TypeError when trying to access the repos list like a dictionary.
> 
> The response.json() call is returning a list, so you need to iterate over it using integers as the index rather than strings.
> 
> Try changing this:
> 
> ```
> repos = response.json()[‘items’]
> ```
> 
> To this:
> 
> ```
> repos = response.json()
> ```
> 
> And access the name like:
> 
> ```
> for repo in repos:
>  print(repo[0]['name'])
> ```
> 

Sure enough this got the code running. An experienced developer will likely pick up these things as you are coding, but I wanted to share how you can use this flow which will be useful as you tackle more tricky errors in libraries that you may be less familiar with.

**Finishing the script**

We are getting there, but now there are a few more things I need my script to do. First I need to get some sort of sorting by most recent, and then I need to create some kind of output so I can review.

To get started I try the following:

> Can you sort the output by most recent please?

And it helpfully provides a update to the code:

> To sort the output of repositories by most recent, you can pass the 'sort' parameter to the GitHub API request. For example, to sort by most recently updated:
> 
> ```
> response = requests.get(
>  f'https://api.github.com/orgs/{org}/repos',
>  params={'sort': 'updated'}
>)
>```
> Or to sort by most recently created:
>
>```
>response = requests.get(
>  f'https://api.github.com/orgs/{org}/repos',
>  params={'sort': 'created'}
>)
>```
>
>The 'sort' parameter accepts 'created' and 'updated' values. This will change the order of the repositories in the API response to be sorted by that date field most recently to least recently. Let me know if you have any other questions!

We are making progress. Now lets see about generating some output.

> can you adjust the code to include the url for the repo please?

And almost immediately we get the following back from Q.

> Here is how you can adjust the code to include the URL for each repository:
> 
> ```
> import requests
> import datetime
>
> org = 'aws-samples'
> one_week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
>
>response = requests.get(
>  f'https://api.github.com/orgs/{org}/repos',
>  params={'since': one_week_ago.strftime('%Y-%m-%d'), 'sort': 'created', 'direction': 'desc'}
>)
>
>repos = response.json()
>
> for repo in repos:
>  print(repo['name'], repo['html_url'])
> 
> ```
>
> Each repository object in the JSON response from GitHub will include an 'html_url' field containing the URL. 
> By printing both the 'name' and 'html_url' for each repo, this will output the name and URL together on each line.
>

When I run this script from the terminal, I now get the following output:

```
transactional-datalake-using-amazon-msk-serverless-and-apache-iceberg-on-aws-glue       2024-01-10T01:26:56Z    https://github.com/aws-samples/transactional-datalake-using-amazon-msk-serverless-and-apache-iceberg-on-aws-glue
aws-msk-serverless-cdc-data-pipeline-with-debezium      2024-01-09T01:03:38Z    https://github.com/aws-samples/aws-msk-serverless-cdc-data-pipeline-with-debezium
aws-healthlake-smart-on-fhir    2024-01-08T23:05:17Z    https://github.com/aws-samples/aws-healthlake-smart-on-fhir
aws-greengrass-custom-components        2024-01-08T11:34:12Z    https://github.com/aws-samples/aws-greengrass-custom-components
graviton-developer-workshop     2024-01-08T03:30:31Z    https://github.com/aws-samples/graviton-developer-workshop
msk-flink-streaming-cdk 2024-01-08T02:25:39Z    https://github.com/aws-samples/msk-flink-streaming-cdk
rag-with-amazon-postgresql-using-pgvector       2024-01-06T04:47:41Z    https://github.com/aws-samples/rag-with-amazon-postgresql-using-pgvector
queueTransfer_ContactTraceRecordSupport-for-Service-Cloud-Voice 2024-01-05T20:34:14Z    https://github.com/aws-samples/queueTransfer_ContactTraceRecordSupport-for-Service-Cloud-Voice
amazon-chime-sdk-voice-voice-translator 2024-01-05T17:25:54Z    https://github.com/aws-samples/amazon-chime-sdk-voice-voice-translator
private-s3-vpce 2024-01-05T06:38:52Z    https://github.com/aws-samples/private-s3-vpce
bedrock-contact-center-tasks-eval       2024-01-04T21:46:51Z    https://github.com/aws-samples/bedrock-contact-center-tasks-eval
clickstream-sdk-samples 2024-01-04T07:21:52Z    https://github.com/aws-samples/clickstream-sdk-samples
aws-msk-cdc-data-pipeline-with-debezium 2024-01-04T04:09:22Z    https://github.com/aws-samples/aws-msk-cdc-data-pipeline-with-debezium
transactional-datalake-using-amazon-msk-and-apache-iceberg-on-aws-glue  2024-01-04T03:39:04Z    https://github.com/aws-samples/transactional-datalake-using-amazon-msk-and-apache-iceberg-on-aws-glue
..

```

Not too shabby at all, all done in just a few minutes. What I am really looking to do is create a weekly report that I will be sent that contains the output of this, so I am figuring that maybe generating output as pdf with links would be useful. I could then copy this file to an Amazon S3 bucket and then send me a notification link when its run. Let's see how Amazon Q can help us here.

> ow can i wrap this up in a nice report that exports as a pdf 

And sure enough, it provides me with some addition code to include:

> Here is how you can generate a PDF report from the GitHub repository data:
> 
> First, import the FPDF library which allows generating PDF documents from Python: 
> 
>```
>from fpdf import FPDF
>```
>
> Next, initialize a new FPDF object and add some basic styles:
> 
> ```
> pdf = FPDF() 
> pdf.add_page()
> pdf.set_font("Arial", size=12)
> ```
> 
>  Then loop through the repository data and add each entry to the PDF:
> 
> ```
> for repo in repos:
>  pdf.cell(200, 10, txt=f"{repo['name']}", ln=1)
>  pdf.cell(200, 10, txt=f"{repo['created_at']}", ln=1) 
>  pdf.cell(200, 10, txt=f"{repo['html_url']}", ln=1)
> ```
> 
>  Finally, save the PDF file:
>
>```
> pdf.output("report.pdf")
> ```
> 
> This will generate a simple multi-page PDF with the repository info. You can customize further by adding headers, images, formatting etc.

Running the new code generates a new error as I have not installed the supporting Python library that this code uses. Amazon Q provides me with help to resolve this issue, and after "pip install fpdf" the code runs perfectly, and I now have an pdf file called report.pdf in the folder where I ran this command.

We are nearly done. So far, this outputs the projects from a single GitHub organisation, but I need to scan multiple ones. I need to update the code so that I can cycle through a number of GitHub orgs and list the repos that I might be interested in. Lets see how Amazon Q handles this task.

For the prompt I try:

> How can I change the code to cycle through a number of GitHub org's repositories please?

And as expected, Amazon Q provides me with some help to do this with code:

> To cycle through repositories from multiple GitHub organizations, you can create a list of orgs and loop through them in your code.
> 
> For example:
> 
> ```
> import requests
>
> orgs = ['aws-samples', 'github', 'python'] 
> for org in orgs:
>
>  response = requests.get(
>    f'https://api.github.com/orgs/{org}/repos',
>    params={'sort': 'created', 'direction': 'desc'}
>  )
>
>  repos = response.json()
>
>  for repo in repos:
>    print(repo['name'])
> ```
> 
> This will:
>
> 1. Define a list of organizations to query, 
> 2. Loop through each org
> 3. Make the API request to that org's repos endpoint
> 4. Print out each repo name
> 
> You could also consolidate the results into a single list or dictionary to report on all repositories together.

I update the code and sure enough, it now cycles through the different GitHub organisations and brings me back the projects....way too many in fact, so lets tweak that.

> can you adjust the code so it only brings back the first 10 repos

And it helps me by providing what I need to change

> Here is how you can adjust the code to only retrieve the first 10 repositories from each organization:
> 
> ```
> import requests
>
>orgs = ['aws-samples', 'awslabs', etc]
>
>for org in orgs:
>
>  response = requests.get(
>    f'https://api.github.com/orgs/{org}/repos',
>    params={'sort': 'created', 'direction': 'desc', 'per_page': 10}
>  )
>
>  repos = response.json()
>
>  for repo in repos[:10]:
>    print(repo['name'])
> ```
> 
>  The key change is adding a 'per_page' parameter to the API request with a value of 10. This will make each request return up to 10 repositories maximum. Then by slicing the repos list to the first 10 elements, it will only loop through and process the first 10 from each org.

When I update the code and run this, voila, I now get a much more manageable list. 

Looking at the report that is exported, I think it would be great to see each GitHub org's projects on separate pages, so lets see how Amazon Q handles that task.

> how can i change the pdf output so that each org starts on a new page please?

I am instructed what needs to be changed:

> To start a new page in the PDF for each organization, you can add a call to pdf.add_page() inside the org loop. For example:
> 
> ```
> for org in orgs:
>  response = requests.get(f'https://api.github.com/orgs/{org}/repos', params)
>  repos = response.json()
>  pdf.add_page() # Add new page
>  for repo in repos[:10]:
>    pdf.cell(200, 10, txt=f"{repo['name']}")
>
> ```
> This will reset the page after processing each org's repositories, so each org's data starts on a fresh page.
> 

**Uploading the pdf reports to Amazon S3**

Now that I have my pdf report, I want to save these on Amazon S3 as this will allow me to access these irrespective of where this script is run. Lets ask Q to help.

> How can I save and upload the pdf file to an S3 bucket, making sure that each report has a unique name based on the date?

And very swiftly, I get what I need.

> To save and upload the generated PDF report to an S3 bucket with a unique name based on the date, you can do the following:
> 
> Import the necessary S3 client and date/time modules:
> 
> ```
> import boto3
> from datetime import datetime
> ```
> 
> Define a function that uploads the file to S3:
> 
> ```
> def upload_to_s3(file_name, bucket, object_name=None):
>   """Upload a file to an S3 bucket
>   """
>   if object_name is None:
>      object_name = file_name
>
>   # Upload the file
>   s3_client = boto3.client('s3')
>   response = s3_client.upload_file(file_name, bucket, object_name)
> ```
> 
> Generate a unique filename using the current date/time:
> 
> ```
> date_str = datetime.now().strftime("%Y%m%d%H%M%S")
> file_name = f"report-{date_str}.pdf"
> ```
> 
> Save and upload the PDF after generation:
> 
> ```
> pdf.output(file_name)
> upload_to_s3(file_name, "my-bucket")
> ```
> 
> This will save each report with a unique name based on the timestamp and upload it to the specified S3 bucket.
> 

Running this generates an error (ModuleNotFoundError: No module named 'boto3') which is kind of to be expected and Amazon Q tells me how to resolve this. When I then run this again, I now get a different error. Mmmm, such is the life of developers. You think it is going to work, until you realise you forgot something.

In this case, I got the error - "The specified bucket does not exist" which makes total sense as I have not created it. Lets see how Q can help me fix this.

> The code generated an error : The specified bucket does not exist. can you update the code to fix that

And it provides some alternative code I can use:

> Based on the error message you provided, it seems the issue is that the S3 bucket specified does not exist. To fix this, you have a few options: 
> 
> 1. Create the S3 bucket manually through the S3 console if it hasn't been created already. Make sure the bucket name matches what is specified in the code. 
> 2. Add code to first check if the bucket exists, and if not, create it:
> 
> ```
> import boto3
> 
> s3 = boto3.client('s3')
> 
> try:
>  s3.head_bucket(Bucket='XXXXXXXX')
> except botocore.exceptions.ClientError as e:
>  if e.response['Error']['Code'] == '404':
>    s3.create_bucket(Bucket='XXXXXXXX')
>```
>
>Handle the error when the bucket doesn't exist by catching the exception and creating the bucket:
>
>```
>try:
>  # upload object
>except ClientError as e:
>   if e.response['Error']['Code'] == "NoSuchBucket":
>       s3.create_bucket(Bucket='XXXXXXXX')  
>       # retry upload object
>```

Running this generated more errors! Blimey, this is turning to be a roller coaster ride. It turns out that by default, when you use s3.create_bucket, it will default to us-east-1, and so we need to add some additional parameters. How do I know that, well I asked Q of course!

> The code generates this error - botocore.exceptions.ClientError: An error occurred (IllegalLocationConstraintException) when calling the CreateBucket operation: The unspecified location constraint is incompatible for the region specific endpoint this request was sent to.       

And it helpfully provided this info:

> Thank you for providing the error message. It looks like the issue is that when creating the S3 bucket, a location constraint is not being specified that matches the AWS region of the request. By default, S3 will use the region of the endpoint to determine bucket location, but this error occurs when those don't match.
> 
> To resolve it, you have a couple options:
> 
> 1. Specify the location constraint explicitly when creating the bucket to match the region. For example:
> 
> ```
> s3.create_bucket(Bucket='XXXXXXXXXX', CreateBucketConfiguration={'LocationConstraint': 'XXXXXXXXXXX'})
> ```
> 
> 2. Ensure the AWS credentials/configuration are set up to use the same region as the intended bucket location.
> 

Let's try and run this - I wonder what new errors this will generate :-) As it turns out, it doesn't and we now have our report sitting in our S3 bucket. Finally, we have made it and we now have a working and useful script. 

Thank you Amazon Q, you have been a super star.

**The finished code**

Here is the output of the finished code, which took me all of about 10 minutes to complete:

```
import requests
import datetime
from fpdf import FPDF
import boto3
import botocore

pdf = FPDF() 
pdf.add_page()
pdf.set_font("Arial", size=8)
s3 = boto3.client('s3', region_name='eu-west-1')

orgs = ['aws-samples','awslabs','aws','aws-ia','aws-quickstart','aws-solutions',]

def upload_to_s3(file_name, bucket, object_name=None):
   """Upload a file to an S3 bucket
   """
   if object_name is None:
      object_name = file_name

   # Upload the file
   s3_client = boto3.client('s3')
   response = s3_client.upload_file(file_name, bucket, object_name)

one_week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
for org in orgs:
    try:
        response = requests.get(f'https://api.github.com/orgs/{org}/repos', 
        params={'since': one_week_ago.strftime('%Y-%m-%d'), 'sort': 'created', 'direction': 'desc'}
        )
        repos = response.json()
    except requests.exceptions.HTTPError as err:
        print(err)
        continue

    pdf.add_page()
    pdf.cell(0,10,txt=org,ln=1,align='C')

    for repo in repos[:10]:
        print(repo['name'], repo['created_at'], repo['html_url'], sep='\t')
        pdf.cell(200, 10, txt=f"{repo['name']}", ln=1, align='L')
        pdf.cell(200, 10, txt=f"{repo['created_at']}", ln=1, align='L')
        pdf.cell(200, 10, txt=f"{repo['html_url']}", ln=1, align='L')

s3_bucket_name = "094459-oss-projects"
try:
  s3.head_bucket(Bucket=s3_bucket_name)
except botocore.exceptions.ClientError as e:
  if e.response['Error']['Code'] == '404':
    s3.create_bucket(Bucket=s3_bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
    print("Bucket created successfully")
date_str = datetime.datetime.now().strftime("%Y%m%d")
file_name = f"report-{date_str}.pdf"
pdf.output(file_name)
upload_to_s3(file_name, s3_bucket_name)


```

**Running this on a schedule**

Now that I have my script, I want to run this on a weekly basis. Lets see if Q can help me with some ideas of the best way to do this.

> How would i run this python script on a scheduled basis

It returns the following list.

> There are a few different ways you could run your Python script on a scheduled basis:
> 
> 1. AWS Lambda - You can configure a Lambda function to run your script and trigger it on a schedule using services like CloudWatch Events. This is a serverless option that doesn't require managing servers.
> 2. EC2 Instance Scheduler - For scripts that need more resources, use the Instance Scheduler to automate starting/stopping an EC2 instance on a schedule to run your script.
> 3. Step Functions - With Step Functions you can build a workflow that includes scheduled events to trigger a Lambda function running your script or other steps.
> 4. Systems Manager Automation - Use SSM Automation to run your script on a schedule via SSM documents and Automation runbooks.
> 5. Local machine - On your local development machine, you can use the task scheduler for your operating system (cron on Linux, Task Scheduler on Windows) to automate running your script periodically.
> 
> Some factors to consider are your script's resource needs, whether it's long/short running, and your infrastructure requirements. Services like Lambda and SSM Automation are good for simple scheduled scripts, while EC2/Batch may work better for more resource-intensive jobs. 

What do you think? Some solid suggestions there, and certainly running this via a Lambda function is how I was thinking.

As I am an open source guy, lets see what open source options it might suggest.

> what open source options can you suggest for scheduling this python script?

And this is what Q comes back with.

> There are a few good open source options for scheduling Python scripts:
> 
> * Cron: Cron is a standard Unix utility for scheduling jobs. You can configure it to run your Python script on a schedule. It's supported on Linux, macOS, and other Unix-like systems.
> * Celery: Celery is a popular asynchronous task queue/job queue based on distributed message passing. You can use it to schedule and run Python scripts as asynchronous tasks on a schedule.
> * Airflow: Apache Airflow is a platform for authoring, scheduling and monitoring workflows or pipelines. You can define Python scripts as tasks in a DAG (directed acyclic graph) and schedule them to run on a periodic basis.
> * Schedule: The Schedule library allows scheduling Python functions and methods to run on some kind of schedule or timetable. It provides a simple way to schedule scripts without additional infrastructure.
> * Regta: Regta is a Python scheduler focused specifically on scheduling Python code. It offers some advantages over Cron like Python-specific optimizations and features like retries and logging.
> 
> Some factors like your hosting environment, task complexity, and automation needs would determine the best fit. But Cron, Celery, and Schedule provide reliable open source options for basic scheduled scripting tasks.





**Conclusions**

I found using Amazon Q in VSCode very easy to use, and I loved the natural flow of prompt/response and how this allowed me to build up the code over steps. It is hard to guess with a simple example like this, but using Amazon Q directly in VSCode helped reduce the friction in this use case. I didn't need to use a browser search tool or StackOverflow (which is typically how I have undertaken these kinds of tasks), and was able to just flow between the chat window and the editor. It saved me a lot of time and effort, and I estimate that I easily did this in a about 25% of the time it would normally take.
I am still learning how to best use tools like Amazon Q in my daily workflow. If you are trying this out for yourself, here are a few things that I found helpful to know.

* Ensure that you start your project in your IDE so that Amazon Q has some context to begin with. This is not necessarily useful at the beginning, but as you start building on your project, it ensures that the suggestions build upon what you already have. In VSCode, the open files you have are important
* Sometimes you will get helpful information when all you want to see is the code, make sure you experiment with various prompts to get this. I found using "show me the code please" worked well of the time
* Amazon Q is a great debugging tool, and I was able to efficiently go from problem to solution. It is surprising how many small errors creep into writing small code like this, so being able to quickly address these saves time.


I will be back again with part two of this post, where I take this script and use Amazon Q to help me schedule this on a weekly basis. Stay tuned, and give Amazon Q a try in your favourite IDE.
