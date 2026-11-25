"""Read-only listing adapter for use with approved Reddit Data API access."""

import json
import os
import re
from datetime import datetime, timezone
from urllib.request import Request, urlopen


def read_public_submissions(username):
    """Return up to 100 public submissions and whether more are available."""
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,30}", username):
        raise ValueError("Invalid Reddit username")

    token = os.environ.get("REDDIT_ACCESS_TOKEN")
    user_agent = os.environ.get("REDDIT_USER_AGENT")
    if not token or not user_agent:
        raise RuntimeError("Approved OAuth access and a Reddit User-Agent are required")

    request = Request(
        f"https://oauth.reddit.com/user/{username}/submitted?limit=100",
        headers={"Authorization": f"Bearer {token}", "User-Agent": user_agent},
    )
    with urlopen(request, timeout=20) as response:
        listing = json.load(response)["data"]

    posts = []
    for child in listing["children"]:
        post = child["data"]
        posts.append({
            "url": "https://www.reddit.com" + post["permalink"],
            "published_at": datetime.fromtimestamp(
                post["created_utc"], timezone.utc
            ).isoformat(),
            "text": post["title"] + "\n" + post.get("selftext", ""),
        })
    return posts, bool(listing.get("after"))
