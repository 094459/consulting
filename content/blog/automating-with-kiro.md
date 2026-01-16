+++
title = "Automating made easy with Kiro CLI"
date = 2025-12-10
draft = false
tags = []
categories = ["Technical"]
canonicalUrl = "https://dev.to/aws/automating-made-easy-with-kiro-cli-1p78"
+++

## What are you automating with generative AI ?

I have spoken at many events this year sharing how I see developers using AI coding assistants like [Kiro]( https://kiro.dev/downloads/?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el) and [Kiro CLI](https://kiro.dev/cli/?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el). The top use case was debugging code, and I wrote about that in [Debugging and troubleshooting issues with AI coding assistants](https://dev.to/aws/debugging-and-troubleshooting-issues-with-kiro-cli-and-amazon-q-developer-40ae). In this post I am going to talk about another very common use case, automation. I will share a couple of things that I found trivial to automate with the help of Kiro, but also some unexpected things I learned along the way.

## Automating tasks

AI Coding tools have lowered the barrier to automation. In the past we might have spent time trying to decide what is worth automating, and if we then did spend time, we would create automation that was perhaps a little basic in functionality and rough around the edges. Those days are gone, and I want to share some recent examples of what I mean.

### Fixing links

Some of you might know that I do a regular open source newsletter (you can find the list of issues [here](https://dev.to/aws/aws-open-source-news-and-updates-reference-5clm)) and I have used my own hosted URL tracking tool to help me understand what the community is interested in. I have over 300 posts written over the past five years, with over 6.5K links tracked. I recently made the decision to switch to a different URL tracking tool, and needed an efficient way to update those. 

What made this automation more challenging is that I publish to two sites: dev.to and my own personal blog at [https://blog.beachgeek.co.uk](https://blog.beachgeek.co.uk/), and so I needed to come up with two different automation approaches.  The first tool that Kiro CLI created for me was a search/replace function, that had a bunch of stuff to support the safe updating. It was pretty straight forward, and I had a comprehensive tool up and running in less than 30 minutes.

The dev.to automation was also trickier because I was going to be using the [dev.to API](https://developers.forem.com/api/v1) to make changes, so I was super nervous that the code might make a hash of things and render the content useless.  You do need to generate an API key to access those APIs though.  I found sketching and providing an outline of how the automation works was a good first step before using something like Kiro CLI to actually generate the automation. This will become the outline it will follow, so I thought about what I needed and what the flow would be like:

- Generate a file that contained all the tracked links, and provide a replacement - this would be used as the source file to control the automation (in the end I created a simple csv file with source and update columns to reflect the update I wanted)

```
def load_link_mappings(self):
        """Load link mappings from CSV file"""
        try:
            with open(CSV_FILE, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 2:
                        old_link = row[0].strip().rstrip('/')
                        new_link = row[1].strip()
                        self.link_mappings[old_link] = new_link
            logging.info(f"Loaded {len(self.link_mappings)} link mappings")
        except FileNotFoundError:
            logging.error(f"CSV file {CSV_FILE} not found")
            sys.exit(1)
```

- Review all the blog posts, and for each blog posts, review for any links - build a map of the blog posts that might need to be updated

```
def find_links_to_replace(self, markdown_content):
        """Find markdown links that need replacement"""
        # Regex to find markdown links [text](url)
        link_pattern = r'\[([^\]]*)\]\(([^)]+)\)'
        matches = re.findall(link_pattern, markdown_content)
        
        print(f"  DEBUG: Found {len(matches)} markdown links")
        print(f"  DEBUG: Have {len(self.link_mappings)} mappings in CSV")
        
        replacements = []
        for i, (text, url) in enumerate(matches):
            print(f"  DEBUG: Link {i+1}: {url}")
            if url in self.link_mappings:
                print(f"  DEBUG: MATCH FOUND for {url}")
                replacements.append({
                    'old_url': url,
                    'new_url': self.link_mappings[url],
                    'text': text,
                    'full_match': f'[{text}]({url})'
                })
            else:
                print(f"  DEBUG: No match for {url}")
        
        return replacements
```

- Find and update matching links - using my source file that was generated, find and update any matches

```
   def update_article_content(self, article_id, new_content):
        """Update article with new content"""
        url = f"{API_BASE_URL}/articles/{article_id}"
        data = {
            "article": {
                "body_markdown": new_content
            }
        }
        
        response = requests.put(url, headers=self.headers, json=data)
        return response.status_code == 200
```

- Track activity of the automation tool - as updates are made, log each update in a log file and keep a backup of the original just in case I need to revert back
- Sign off - for each blog post updated, provide a review of what changes you plan to make and get confirmation to make the change

```
def process_articles(self, dry_run_only=False, article_url=None):
        """Main processing function"""
        if dry_run_only:
            return self.dry_run(article_url)
            
        # First, run dry run
        has_changes = self.dry_run(article_url)
        
        if not has_changes:
            print("\nNo changes found. Exiting.")
            return
            
        # Ask for confirmation to proceed
        print(f"\nProceed with updates? (y/N): ", end="")
        if input().strip().lower() != 'y':
            print("Operation cancelled.")
            return
        
        # Now perform actual updates
        print(f"\n{'='*80}")
        print("PERFORMING ACTUAL UPDATES")
        print(f"{'='*80}")
        
        self.load_link_mappings()
        
        if article_url:
            articles = self.get_article_by_url(article_url)
            if not articles:
                return
        else:
            articles = self.get_all_articles()
        
        updated_count = 0
        
        for i, article in enumerate(articles, 1):
            article_id = article['id']
            title = article['title']
            
            print(f"\nProcessing article {i}/{len(articles)}: {title}")
            
            # Get full article details
            full_article = self.get_article_details(article_id)
            if not full_article or 'body_markdown' not in full_article:
                print("  No markdown content found")
                continue
                
            markdown_content = full_article['body_markdown']
            
            # Count all links in the post
            all_links = re.findall(r'\[([^\]]*)\]\(([^)]+)\)', markdown_content)
            print(f"  Found {len(all_links)} total links in post")
            
            replacements = self.find_links_to_replace(markdown_content)
            print(f"  Found {len(replacements)} links to update")
            
            if not replacements:
                continue
                
            print(f"\nUpdating: {title}")
            
            # Apply replacements
            updated_content = markdown_content
            for replacement in replacements:
                old_link = f"[{replacement['text']}]({replacement['old_url']})"
                new_link = f"[{replacement['text']}]({replacement['new_url']})"
                updated_content = updated_content.replace(old_link, new_link)
            
            # Update the article
            if self.update_article_content(article_id, updated_content):
                updated_count += 1
                logging.info(f"Updated article '{title}' (ID: {article_id})")
                for replacement in replacements:
                    logging.info(f"  Replaced: {replacement['old_url']} -> {replacement['new_url']}")
                print(f"  ✓ Successfully updated")
            else:
                logging.error(f"Failed to update article '{title}' (ID: {article_id})")
                print(f"  ✗ Failed to update")
        
        logging.info(f"Process complete. Updated {updated_count} articles.")
        print(f"\n{'='*80}")
        print(f"COMPLETED: Updated {updated_count} articles")
        print(f"{'='*80}")
```

As I was orchestrating this code, I realised I needed to add the capability to run the script in non destructive mode, and Kiro quickly added this as a new command switch:

```
    def dry_run(self, article_url=None):
        """Perform a dry run to show all planned changes"""
        self.load_link_mappings()
        
        if article_url:
            articles = self.get_article_by_url(article_url)
            if not articles:
                return False
        else:
            articles = self.get_all_articles()
        
        total_articles_with_changes = 0
        total_replacements = 0
        
        print(f"\n{'='*80}")
        print("DRY RUN - Showing all planned changes")
        print(f"{'='*80}")
        for i, article in enumerate(articles, 1):
            article_id = article['id']
            title = article['title']
            
            print(f"\nProcessing article {i}/{len(articles)}: {title}")
            
            # Get full article details
            full_article = self.get_article_details(article_id)
            if not full_article or 'body_markdown' not in full_article:
                print("  No markdown content found")
                continue
                
            markdown_content = full_article['body_markdown']
            
            # Count all links in the post
            all_links = re.findall(r'\[([^\]]*)\]\(([^)]+)\)', markdown_content)
            print(f"  Found {len(all_links)} total links in post")
            
            replacements = self.find_links_to_replace(markdown_content)
            print(f"  Found {len(replacements)} links to update")
            
            if not replacements:
                continue
                
            total_articles_with_changes += 1
            total_replacements += len(replacements)
            
            print(f"ID: {article_id}")
            print(f"URL: https://dev.to/{article.get('path', '')}")
            
            for j, replacement in enumerate(replacements, 1):
                print(f"  {j}. '{replacement['text']}'")
                print(f"     FROM: {replacement['old_url']}")
                print(f"     TO:   {replacement['new_url']}")
        
        print(f"\n{'='*80}")
        print(f"DRY RUN SUMMARY:")
        print(f"  Articles with changes: {total_articles_with_changes}")
        print(f"  Total link replacements: {total_replacements}")
        print(f"{'='*80}")
        
        return total_articles_with_changes > 0
```
This ended up being super useful as it allowed me to test updates before doing this in real mode. 

I then wanted to update the code so that as it was replacing the URL back to the original, that it checked to make sure that the original link was still valid. Whilst this would not necessarily change anything (the tracking link would be currently failing), it would allow me to check those links. As it turns out I only had a few to deal with:

```
2025-10-29 09:15:20,050 - INFO - Loaded 5948 link mappings
2025-10-29 09:15:29,951 - INFO - Found 333 articles
2025-10-29 09:15:30,368 - ERROR - Failed to get article 1765341: 404
2025-10-29 09:15:30,588 - ERROR - Failed to get article 572590: 404
2025-10-29 09:17:34,035 - ERROR - Failed to get article 474840: 429
2025-10-29 09:17:56,117 - ERROR - Failed to get article 228401: 429
```

It was at this point I then decided I need to add the capability to just make one specific update, rather than looking through all 330+ blog posts, which would allow me to minimise the blast radius of any issue.

```
    def get_article_by_url(self, article_url):
        """Get article by dev.to URL"""
        # Extract username and slug from URL like https://dev.to/username/slug
        url_parts = article_url.rstrip('/').split('/')
        if len(url_parts) < 2:
            logging.error(f"Invalid URL format: {article_url}")
            return None
            
        username = url_parts[-2]
        slug = url_parts[-1]
        
        url = f"{API_BASE_URL}/articles/{username}/{slug}"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return [response.json()]  # Return as list for consistent processing
        else:
            logging.error(f"Failed to get article from URL {article_url}: {response.status_code}")
            return None
```

After running this initially on one post (first in dry run and then in full update mode), I was confident it would work. I checked dev.to and I noticed that all that changed on the post was that it was now updated to reflect the edit ("Edited on....").

This sounds like a lot of effort and work, but the total time take was around two hours. When I consider the alternative options, this could easily take a few days of work to make the same changes.

### GitHub Stats

I also create a number of hands on tutorials and workshops on GitHub, and need to keep a track of who is using them. GitHub limits you to only 14 days of traffic data, and I needed a way of capturing this data. In a [previous blog post](https://dev.to/aws/how-i-used-amazon-q-developer-to-move-faster-with-data-3e7i) I shared how I had started doing this, but it was time to revisit and simplify this approach.

Starting with the [GitHub API](https://raw.githubusercontent.com/094459/github-stats/refs/heads/main/docs/api.github.com.json) I was able to quickly get a prototype up in minutes. I was vibe coding hard, and as soon as Kiro had generated some code and I had tested it, I was providing feedback on what to change. When it comes to automation, this "tactile" feedback look is super satisfying.

I was pretty happy with how it turned out. I have shared the code [on Github here](https://github.com/094459/github-stats) if you want to use that as a starting point to see what is possible.

![demo of github-stats](https://raw.githubusercontent.com/094459/github-stats/refs/heads/main/images/github-stats-demo.png)

## OpenAPI specs are a great starting point

In both examples, my automation efforts very accelerated by having a good foundation - the service API. When you are working on automation, you need to consider how to provide the right context and so look for this. You might not always have OpenAPI spec documents, but there might be online SDK docs you can use for example as alternatives.

Bear in mind that when you are doing this, less is more. The GitHub API for example is massive - what I did was create some markdown documents by first introspecting and asking via Kiro CLI, some specific questions. For example, "Review the API and tell me how I would get traffic data for Clones and Views for a repo - put this in a document called git-traffic.md". I would then use these docs after carefully reviewing these were accurate.

## Improving and iterating

One of the unexpected things that I have learned as I have started to automate using tools like Kiro CLI is how quick and effortless is feels to iterate and improve the initial automations you create. After you start with your initial task, which might provide your basic automation need, I was discovering additional things that I did not think about in my original automation requirements. For example, in the fixing links I realised that I wanted to add the option to run in non destructive mode so I could analyse and check to make sure it was doing the right thing. With the GitHub Stats tool I realised that I wanted to change how I added new repos, what was the important data I wanted to capture, and how this would look on the dashboard.

I actually found that I was becoming addicted to the automation improvement cycle! From rough beginnings I was creating very useful tools that could stand by themselves. I just kept having more ideas and then quickly implementing them. This is the --help options for the link-fixing tool, I just would never have got around to implementing this if I was hand coding this.

```
python markdown_link_replacer.py --help
usage: markdown_link_replacer.py [-h] [--content-dir CONTENT_DIR] [--csv-file CSV_FILE] [--backup-dir BACKUP_DIR] [--no-backup]
                                 [--verbose] [--dry-run] [--parallel] [--max-workers MAX_WORKERS] [--validate-links]
                                 [--timeout TIMEOUT] [--max-retries MAX_RETRIES] [--concurrent-requests CONCURRENT_REQUESTS]
                                 [--ignore-ssl-errors] [--output-format {text,json,csv}] [--errors-only]
                                 [--exclude-domains EXCLUDE_DOMAINS] [--exclude-patterns EXCLUDE_PATTERNS] [--include-localhost]
                                 [--base-url BASE_URL] [--rate-limit-delay RATE_LIMIT_DELAY] [--max-redirects MAX_REDIRECTS]
                                 [--user-agent USER_AGENT] [--exclude-file EXCLUDE_FILE] [--include-file INCLUDE_FILE]
                                 [--fix-broken-links] [--state-file STATE_FILE]

Markdown Link Replacer - Replace tracked links and validate link health in markdown files

This tool provides two main modes of operation:

1. LINK REPLACEMENT MODE (default): Replaces tracked links in markdown files with their 
   destination URLs based on a CSV mapping file. This is useful for converting short 
   links or tracking URLs to their final destinations.

2. LINK VALIDATION MODE (--validate-links): Validates all links in markdown files by 
   making HTTP requests to check their status. Provides detailed reporting on broken 
   links, response times, and can automatically fix broken links using CSV mappings.

The tool can also operate in combined mode, performing both replacement and validation 
operations in sequence for a complete link management workflow.
        

options:
  -h, --help            show this help message and exit
  --content-dir CONTENT_DIR
                        Directory containing markdown files to process. The tool will recursively scan this directory for .md
                        files. (default: content)
  --csv-file CSV_FILE   Path to CSV file containing link mappings. Format: source_url,destination_url with one mapping per line.
                        Used for both replacement and broken link fixing. (default: data/tracked-links.csv)
  --backup-dir BACKUP_DIR
                        Directory to store backup files before modification. Backups are organized by timestamp and original file
                        path. (default: backups)
  --no-backup           Skip creating backup files before modification. WARNING: This is not recommended as it makes it impossible
                        to recover original files if needed.
  --verbose, -v         Enable verbose logging output. Shows detailed progress, file processing information, and validation
                        results. Useful for debugging and monitoring.
  --dry-run             Preview mode: show what changes would be made without actually modifying files. Useful for testing
                        configurations and reviewing potential changes.
  --parallel            Enable parallel processing of files for faster operation on large datasets. Use with --max-workers to
                        control concurrency level.
  --max-workers MAX_WORKERS
                        Maximum number of worker threads for parallel file processing. Higher values may improve performance but
                        use more system resources. (default: 4)
  --validate-links      Enable link validation mode to check HTTP status of all links found in markdown files. Makes HTTP requests
                        to verify each link is accessible and generates detailed reports on link health, response times, and
                        errors.
  --timeout TIMEOUT     HTTP request timeout in seconds. Increase for slow connections or decrease for faster validation of large
                        datasets. Range: 1-300 seconds. (default: 10)
  --max-retries MAX_RETRIES
                        Maximum number of retries for failed HTTP requests. Helps handle transient network issues. Set to 0 to
                        disable retries. Range: 0-10. (default: 2)
  --concurrent-requests CONCURRENT_REQUESTS
                        Maximum number of concurrent HTTP requests. Higher values speed up validation but may overwhelm servers or
                        trigger rate limiting. Use lower values (3-5) for respectful validation. Range: 1-50. (default: 10)
  --ignore-ssl-errors   Skip SSL certificate validation for HTTPS URLs. Useful for testing environments with self-signed
                        certificates, but reduces security. Use with caution in production.
  --output-format {text,json,csv}
                        Output format for validation reports. "text" provides human-readable reports, "json" enables programmatic
                        processing, "csv" allows spreadsheet analysis. (default: text)
  --errors-only         Filter validation report to show only links that returned errors (4xx, 5xx status codes, timeouts,
                        connection failures). Useful for focusing on issues that need attention.
  --exclude-domains EXCLUDE_DOMAINS
                        Comma-separated list of domains to exclude from validation. Useful for skipping internal systems,
                        development servers, or known problematic domains. Example:
                        "localhost,staging.example.com,internal.corp.com"
  --exclude-patterns EXCLUDE_PATTERNS
                        Comma-separated list of regex patterns to exclude URLs from validation. Allows flexible filtering based on
                        URL patterns. Example: ".*\.pdf$,.*\?utm_.*,.*#.*" to skip PDFs, tracking URLs, and anchors.
  --include-localhost   Include localhost and 127.0.0.1 URLs in validation. By default, local URLs are excluded since they
                        typically are not accessible from external validation environments.
  --base-url BASE_URL   Base URL for resolving relative links found in markdown files. Required if you want to validate relative
                        links like "/docs/page.html". Example: "https://mysite.com" converts "/docs" to "https://mysite.com/docs"
  --rate-limit-delay RATE_LIMIT_DELAY
                        Delay in seconds between requests to the same domain. Helps prevent overwhelming target servers and avoids
                        triggering rate limiting. Use higher values (2-5) for respectful validation, lower values (0.1-0.5) for
                        faster validation of trusted domains. (default: 1.0)
  --max-redirects MAX_REDIRECTS
                        Maximum number of HTTP redirects to follow before considering a link broken. Prevents infinite redirect
                        loops while allowing reasonable redirect chains. Range: 0-20. Set to 0 to treat any redirect as an error.
                        (default: 5)
  --user-agent USER_AGENT
                        User-Agent string sent with HTTP requests. Some servers block requests without proper user agents. Use
                        descriptive values that identify your validation tool. (default: Markdown-Link-Validator/1.0)
  --exclude-file EXCLUDE_FILE
                        Path to text file containing URLs to exclude from validation, one URL per line. Useful for maintaining a
                        persistent list of URLs to skip. Lines starting with # are treated as comments and ignored.
  --include-file INCLUDE_FILE
                        Path to text file containing URLs to include in validation, one URL per line. When specified, ONLY URLs in
                        this file will be validated (whitelist mode). Useful for validating specific subsets of links.
  --fix-broken-links    Automatically replace broken links with working alternatives from the CSV mapping file. When validation
                        finds broken links that have replacements available in the CSV, they will be automatically updated in the
                        markdown files.
  --state-file STATE_FILE
                        Path to state file for resumable validation. Allows interrupting and resuming long-running validations. If
                        not specified, auto-generates based on current date. Useful for large datasets or unreliable network
                        connections.

USAGE EXAMPLES:

Basic Link Replacement:
  markdown_link_replacer.py                                    
    Process content/ directory with default settings
```

That is not something that I expected, and I think shows how AI coding assistants are really helping developer to experiment and move more quickly.

It reminded me how many open source projects once started out,  an "itch" that one developer wanted to scratch.

## Finding my tools!

The growing number of tools that I have created has led to an unexpected issue - I have created so many tools, that I sometimes forget where they are and how they work. What I have started to do is consolidate these into one directory on my machine, this is my current set of tools:

```
tools
├── ai-agents
├── alt-spec
├── bootstrap-demos
├── devto-update
├── finch-postgres
├── fix-links
├── github-stats
├── gen-kiro-resources
├── load-gen
├── my-prompts
├── newsletter-automation
├── oss-projects
├── sdd
└── timer
```

I have then used Kiro to generate documentation for each of these tools where it was missing. What I noticed is that the earlier generation of tools that I created tended to have less (and lower quality) docs, so this was a good opportunity to use Kiro CLI to update these. 

## Conclusion

Automating your developer tasks is low hanging fruit for AI coding assistants, and is a great way for you to start learning how to get the best of them. I have shared a few examples of how I am using these to automate tasks, and when I speak with internal Builders and developers at events, they tell me some of the things they are automating. The call to action here is that with the barrier so low, there are really no reasons why you would not automate. Go Automate!

You can get started with Kiro today for free. [Download it from this link](https://kiro.dev/downloads/?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el) and then login using GitHub or your [Builder ID](https://builder.aws.com/start?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el). When you initially sign up you get a very generous 500 credits which are renew every month (50 for the free tier).  I have created a couple of workshops if you want to get deeper into Kiro. The [Kiro CLI workshop](https://github.com/094459/aqd-cli-workshop) will walk you through getting started with the terminal based Kiro CLI tool, and provides a comprehensive overview as well as advanced topics. My [spec driven development](https://github.com/094459/sdd-workshop) workshop dives more into using Kiro in spec driven mode.

Made with ❤️ by DevRel.
