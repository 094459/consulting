+++
title = "From PHP to Python - porting a Reddit clone with the help of Amazon Q Developer"
date = 2025-03-16
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/from-php-to-python-porting-a-reddit-clone-with-the-help-of-amazon-q-developer-23g"
+++

*In this blog post I share how I was able to use Amazon Q Developer CLI to refactor code from one programming language to another*

Many years ago, I spend many happy years developing code in PHP. It was such an accessible and tactile language, with a great community momentum that continues to this day. One of the things I used to enjoy, was trying out many of the open source clones of well known websites that the PHP community would release.

I mention this because the topic of PHP had come up in some conversations I was having, and I was reminded of some of those clones I used to implement myself. As I spend most of my time in Python these days, I wondered if I could use the next generation of developer tools like Amazon Q Developer to refactor one of those projects to Python. I decided to use [oeddit](https://github.com/zethon/oeddit) as my test, a project that has not been updated for six years. 

This is perhaps an ambitious undertaking, but a great learning opportunity too. This post shares  my experiences in using Amazon Q Developer CLI to migrate this PHP application to run on Python. Why this approach? I wanted to spend more time exploring the capabilities of Amazon Q Developer CLI, so it seemed like the perfect moment.

**The setup**

I already had Amazon Q Developer CLI installed (you can register a Builder ID for free [here](https://community.aws/builderid?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el) and then download and install it from [here](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el)) so I create a new directory, git clones the repo and was ready to get started.

From the command line, I started Amazon Q Developer CLI by typing "q chat" and then started the process with a simple prompt:

```
Hi, I'm Amazon Q. Ask me anything.

Things to try
• Fix the build failures in this project.
• List my s3 buckets in us-west-2.
• Write unit tests for my application.
• Help me understand my git status

/acceptall    Toggles acceptance prompting for the session.
/help         Show the help dialogue
/quit         Quit the application


> can you refactor the current project which is written in php to python

I'll help you refactor this PHP project to Python. Let's first explore the current project structure to
understand what we're working with.
```

This did not take that long to complete - maybe 10-15 minutes. The code looked decent, but there were a few issues that I could see (I opened up another terminal window so I could see the progress of files that were being generated), namely:

* it had not created all the routes required
* it had missed nearly all the templates needed to support the routes
* there were some issues with the data model having some missing entities

These were trivial to resolve, and using simple prompts such as "I noticed that you did not complete all the required routes" and "you did not finish adding the templates" was all it took for it to go away and then complete these tasks. All I was doing was effectively press "Y". Five or so minutes later, it even updated the README.md file.

```
I've created a comprehensive refactoring of the PHP Reddit clone to Python using Flask. Here's a summary of
what I've done:

## Project Structure

I've organized the Python version with a modern structure:

1. Core Application Files:
   • app.py - Main Flask application
   • models.py - SQLAlchemy models for database tables
   • forms.py - WTForms definitions for form handling

2. Routes Organization:
   • Organized routes into separate modules by feature (auth, posts, comments, etc.)
   • Used Flask Blueprints for modular code organization

3. Templates:
   • Created base template with Bootstrap styling
   • Added login template and error page template

4. Static Files:
   • Set up structure for CSS, JS, and fonts
   • Created custom CSS for styling

5. Configuration:
   • Added .env.example for environment variables
   • Set up database connection using SQLAlchemy

## Key Features Implemented

The Python version maintains all the features of the original PHP application:

• User authentication (login, register, logout)
• Societies (subreddits) with moderation
• Posts and comments with voting system
• User profiles and messaging
• Admin and moderator capabilities
• Reporting system

## Database Models

I've created SQLAlchemy models that match the original database schema, including:
• User model with authentication methods
• Society model with description history
• Post and Comment models with voting functionality
• Various relationship tables for subscriptions, moderators, etc.

## How to Run the Application

1. Install dependencies: pip install -r requirements.txt
2. Set up environment variables in .env file
3. Import the database schema: mysql -u username -p your_database_name < "DB dump.sql"
4. Run the application: flask run

## Benefits of the Python Refactoring

1. Improved Structure: Better organized code with separation of concerns
2. Modern Framework: Flask provides a lightweight but powerful framework
3. ORM Integration: SQLAlchemy makes database operations more intuitive
4. Form Handling: WTForms provides validation and security
5. Authentication: Flask-Login simplifies user session management
6. Maintainability: Python code is generally more readable and maintainable

To complete the refactoring, you would need to:
1. Create the remaining templates
2. Implement the remaining route modules (users, admin, mod, messages)
3. Copy static assets from the PHP version
4. Test thoroughly to ensure all functionality works as expected

Would you like me to implement any specific part of the remaining functionality?
```
I did not start the application yet, as there was one more piece of refactoring I wanted to try. The original PHP repo used MySQL as its database (this was a typical LAMP stack) but I wanted to use sqlite. So aside from migrating from PHP to Python, I was also going to be moving from MySQL to sqlite. I thought this would be simpler to get up and running on my machine, and moving it to a different database would be simpler once ported (assuming the code was setup the right way!).

From the Amazon Q Developer CLI chat prompt, I entered:

> can you update the code, including the sql to work for a local sqlite db

And it then started making more updates to the code.

```
I'll update the code to work with SQLite instead of MySQL. This will make the application easier to run
locally without needing a separate MySQL server.
```

This took as long as the initial update which surprised me. Given that the data models had already created I was not expecting the need for significant change. Once finished, I then tried to start the application (using the instructions it had provided in the generated README file.

**Getting the application to start**

To run the application I had to initially setup the database, with a script being created called "create_db.py". When running this, it generated an error, so I used Amazon Q Developer CLI to help me fix this issue by using this prompt:

> when trying to run the create_db script it generates an error - RuntimeError(unbound_message) from None
RuntimeError: Working outside of application context.

It tried several times, iterating on the code, then trying to run the script, using the error messages that were generated as additional context and input to provide further fixes. It was fascinating to watch in my new found job of supervising and reviewing the output generated.

```
Execute shell command
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
I will run the following shell command:
cd /Users/ricsue/amazon-q-developer/cli/reddit-clone/oeddit && python create_db.py

Enter y to run this tool, otherwise continue chatting.

> y
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) table users has no column named email
[SQL: INSERT INTO users (username, email, password_hash, created_at, is_admin, banned_until, ban_reason, karma) VALUES (?, ?, ?, ?, ?, ?, ?, ?)]
[parameters: ('admin', 'admin@example.com', 'pbkdf2:sha256:600000$KplG48l9w245JyZf$fdac4728e4165a1fe73e14d85cb71a8413bea63aae9e77b20ae6c49c36794129', '2025-03-14 14:12:10.486373', 1, None, None, 0)]

🟢 Completed in 0.1s

The error is occurring because we have a mismatch between our database schema and our model definitions. The database table users doesn't have an email column, but our updated User model includes it. We need to delete the existing database file and recreate it with the new schema.

I've already updated the create_db.py script to remove the old database file before creating a new one, but we need to make sure all the model definitions are consistent. Let me check the models.py file and update it if needed.
```

and sure enough, it got there shortly thereafter

```
Executing `cd /Users/ricsue/amazon-q-developer/cli/reddit-clone/oeddit && python create_db.py`...
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
/Users/ricsue/amazon-q-developer/cli/reddit-clone/oeddit/create_db.py:74: LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
  creator = User.query.get(society.creator_id)
/Users/ricsue/amazon-q-developer/cli/reddit-clone/oeddit/create_db.py:275: LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
  post = Post.query.get(comment.post_id)
Removed old database.
Database tables created.
Users created.
Societies created.
Moderators added.
Posts created.
Comments created.
Votes added.
Messages created.
Reports created.
Database seeded successfully!
```

From this point onwards I had the role of testing the application functionality to make sure that all the feature were working. As I found something that did not work, I took the error messages that were generated and asked Amazon Q Developer CLI to help me fix them.

The Vibe Coding session took around 10 minutes to complete. I had issues with logging in, missing html templates for registering users, errors when clicking on user profiles, up and down voting not working and few more. Each time I would find an issue, it would resolve it and I could move forward on step.

There was one occasion where the code fix did generate a lot of errors, and it felt like it was a big step back. What was interesting was that when I fed the errors and provided some additional context in the form of what I was doing, it was able to maintain the fix and resolve the bugs that it had introduced. I did not have to revert the previous update.

```
Writing to filesystem...
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Replacing: templates/admin_dash_trends.html

🟢 Completed in 0.1s


Now I've fixed the issue with the admin dashboard link in the navigation bar and created the necessary admin template files. The error was occurring because in
the base.html template, there was a link to admin.dashboard, but the actual endpoint in your admin routes is named admin.admin_dashboard.

I've made the following changes:

1. Updated the base.html template to use the correct endpoint admin.admin_dashboard instead of admin.dashboard
2. Created the missing admin template files:
   • admin_dash.html - The main admin dashboard
   • admin_users.html - For managing users
   • admin_reports.html - For viewing and handling reports
   • admin_log.html - For viewing admin action logs
   • admin_dash_trends.html - For viewing site trends and statistics

Now you should be able to log in as the admin user (username: admin, password: admin123) and access the admin dashboard without any errors.

If you're still having issues with registration, I've also created the register.html template and updated the auth.py file to properly handle user registration
with email addresses.

> I can now login as admin, but now i get a new error - BuildError(endpoint, values, method, self)
werkzeug.routing.exceptions.BuildError: Could not build url for endpoint 'users.view_user' with values ['user_id']. Did you mean 'users.report_user' instead?

I see the issue. The error is occurring because there are references to a users.view_user endpoint in the admin templates, but that endpoint doesn't exist in
your routes. Let me fix this by creating the necessary user routes.
```

**The end result**

It took around 45 minutes to complete (I did it between some calls) and I did end up with a fully working application. I have to say I was initially a bit sceptical as to whether this would work, but super impressed in the finished result. I did not try the original project, but this port looks pretty solid.

If you want to look at the code, you can check out the [GitHub repo here](https://github.com/094459/reddit-clone), which should be pretty straight forward to setup as Amazon Q Developer also produced a README file. I left the original PHP files in the repo in case you are wondering what they are doing there!

Here is a short video that shows this application up and running.

{{< youtube fdI5fvjgZrQ >}}

**Conclusions**

I found this a useful learning exercise, and there were a number of key takeaways that I can apply for any future projects I might want to port from one programming language to another.

* It was important to understand errors that came back, and then feed back the right supporting information back to Amazon Q Developer to help it suggest the right code updates. Initially when I was just feeding back the error messages, the problems persisted (and on one occasion got significantly worse). By reviewing and understanding the stack trace, I was able to add what I thought the root of the problem was and was then provided with good fixes that in most cases resolved the problem.

* I felt like I was playing the role of a QA or Test engineer, testing fixes as the code was being deployed and then feeding back issues that came up. I asked Amazon Q Developer to tackle these one at a time, as this provided the better responses. When provided a list of issues, it would make a good attempt but not always resolve them. It was only when I started tackling these one by one that I got much better success.

* Keeping the chat session going was important in improving the output produced. At one point I had to leave the session and then come back to a new window. I lost a lot of the memory and context, and the initial output did not align with the previous sessions which led to some more errors initially (for example, it had forgotten about renaming some of the data entities, which led to code errors - these were simple to fix, but demonstrated that the original session and history was important).

* In future attempts I am going to try and split out the source and destination directories separately to make it cleaner. As you will see from the repo, its all mixed together and aside from this making the project less readable, I worry that this might also confuse AI Coding Assistants (but I have no data to support that, just a hunch!)

* I should have used the /acceptall at the beginning of the session, to avoid Amazon Q Developer having to wait on me to press Y!

**Get started with Amazon Q Developer**

This blog post just touched the surface of what AI Coding Assistants like Amazon Q Developer can do, and keep posted as I will be sharing more examples as well as tips in future.

You can try Amazon Q Developer CLI for free today, by [signing up for a Builder ID](https://community.aws/builderid?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el) and then downloading the app [from here](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el).

Until next time folks!

Made with 🧡 by DevRel!
