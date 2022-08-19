import feedparser
NewsFeed = feedparser.parse("https://cert.at/cert-at.de.warnings.rss_2.0.xml")

entry = NewsFeed.entries
for x in range(len(entry)):
    print (entry[x],)
