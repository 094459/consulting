+++
title = "Running Model Context Protocol (MCP) Servers on containers using Finch"
date = 2025-05-02
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/running-model-context-protocol-mcp-servers-on-containers-using-finch-kj8"
+++

I was chatting with AWS Hero Matt Lewis on the topic of how to run MCP Servers via a container image, and realised that I had not actually tried this yet. So this post was inspired by that conversation, and I hope it helps anyone else who is looking to try it out.  In a previous post I introduced how Amazon Q CLI now supports Model Context Protocol (MCP) (check out [Configuring Model Context Protocol (MCP) with Amazon Q CLI](https://dev.to/aws/configuring-model-context-protocol-mcp-with-amazon-q-cli-e80) for more details). 

This post will build on that and show you how to run MCP Servers via container images. As I switched to using Finch from Docker back in 2024, I will be using that - this means if you are using something different to Docker, like Podman for example, you should be able to follow along and use that tool too.

**Refresh of how to connect to MCP Servers**

When looking to integrate with MCP Servers, you can integrate locally (what is referred to as STDIO), or you can connect to remote MCP servers (over either Server-Sent Events, SSE, or the new Streamable HTTP - but I will not be covering those in this post). 

I have seen two common ways that people are integrating MCP Servers using STDIO: they are either installing/running libraries or executables, or they are running the same libraries/executables but through a container image. Most of the examples (including my original post) showed the first way (running direct libraries). You might be thinking why would you use one method over another. In my previous post I shared that if you run MCP Servers locally you need to make sure that you meet all the dependencies. You might encounter some MCP Servers that have a lot of dependencies (libraries, binaries, etc) or maybe dependencies that clash with your setup. In these circumstances then running those MCP Servers in a container is probably a good approach.

**Integrating the GitHub MCP Server**

Announced a few weeks ago, the [GitHub MCP Server](https://github.com/github/github-mcp-server) allows you to get additional context from any GitHub repo, providing details about those repos such as commits, issues, pull requests and more.

If I want to add this to the list of MCP Servers I use in my Amazon Q CLI sessions, then I can add the following to my mcp.json file

```
      "github-mcp-server": {
        "command": "finch",
        "args": [
          "run",
          "--rm",
          "--interactive",
          "--env",
          "GITHUB_PERSONAL_ACCESS_TOKEN",
          "ghcr.io/github/github-mcp-server"
        ],
        "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": "addyourtoken"}
      }
```

You will need to update your mcp.json file to include your GitHub token before you are able to run this. 

> As you can see, pretty straight forward. As I am using Finch, I need to make sure that I have started it (finch vm start) and review and adjust the command line arguments as needed. If you are using something different (like Podman) these might be different. Typically you will find the arguments for Docker used, but these should be easy enough to update.

Once you have updated and saved the file, when you next start Amazon Q CLI and then review the available tools, you should see the new entries from the GitHub MCP Server.

```
> /tools

Tool                                                        Permission
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Built-in:
- fs_write                                                  * not trusted
- fs_read                                                   * trusted
- report_issue                                              * trusted
- use_aws                                                   * trust read-only commands
- execute_bash                                              * trust read-only commands

github_mcp_server (MCP):
- github_mcp_server___list_branches                         * not trusted
- github_mcp_server___get_pull_request                      * not trusted
- github_mcp_server___update_issue                          * not trusted
- github_mcp_server___create_issue                          * not trusted
- github_mcp_server___push_files                            * not trusted
- github_mcp_server___get_issue                             * not trusted
- github_mcp_server___get_commit                            * not trusted
- github_mcp_server___get_pull_request_comments             * not trusted
- github_mcp_server___get_pull_request_status               * not trusted
- github_mcp_server___search_users                          * not trusted
- github_mcp_server___create_pull_request                   * not trusted
- github_mcp_server___get_me                                * not trusted
- github_mcp_server___list_code_scanning_alerts             * not trusted
- github_mcp_server___update_pull_request                   * not trusted
- github_mcp_server___get_pull_request_files                * not trusted
- github_mcp_server___search_issues                         * not trusted
- github_mcp_server___get_issue_comments                    * not trusted
- github_mcp_server___list_secret_scanning_alerts           * not trusted
- github_mcp_server___add_pull_request_review_comment       * not trusted
- github_mcp_server___get_secret_scanning_alert             * not trusted
- github_mcp_server___list_commits                          * not trusted
- github_mcp_server___fork_repository                       * not trusted
- github_mcp_server___update_pull_request_branch            * not trusted
- github_mcp_server___create_repository                     * not trusted
- github_mcp_server___get_pull_request_reviews              * not trusted
- github_mcp_server___merge_pull_request                    * not trusted
- github_mcp_server___list_issues                           * not trusted
- github_mcp_server___get_code_scanning_alert               * not trusted
- github_mcp_server___add_issue_comment                     * not trusted
- github_mcp_server___search_code                           * not trusted
- github_mcp_server___get_file_contents                     * not trusted
- github_mcp_server___create_pull_request_review            * not trusted
- github_mcp_server___create_branch                         * not trusted
- github_mcp_server___create_or_update_file                 * not trusted
- github_mcp_server___search_repositories                   * not trusted
- github_mcp_server___list_pull_requests                    * not trusted
```

**AWS MCP Servers**

In my original post I showed integrating a number of the [AWS MCP Servers](https://github.com/awslabs/mcp), using the libraries that have already been published to PyPi. But perhaps you might want to review/update these MCP servers slightly. Building and then running them via containers might be a good option for you then. This is also pretty straight forward.

> As of writing, the AWS MCP Servers are not available on any of the main public container image repositories

The AWS MCP Servers repo contains a src directory for each MCP Server. If I wanted to run say the "cost-analysis-mcp-server" MCP Server, then all I need to do is:

1. Check out the full repo into my local workspace
2. Go into the source directory (so in this case, this is src/cost-analysis-mcp-server
3. Build the container image (using the command "finch build -t awslabs/cost-analysis-mcp-server ." (and then perhaps push this to your preferred container image repository)
4. Update the mcp.json figure to point to this local container image - this is the one I used

```
      "awslabs.cost-analysis-mcp-server": {
        "command": "finch",
        "args": [
          "run",
          "--rm",
          "--interactive",
          "--env",
          "FASTMCP_LOG_LEVEL=ERROR",
          "awslabs/cost-analysis-mcp-server"
         ],
         "env": {}
        }
```

And when I run Amazon Q CLI, I can see that I now have these tools available to me.

```
> /tools

Tool                                                        Permission
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔Built-in:
- fs_read                                                   * trusted
- report_issue                                              * trusted
- execute_bash                                              * trust read-only commands
- fs_write                                                  * not trusted
- use_aws                                                   * trust read-only commands

awslabscost_analysis_mcp_server (MCP):
- awslabscost_analysis_mcp_server___get_pricing_from_api    * not trusted
- awslabscost_analysis_mcp_server___get_pricing_from_web    * not trusted
- awslabscost_analysis_mcp_server___get_bedrock_patterns    * not trusted
- awslabscost_analysis_mcp_server___generate_cost_report    * not trusted
- awslabscost_analysis_mcp_server___analyze_cdk_project     * not trusted
```

**Get started with Amazon Q CLI**

This was a quick post that showed you how you can run MCP Servers from container images, and how to configure Amazon Q CLI to use them - whether you use Docker, Finch, or Podman. 

I hope this blog post has inspired you to want to try Amazon Q CLI for yourself. You can try it for free by [signing up for a Builder ID](https://community.aws/builderid?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el) and then downloading the app [from here](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el).

Until next time folks!

Made with 🧡 by DevRel!
