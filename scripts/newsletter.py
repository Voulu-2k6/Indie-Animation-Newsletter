import os
import json
from pathlib import Path
from dotenv import load_dotenv
from eventregistry import EventRegistry, QueryArticlesIter

# --- Load secrets ---
load_dotenv("secrets.env")  # Reads the file

news_api_key = os.getenv("NEWSAPI_KEY")
er = EventRegistry(apiKey = news_api_key)
query = {
  "$query": {
    "keyword": '"anime news"',
    "keywordLoc": "body"
  },
  "$filter": {
    "forceMaxDataTimeWindow": "3",
    "dataType": "news"
  }
}
q = QueryArticlesIter.initWithComplexQuery(query)
items = []

for article in q.execQuery(er, maxItems=4):
    obj = {
        "title": article.get("title"),
        "url": article.get("url"),
        "image": article.get("image"),
        "date": article.get("date")
    }
    items.append(obj)

dir_path = Path(__file__).parent.parent
file_path = dir_path / "articles.JSON"

with open(file_path, "r", encoding="utf-8") as f:
    try:
        existing_items = json.load(f)
    except json.JSONDecodeError:
        existing_items = []

combined = existing_items + items

# Deduplicate by URL 
deduped_dict = {item['url']: item for item in combined}
deduped = list(deduped_dict.values())

# Sort by date
deduped.sort(key=lambda x: x['date'], reverse=True)

# Write back to file
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(deduped, f, indent=2)
