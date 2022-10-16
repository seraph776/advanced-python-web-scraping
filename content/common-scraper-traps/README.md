<div id="top"  align="center">


# Common Scraper Traps

</div>



In `SEO`, "crawler traps" are a structural issue within a website that causes crawlers to find a virtually infinite number of irrelevant URLs. In theory, crawlers could get stuck in one part of a website and never finish crawling these irrelevant URLs. That's why we call it a "crawl" trap. Crawler traps are sometimes also referred to as `"spider traps."` The most common crawler traps we often see in the wild:

- **Setting up robots.txt** — This is the most ineffective method to prevent scraping.
- **URLs with query parameters** — these often lead to infinite unique URLs.
- **Infinite redirect loops** — URLs that keep redirecting and never stop.
- **Links to internal searches** — links to internal search-result pages to serve content.
- **Dynamically generated content** — where the URL is used to insert dynamic content.
- **Infinite calendar pages** — where there's a calendar present that has links to previous and upcoming months.
- **Faulty links** — links that point to faulty URLs, generating even more faulty URLs.
- **Filtering requests by User agent** — This method merely stops new bots written by inexperienced scrapers for a few hours.
- **Blacklisting the IP address** — Less than 2% of scraping bots were detected for one of our customer’s when we did a trial run.
- **Throwing CAPTCHA** — Boring for users
- **Honey pot or Honey trap** — Honey pots are a brilliant trap mechanism to capture new bots (scrapers who are not well versed with structure of every page) on the website. Search engine bots visit these links and might get trapped accidentally. These links are interpreted as dead, irrelevant or fake links by search engines. With more such traps, the ranking of the website decreases considerably. In short, honey pots are risky business which must be handled very carefully.



## Honey Traps

Some website developers put honeypot traps in the form of links which are not visible to the typical user on the browser. The easiest way to set the honeypot is by setting the CSS as `display: none`. Since the web crawler script does not operate the way a human does, it can try to scrape the information from the link. As a result, the website detects the scraping and blocks the source IP address.

This detection is not easy and requires a significant amount of programming work to accomplish correctly.

<div align="right">

[[↑] Back to top](#top)

</div>  
