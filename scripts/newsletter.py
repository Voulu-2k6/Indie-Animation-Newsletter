import os
from dotenv import load_dotenv
from eventregistry import EventRegistry, QueryArticlesIter

# --- Load secrets ---
load_dotenv("secrets.env")  # Reads the file

news_api_key = os.getenv("NEWSAPI_KEY")
er = EventRegistry(apiKey = news_api_key)
query = {
  "$query": {
    "keyword": "animation",
    "keywordLoc": "body"
  },
  "$filter": {
    "forceMaxDataTimeWindow": "3"
  }
}
q = QueryArticlesIter.initWithComplexQuery(query)

for article in q.execQuery(er, maxItems=10):
    print(article.get("title", "No title available"))
    print(article.get("url", "No URL available"))