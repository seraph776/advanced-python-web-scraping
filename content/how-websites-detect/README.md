<div id="top"  align="center">


# How Websites Detect Scraping

</div>


Websites can use different mechanisms to detect a scraper/spider from a normal user. Some of these methods are enumerated below:

1. Unusual traffic/high download rate especially from a single client/or IP address within a short time span.
2. Repetitive tasks performed on the website in the same browsing pattern – based on an assumption that a human user won’t perform the same repetitive tasks all the time.
3. Checking if you are real browser – A simple check is to try and execute javascript. Smarter tools can go a lot more and check your Graphic cards and CPU to make sure you are coming from real browser.
4. Detection through honeypots – these honeypots are usually links which aren’t visible to a normal user but only to a spider. When a scraper/spider tries to access the link, the alarms are tripped.

Detection can be done on `client side` i.e. on your browser or on `server-side` or by using both of these mechanisms. Web server can use inbuilt software to detect a bot or they can use clod service providers like AWS or Google cloud. As this detection is based on probability determined by considering various factors it can go wrong. Sometimes it can block genuine users and allow bots to enter the webpage.
  
## Server-side Bot Detection

This type of detection occurs at web server end by using either softwares or a web service provider. All the traffic is routed through that software or service provider’s server and only genuine users are allowed to actually hit the original web server. There are many ways to do such detection as follows:

**HTTP Fingerprinting:** - HTTP fingerprinting is done by scanning some basic information send by a browser like User Agent, Request headers like cookies, referrer, browser encoding, gzip compression etc. Most important and easy to detect way is IP address of the user.

**TCP/IP Fingerprinting:** - Any data that we send to a web server is sent as packets over TCP/IP. These packets contains details such as Initial packet size, TTL, Browser window size, segment size, window scaling value, “sackOk” flag, “nop” flag etc. All these details are combined to make a unique signature of a machine which can help in finding a bot.
Web Activity Monitoring and Pattern Detection:

After creating an identity using all the methods listed above, bot detectors can monitor user activity on a website or on number of websites using same bot detecting services and if any unusual activity is found like higher than usual requests which can only be made a by a bot. If a user is identified as a bot, website can ask to solve a CAPTCHA, if user fails he can be flagged or blocked.


<div align="right">

[[↑] Back to top](#top)

</div>  


## Client-Side Bot Detection

As client side bot detection is easier most websites use both technics. On the client side any request that is not coming through a genuine browser gets blocked instantly. Easiest way to detect if request is coming from a bot is to see if it can render a block of java script. All the browsers have javascript enabled while a request sent by a boat such as using Request module can not render a javascript.

In such cases a real browser is necessary to access the webpage and scrape it. There are libraries like selenium, puppeteer etc which can control a real web browser like chrome and do scraping.

Client side detection occurs by creating a fingerprint using multiple attributes of a real browser such as:

1. User Agent
2. Current Language
3. Do Not Track Status
4. Supported HTML5 Features
5. Supported CSS Rules
6. Javascript Features that Supported
7. Plugins installed in Browser
8. Screen Resolution, Color Depth
9. Time Zone
10. Operating System
11. Number of CPU Cores
12. GPU Vendor Name & Rendering Engine
13. Number of Touch Points
14. Different Types of Storage Support in Browser
15. HTML5 Canvas Hash
16. The list of fonts have installed on the computer


Using all these technics a website can detect a bot. But again as websites gets smarter in bot detecting so does the web scraper. Expertise web scraping services can mimic a browser using selenium or use proxies, IP rotation, CAPTCHA solving services etc to bypass all the checkpoints. It is an ongoing fight between websites and scrapers and both are continuously developing new ways to counter each other.

<div align="right">

[[↑] Back to top](#top)

</div>  


## How do you find out if a website has blocked or banned you?


If any of the following signs appear on the site that you are crawling, it is usually a sign of being blocked or banned.

- CAPTCHA pages
- Unusual content delivery delays
- Frequent response with HTTP 404, 301 or 50x errors

Frequent appearance of these HTTP status codes is also indication of blocking

- 301 Moved Temporarily
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 408 Request Timeout
- 429 Too Many Requests
- 503 Service Unavailable
