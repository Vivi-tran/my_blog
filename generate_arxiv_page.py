import feedparser

URL = "http://export.arxiv.org/api/query?search_query=cat:cs.AI&start=0&max_results=5&sortBy=submittedDate&sortOrder=descending"
feed = feedparser.parse(URL)

with open("arxiv.html", "w", encoding="utf-8") as f:
    f.write("<html><head><title>Latest arXiv Papers</title></head><body>")
    f.write("<h1>Latest arXiv Papers in AI</h1>")

    for entry in feed.entries:
        f.write(f"<div><h3><a href='{entry.link}'>{entry.title}</a></h3>")
        f.write(f"<p><strong>Authors:</strong> {', '.join(author.name for author in entry.authors)}</p>")
        f.write(f"<p>{entry.summary[:300]}...</p></div><hr>")

    f.write("</body></html>")
