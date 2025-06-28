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
      <h3><a href="{entry.link}" target="_blank" rel="noopener">{entry.title}</a></h3>
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
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Latest arXiv Papers - Biomolecules</title>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Fira Code', monospace;
      margin: 0;
      background-color: #f9f9f9;
      color: #333;
    }
    header, footer {
      background-color: #282c34;
      color: white;
      padding: 1rem;
      text-align: center;
    }
    nav a {
      color: white;
      margin: 0 1rem;
      text-decoration: none;
    }
    main {
      max-width: 800px;
      margin: 2rem auto;
      padding: 1rem;
    }
    .paper {
      border-bottom: 1px solid #ccc;
      margin-bottom: 1rem;
      padding-bottom: 1rem;
    }
  </style>
</head>
<body>

<header>
  <h1>My Blog</h1>
  <nav>
    <a href="index.html">Home</a>
    <a href="#">Projects</a>
    <a href="#">About</a>
    <a href="arxiv.html">Latest Papers</a>
  </nav>
</header>

<main>
  <h2>🔬 Latest arXiv Papers in Biomolecules</h2>
""")

    for entry in biomol_feed.entries:
        f.write(format_entry(entry))

    f.write("<h2>🧬 Latest arXiv Papers in Peptides</h2>\n")

    for entry in peptide_feed.entries:
        f.write(format_entry(entry))

    f.write("""
</main>

<footer>
  © 2025 My Blog | Powered by arXiv API
</footer>

</body>
</html>""")
