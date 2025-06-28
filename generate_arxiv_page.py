import feedparser

def fetch_arxiv_feed(query, max_results=5):
    base_url = "http://export.arxiv.org/api/query"
    full_url = f"{base_url}?search_query={query}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    return feedparser.parse(full_url)

def format_entry(entry):
    authors = ", ".join(author.name for author in entry.authors)
    summary = entry.summary.strip().replace('\n', ' ')
    return f"""
    <div class="paper">
      <h3><a href="{entry.link}" target="_blank">{entry.title}</a></h3>
      <p><strong>Authors:</strong> {authors}</p>
      <p>{summary[:300]}...</p>
    </div>
    """

# Fetch feeds
biomol_feed = fetch_arxiv_feed("cat:q-bio.BM")
peptide_feed = fetch_arxiv_feed("cat:q-bio.BM+AND+all:peptide")

# Generate HTML
with open("arxiv.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latest arXiv Papers</title>
  <style>
    body { font-family: sans-serif; max-width: 800px; margin: auto; padding: 2rem; }
    .paper { border-bottom: 1px solid #ccc; margin-bottom: 1rem; padding-bottom: 1rem; }
    h1, h2 { color: #333; }
  </style>
</head>
<body>
  <h1>arXiv Paper Feed</h1>

  <h2>🔬 Latest arXiv Papers in Biomolecules</h2>
""")

    for entry in biomol_feed.entries:
        f.write(format_entry(entry))

    f.write("<h2>🧬 Latest arXiv Papers in Peptides</h2>\n")

    for entry in peptide_feed.entries:
        f.write(format_entry(entry))

    f.write("</body></html>")
