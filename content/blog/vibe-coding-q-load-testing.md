+++
title = "Vibe coding with Amazon Q CLI - creating some load testing code"
date = 2025-06-24
draft = false
tags = []
categories = ["Technical"]
+++

I have a long history with testing, and specifically load testing. Many many years ago, I spent many a happy hour designing, building, running, and then assessing load tests for the applications I was working with. It was one of the first technical interviews I ever did and it was also how I found AWS, spinning up Centos load runners to simulate thousands of virtual test users. Ahh the good old days!

As this was for a fun side project, nothing serious, I thought I would vibe code this one as I didn't want to spend too much time and effort on it, and I kind of wanted to see what was possible. After loading up Amazon Q CLI, my starting gambit was:

> I want to load test an application using a tool in Python. I want it to generate realistic looking, randomised user agents. I want to be able to submit a url that it will access. Can you generate code and explanations

Whilst this produced some usable Python code, that simulated users by changing user agent strings, it was a little crude. 

I know that there are a lot of different tools and libraries to help here, so I followed up with some refining prompts.

> can you tell me about some load testing tools and libraries that work well with Python and that can simulate real users

What followed for the next twenty minutes was CHOP - Chat Orientated Programming, where I would take the output from one prompt, test it, and then refine my requirements with follow up prompts.

This flow navigated the solution and code from the initial code written in pure Python, to using tools like Locust, Artillary, Selenium, and then ending up at Playwright. A key part of this flow was:

- identifying what the important requirement was
- testing the resulting code against the requirements
- adjusting the prompt, or providing feedback to address issues

What was interesting as part of this CHOP flow was that I was learning about the trade-offs of these different tools, doing real implementation and testing of them to see how they would work. I learned more about load testing in today's Python that me reading a bunch of posts (ha! I am not trying to lose you dear reader....)

