# Reddit Data API pilot

This repository contains the read-only Reddit adapter for an external company-news dashboard. The proposed pilot would link relevant public discussions to company profiles, preserve links and timestamps, and ask Reddit to confirm the terms for summarization with an external AI service. It does not propose model training on Reddit content.

Proposed pilot communities are r/wallstreetbets, r/stocks, r/StockMarket, r/investing, and r/SecurityAnalysis.

The current adapter demonstrates a single OAuth-authenticated listing request for public submissions. Subreddit search and comment retrieval are proposed pilot features. The adapter does not publish posts, write to disk, or send content to an AI service.

Use requires approved Reddit Data API access, with an OAuth token in REDDIT_ACCESS_TOKEN and an identifying user agent in REDDIT_USER_AGENT.
