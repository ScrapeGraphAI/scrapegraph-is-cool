""" 
Basic example of scraping pipeline using SmartScraper
"""
import os
import json
from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperMultiGraph

load_dotenv()

openai_key = os.getenv("OPENAI_APIKEY")

graph_config = {
    "llm": {
        "api_key": openai_key,
        "model": "openai/gpt-4o",
    },
    "verbose": True,
    "headless": False,
}

multiple_search_graph = SmartScraperMultiGraph(
    prompt="Extract me all the articles",
    source= [
        "https://www.wired.com",
        "https://www.wired.com/category/politics/",
        "https://www.wired.com/category/science/",
        "https://www.wired.com/category/business/"
        ],
    schema=None,
    config=graph_config
)

result = multiple_search_graph.run()
print(json.dumps(result, indent=4))