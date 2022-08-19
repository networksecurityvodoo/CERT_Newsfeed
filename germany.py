## Retrieve current securityadvisory from CERT BUND via RSS-Feed ##


import feedparser
NewsFeed = feedparser.parse("https://wid.cert-bund.de/content/public/securityAdvisory/rss")

entry = NewsFeed.entries
for x in range(len(entry)):
    print (entry[x],)