One of the areas that impressed me was in the subtle ways that I could tap the knowledge of the AI Coding Assistant to help tweak my solution. For example, whilst ALL the code generated worked and generated load, not all of the code testing the applications in the way that would accurately depict users. One specific is how these did (or didn't) support Javascript. This meant that as I was testing the code, I was refining my working knowledge of the domain and converting that into real code changes that addressed the underlying requirements. I can't state how important this is as a capability, especially for junior developers or those new to a library or framework who might have a good grasp of what they want, but not necessarily how to implement it. AI Coding Assistants can still be helpful, and magnify for me the **learn by doing**.

This was the script that it eventually created for me.


```
import asyncio
import time
import random
from playwright.async_api import async_playwright
import argparse

class AnalyticsLoadTester:
    def __init__(self, url, concurrent_users=3, duration=60, dwell_min=5, dwell_max=15, pause_min=3, pause_max=8):
        self.url = url
        self.concurrent_users = concurrent_users
        self.duration = duration
        self.dwell_min = dwell_min * 1000  # Convert to milliseconds
        self.dwell_max = dwell_max * 1000
        self.pause_min = pause_min * 1000
        self.pause_max = pause_max * 1000
        self.results = []
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        ]

    async def run_user_session(self, user_id):
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=False,  # Visible for analytics
                args=['--disable-blink-features=AutomationControlled']
            )
            context = await browser.new_context(
                user_agent=random.choice(self.user_agents),
                viewport={'width': 1920, 'height': 1080}
            )
            page = await context.new_page()
            
            # Force page to be "visible" for analytics
            await page.add_init_script("""
                Object.defineProperty(document, 'visibilityState', {
                    writable: true,
                    value: 'visible'
                });
                Object.defineProperty(document, 'hidden', {
                    writable: true,
                    value: false
                });
            """)
            
            start_time = time.time()
            end_time = start_time + self.duration
            requests = 0
            
            while time.time() < end_time:
                try:
                    request_start = time.time()
                    await page.goto(self.url, wait_until='networkidle')
                    
                    # Stay on page for configurable dwell time
                    dwell_time = random.randint(self.dwell_min, self.dwell_max)
                    await page.wait_for_timeout(dwell_time)
                    
                    # Simulate user interaction
                    await page.mouse.move(random.randint(50, 500), random.randint(50, 500))
                    await page.wait_for_timeout(1000)
                    
                    response_time = (time.time() - request_start) * 1000
                    self.results.append({
                        'user_id': user_id,
                        'response_time': response_time,
                        'status': 'success'
                    })
                    requests += 1
                    print(f"User {user_id}: Request {requests} - {response_time:.2f}ms")
                    
                    # Wait between requests (pause time)
                    pause_time = random.randint(self.pause_min, self.pause_max)
                    await page.wait_for_timeout(pause_time)
                    
                except Exception as e:
                    self.results.append({
                        'user_id': user_id,
                        'response_time': 0,
                        'status': 'error',
                        'error': str(e)
                    })
                    print(f"User {user_id}: Error - {str(e)}")
            
            await browser.close()

    async def run_load_test(self):
        print(f"Starting analytics-friendly load test on {self.url}")
        print(f"Users: {self.concurrent_users}, Duration: {self.duration}s")
        print(f"Dwell time: {self.dwell_min//1000}-{self.dwell_max//1000}s, Pause time: {self.pause_min//1000}-{self.pause_max//1000}s")
        print("Running with visible browsers for analytics tracking...")
        print("-" * 50)
        
        tasks = [self.run_user_session(i) for i in range(self.concurrent_users)]
        await asyncio.gather(*tasks)
        
        self.print_results()

    def print_results(self):
        print("\n" + "="*50)
        print("ANALYTICS LOAD TEST RESULTS")
        print("="*50)
        
        successful = [r for r in self.results if r['status'] == 'success']
        failed = [r for r in self.results if r['status'] == 'error']
        
        print(f"Total requests: {len(self.results)}")
        print(f"Successful: {len(successful)}")
        print(f"Failed: {len(failed)}")
        print(f"Success rate: {(len(successful)/len(self.results)*100):.1f}%")
        
        if successful:
            response_times = [r['response_time'] for r in successful]
            print(f"Average response time: {sum(response_times)/len(response_times):.2f}ms")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analytics-friendly load test')
    parser.add_argument('url', help='URL to test')
    parser.add_argument('-u', '--users', type=int, default=3, help='Concurrent users (default: 3)')
    parser.add_argument('-d', '--duration', type=int, default=60, help='Test duration in seconds (default: 60)')
    parser.add_argument('--dwell-min', type=int, default=5, help='Minimum dwell time on page in seconds (default: 5)')
    parser.add_argument('--dwell-max', type=int, default=15, help='Maximum dwell time on page in seconds (default: 15)')
    parser.add_argument('--pause-min', type=int, default=3, help='Minimum pause between requests in seconds (default: 3)')
    parser.add_argument('--pause-max', type=int, default=8, help='Maximum pause between requests in seconds (default: 8)')
    
    args = parser.parse_args()
    
    tester = AnalyticsLoadTester(args.url, args.users, args.duration, args.dwell_min, args.dwell_max, args.pause_min, args.pause_max)
    asyncio.run(tester.run_load_test())
```

Amazon Q CLI also helped me through getting this up and running, creating an installation script to manage all my dependencies.

```

sudo apt install python3.12-venv
sudo apt install python3-pip
sudo apt-get install xvfb

pip3 install requests playwright
playwright install-deps
playwright install chromium

```

Another example of how I use tools like Amazon Q CLI to provide focused learning is when it had finally finished and tested the code (on my mac), how to run this on a headless system. It walked me through the different options available, as well as providing code I could quickly test. In my specific case, to run this load test in a headless environment, you need to configure a virtual frame buffer and set this up before running the script.

```
#!/bin/bash

# Install Xvfb (virtual display) if not already installed
# Ubuntu/Debian: sudo apt-get install xvfb
# CentOS/RHEL: sudo yum install xorg-x11-server-Xvfb
# macOS: brew install --cask xquartz

# Run with virtual display
export DISPLAY=:98
Xvfb :98 -screen 0 1920x1080x24 &
XVFB_PID=$!

# Wait for Xvfb to start
sleep 2

# Run the analytics test
python3 load.py "$@"

# Clean up
kill $XVFB_PID
``` 

I don't know about you, but this took Amazon Q CLI all of about 20 seconds to create. This would easily have consumed me for around 20-30 minutes as I am not writing scripts on a regular basis these days, and certainly have not done much with virtual frame buffers since a while back.

One thing that is perhaps not talked as much as that whilst tools like Amazon Q CLI are great at writing code, once you have your code, you still need to deploy/run it somewhere. That easily takes up as much if not more time, so its great that I can use Amazon Q CLI to take a lot of that heavy lifting off me. This is the bash script that Amazon Q CLI created to run these tests.

```
#!/bin/bash

# Configuration variables
URLS=(
    "url1"
    "url2"
    "url3"
    "url4"
)

# User count range (min-max)
USER_MIN=5
USER_MAX=10

# Duration range in seconds (min-max)
DURATION_MIN=120
DURATION_MAX=720

# Dwell time ranges
DWELL_MIN_RANGE=(30 60)
DWELL_MAX_RANGE=(70 120)

# Set paths
SCRIPT_DIR="/home/ubuntu/load-gen"
LOG_FILE="$SCRIPT_DIR/logs/load_test_$(date +%Y%m%d_%H%M%S).log"

# Create logs directory if it doesn't exist
mkdir -p "$SCRIPT_DIR/logs"

# Change to script directory
cd "$SCRIPT_DIR"

# Randomize parameters
RANDOM_URL=${URLS[$RANDOM % ${#URLS[@]}]}
RANDOM_USERS=$((RANDOM % (USER_MAX - USER_MIN + 1) + USER_MIN))
RANDOM_DURATION=$((RANDOM % (DURATION_MAX - DURATION_MIN + 1) + DURATION_MIN))
RANDOM_DWELL_MIN=$((RANDOM % (${DWELL_MIN_RANGE[1]} - ${DWELL_MIN_RANGE[0]} + 1) + ${DWELL_MIN_RANGE[0]}))
RANDOM_DWELL_MAX=$((RANDOM % (${DWELL_MAX_RANGE[1]} - ${DWELL_MAX_RANGE[0]} + 1) + ${DWELL_MAX_RANGE[0]}))

# Run the load test with logging
echo "$(date): Starting load test" >> "$LOG_FILE"
echo "URL: $RANDOM_URL" >> "$LOG_FILE"
echo "Users: $RANDOM_USERS, Duration: ${RANDOM_DURATION}s, Dwell: ${RANDOM_DWELL_MIN}-${RANDOM_DWELL_MAX}s" >> "$LOG_FILE"
source .venv/bin/activate
./run_with_xvfb.sh "$RANDOM_URL" -u "$RANDOM_USERS" -d "$RANDOM_DURATION" --dwell-min "$RANDOM_DWELL_MIN" --dwell-max "$RANDOM_DWELL_MAX" >> "$LOG_FILE" 2>&1
echo "$(date): Load test completed" >> "$LOG_FILE"

# Clean up old logs (keep last 30 days)
find "$SCRIPT_DIR/logs" -name "load_test_*.log" -mtime +30 -delete
```

I had spun up an EC2 instance running Ubuntu to test this out, and everything worked faultlessly. I made some changes, and those changes (thanks to Amazon Q CLI) helped me create a super fast feedback loop, allowing me to try changes easily to add new features (test a selection of URLs, add dwell time and pause times, randomise the number of test users, etc).

**Get started with Amazon Q CLI**

This was a quick post that showed you how I am sometimes using Amazon Q CLI to Vibe code, creating working code to satisfy my curiosity and learn new things. I spent all of about 45 minutes putting this together, and I estimate I saved myself 1-2 days worth of effort. It was enough effort that I would ordinarily have not spent the time/effort to learn about these modern application load testing tools. 

So, what do you want to learn, and how can you use Amazon Q CLI to help you?

I hope this blog post has inspired you to want to try Amazon Q CLI for yourself. You can try it for free by [signing up for a Builder ID](https://community.aws/builderid?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el) and then downloading the app [from here](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html?trk=71546b8e-c969-4ead-aa9f-9cd06f6d8610&sc_channel=el).

Until next time folks!

Made with 🧡 by DevRel!
