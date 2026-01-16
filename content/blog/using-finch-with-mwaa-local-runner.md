+++
title = "Using Finch to run Apache Airflow using mwaa-local-runner"
date = 2024-02-12
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://community.aws/content/2cGp3ztpb3XLW2P2QsMi7IO011h/running-mwaa-local-runner-with-finch"
+++

> I show you how you can use the Finch to run Apache Airflow using the mwaa-local-runner tool, and how you can do this for your applications too

As some of you may know, I have been creating content on Apache Airflow for a few years now. One of the open source projects that AWS has produced to make it easier for developers to get started with Apache Airflow, is [mwaa-local-runner](https://github.com/aws/aws-mwaa-local-runner). If you have seen me at an event, it is likely you will have seen my live coding/demos, where I use this project. It is awesome!

The thing is, I have just got myself a new Mac (M1 as you asked so nicely), and as I was installing software that I needed, I decided that rather than re-install Docker and Docker Compose, I would make time to get to know Finch. What is Finch I can hear you all asking. [Finch](https://aws.amazon.com/blogs/opensource/introducing-finch-an-open-source-client-for-container-development/) is another open source project from AWS that provides a command line client for building, running, and publishing Linux containers. As I prepare for my talk later this week at a local developer conference, I thought I would put together a quick post on how I updated mwaa-local-runner to use Finch rather than Docker.

**Installing Finch**

[Installing Finch](https://runfinch.com/docs/getting-started/installation/) was very straightforward thanks to the excellent documentation that the community has put together.

With my previous laptop when I was using Docker, I had to start the Docker demon so that I can run the various Docker commands. With Finch, we have to kind of do something similar as we need resources in which to run our containers. This is outlined in the docs very nicely, and I had to run the following commands:

* finch vm init
* finch vm start

Here is the output of the second command, which tells me that we are ready for action.

```
finch vm start
INFO[0000] Starting existing Finch virtual machine...
INFO[0025] Finch virtual machine started successfully
```

**Finch compatibility**

mwaa-local-runner uses a bash script to manage all the various activities that it does (building, starting, cleaning container images) and so the first port of call was to review the script, to see what docker commands it was running, and then review these against the [Finch command line reference guide](https://runfinch.com/docs/cli-reference/finch_build/). Luckily, compatibility with switches within Finch makes it super easy to migrate your containerised build scripts.

Going through this there were a few commands that it looked like I needed to change.

* **docker run = finch run** - the way we run container images in Finch just changes docker for finch, easy peasy!
* **docker build = finch build** - wow, this is too easy
* **docker compose up = finch** compose up - a very straight forward swap, although this was the one I was most concerned about, but I should not have worried though, as the project docs had me covered

> ```
> Containerized applications composed of multiple services are often defined in Docker Compose files. Finch offers a CLI that is compatible to the docker compose cli, therefore commands that you have used previously like docker compose up could be translated to finch compose up.
> ```

As I was looking at some of the commands that were used by the script, many were using command line switches. I wanted to review these to make sure that Finch also supported these. As it turned out, one command line switches used was not supported by Finch.

* **--compress** - this command line option for Docker was [not supported](https://runfinch.com/docs/cli-reference/finch_build/) in the current version of Finch that I was using, so I removed this. Removing it was ok, and the build worked. That does beg the question, what does --compress do, and should I be concerned? Reading [this document](https://www.howtogeek.com/devops/understanding-the-docker-build-context-why-you-should-use-dockerignore/) it looks like --compress helps you improve the build performance. I am not too worried, as I am not planning on building these images frequently, so I think I can live without this option.

**Running my updated script**

Rather than modify the existing script, I created a new one (finch-mwaa-local-runner) and then made my changes. Before I kicked this off though, I went through the specific commands within the script, and ran them in a terminal to make sure they worked.

Building the container image worked a treat, and I had no errors when running this. 

```
finch build --rm -t amazon/mwaa-local:2_7 ./docker
[+] Building 440.9s (25/26)
[+] Building 441.1s (26/26) FINISHED
 => [internal] load build definition from Dockerfile                                                                  0.0s
 => => transferring dockerfile: 1.73kB                                                                                0.0s
 => [internal] load metadata for docker.io/library/amazonlinux:2023                                                   1.4s
 => [internal] load .dockerignore                                                                                     0.0s
 => => transferring context: 2B                                                                                       0.0s
 => [ 1/21] FROM docker.io/library/amazonlinux:2023@sha256:d8323b3ea56d286d65f9a7469359bb29519c636d7d009671ac00b5c12  5.6s
 => => resolve docker.io/library/amazonlinux:2023@sha256:d8323b3ea56d286d65f9a7469359bb29519c636d7d009671ac00b5c12dd  0.0s
 => => sha256:d111cbc02b249a552b77e87298e3df2ce29173bc39b7d82aecba5ca8a2ab06d2 51.32MB / 51.32MB                      4.5s
 => => extracting sha256:d111cbc02b249a552b77e87298e3df2ce29173bc39b7d82aecba5ca8a2ab06d2                             1.0s
 => [internal] load build context                                                                                     0.0s
 ..
 ..
  => [21/21] WORKDIR /usr/local/airflow                                                                                0.0s
 => exporting to docker image format                                                                                 78.7s
 => => exporting layers                                                                                              61.8s
 => => exporting manifest sha256:76739ac599da52b352158076e802f1331eb61c385fdecf20cc0f36728e753478                     0.0s
 => => exporting config sha256:d2afaf67f1dd0022006d153aae0a55d98fbf9fa82e0734386ef613da50d255d2                       0.0s
 => => sending tarball                                                                                               16.9s
Loaded image: docker.io/amazon/mwaa-local:2_7
```

The next test was to actually kick off and run the containers.

```
finch compose -p $PROJECT_NAME -f ./docker/docker-compose-local.yml up
WARN[0000] Ignoring: service local-runner: [EnvFile HealthCheck]
WARN[0000] Ignoring: service local-runner: depends_on: postgres: [Required]
INFO[0000] Ensuring image postgres:11-alpine
INFO[0000] Ensuring image amazon/mwaa-local:2_7
INFO[0000] Re-creating container aws-mwaa-local-runner-2_7-postgres-1
INFO[0000] Re-creating container aws-mwaa-local-runner-2_7-local-runner-1
INFO[0000] Attaching to logs
..
..
```
Eventually, the start process failed with the following:

```
postgres-1     |chown: /var/lib/postgresql/data: Permission denied
postgres-1     |chown: /var/lib/postgresql/data/pg_multixact: Permission denied
local-runner-1 |Mon Feb 12 13:08:13 UTC 2024 - postgres:5432 still not reachable, giving up
INFO[0183] Container "aws-mwaa-local-runner-2_7-local-runner-1" exited
INFO[0183] All the containers have exited
INFO[0183] Stopping containers (forcibly)
INFO[0183] Stopping container aws-mwaa-local-runner-2_7-postgres-1
INFO[0183] Stopping container aws-mwaa-local-runner-2_7-local-runner-1
```

I was getting hundreds of permissions errors. Oh no, I knew this was going too well. Looking at the current issues within the Finch GitHub repo, I found an [issue](https://github.com/runfinch/finch/issues/131)  that I thought would help resolve this problem. Looking at this I created a new docker-compose file to take into consideration some of the comments, as well as adding a new step.

First I needed to create a volume with the Finch cli

```
finch volume create pgdata
```

And then modify the docker file. I used this opportunity to rename my configuration files. I created finch-local.yml and finch-resetdb.yml, and this is what they looked like:

```
version: '3.7'
services:
    postgres:
        image: postgres:11-alpine
        environment:
            - POSTGRES_USER=airflow
            - POSTGRES_PASSWORD=airflow
            - POSTGRES_DB=airflow
            - PGDATA=/var/lib/postgresql/data
        logging:
            options:
                max-size: 10m
                max-file: "3"
        volumes:
            - pgdata:/var/lib/postgresql/data:rw

    local-runner:
        image: amazon/mwaa-local:2_7
        restart: always
        depends_on:
            - postgres
        environment:
            - LOAD_EX=n
            - EXECUTOR=Local
        logging:
            options:
                max-size: 10m
                max-file: "3"
        volumes:
            - "/Users/ricsue/Projects/airflow-101/workflow/dags:/usr/local/airflow/dags"
            - "/Users/ricsue/Projects/airflow-101/workflow/plugins:/usr/local/airflow/plugins"
            - "/Users/ricsue/Projects/airflow-101/workflow/requirements:/usr/local/airflow/requirements"
            - "${PWD}/startup_script:/usr/local/airflow/startup"
        ports:
            - "8080:8080"
        command: local-runner
        healthcheck:
            test: ["CMD-SHELL", "[ -f /usr/local/airflow/airflow-webserver.pid ]"]
            interval: 30s
            timeout: 30s
            retries: 3
        env_file:
            - ./config/.env.localrunner
volumes:
    pgdata:

```

**mwaa-local-runner now runs on Finch**

Re-trying this showed that it looked good to go now.

```
local-runner-1 |Mon Feb 12 13:19:58 UTC 2024 - waiting for Postgres... 1/20
postgres-1     |sh: locale: not found
postgres-1     |2024-02-12 13:19:58.329 UTC [31] WARNING:  no usable system locales were found
postgres-1     |The files belonging to this database system will be owned by user "postgres".
postgres-1     |This user must also own the server process.
postgres-1     |
postgres-1     |The database cluster will be initialized with locale "en_US.utf8".
postgres-1     |The default database encoding has accordingly been set to "UTF8".
postgres-1     |The default text search configuration will be set to "english".
postgres-1     |
postgres-1     |Data page checksums are disabled.
postgres-1     |
postgres-1     |fixing permissions on existing directory /var/lib/postgresql/db/pgdata ... ok
postgres-1     |creating subdirectories ... ok
postgres-1     |selecting default max_connections ... 100
postgres-1     |selecting default shared_buffers ... 128MB
postgres-1     |selecting default timezone ... UTC
postgres-1     |selecting dynamic shared memory implementation ... posix
postgres-1     |creating configuration files ... ok
postgres-1     |running bootstrap script ... ok
postgres-1     |performing post-bootstrap initialization ... ok
```

I was then greeted with the familiar Airflow ascii graphics that showed me that I was good to go. Testing in a local browser confirmed that I was now running mwaa-local-runner using Finch.

**Fixing the bootstrap.sh**

As is always the way, just when you think you have cracked it, a problem appears. As it turns out, when I went to test a simple DAG (one that calls the AWS cli, doing an aws sts get-caller-identity command) the task failed with the following error:

```
/lib64/ld-linux-x86-64.so.2: No such file or directory
```

Initially when I looked at this error, something was off - I am running on an aarch64 not an amd64 processor. Searching for possible answers took me down several rabbit holes and wasted a lot of time before I realised what it was. The current **bootstrap.sh** script that is used when building the Airflow container contained the following entry:

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o $zip_file
```
So it was always trying to install amd64 binaries, despite me building this on an aarch64. To fix this, I modified the script as follows:

```
if [[ $(uname -p) == "aarch64" ]]; then
  curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o $zip_file
else
  curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o $zip_file
fi
```

So that whether I am using an intel based or arm based system, it will pick up the right AWS cli to install.

**MySQL Provider**

The next issue I bumped into was that when trying to run a task using the MySQL Operator, I encountered the following error:

```
No module named 'MySQLdb'
```

This time searching provided more helpful, sort of. In [this](https://github.com/apache/airflow/discussions/25831) I found out that using the MySQL Operator on my local aarch64 based mac was not going to work. There was probably some work I could do to work around this, but it seemed a better approach to switch to using PostgreSQL instead.

**Accessing the local host**

The final thing that I needed to figure out was how to access services that were running on my local machine. Docker surfaces up **host.docker.internal** which you can use within processes within your container to connect to external services running on the host (i.e. my mac). It took my a while to find this, but when using Finch, you can do the same thing by using **192.168.5.2**. 

**Open Source is awesome!**

I hope this post was useful, and that for those of you who are looking to use open source tools like Finch to manage your container development processes, you will get some ideas of how easy it can be. I have created a [GitHub repo](https://github.com/094459/finch-local-runner) that shares the configuration files I used to get mwaa-local-runner to work with Finch.

If you found this post useful, please provide me [feedback](https://pulse.aws/survey/BX1EMQNI). I use this feedback to help me improve my content, but also to know what content to write about. Thank you so much!
