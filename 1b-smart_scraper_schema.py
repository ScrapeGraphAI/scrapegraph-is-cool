""" 
Basic example of scraping pipeline using SmartScraper with schema
"""
import os
import json
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from scrapegraphai.graphs import SmartScraperGraph

load_dotenv()

# ************************************************
# Define the output schema for the graph
# ************************************************

class Article(BaseModel):
    title: str = Field(description="The title of the article")
    author: str = Field(description="The author of the article")

class Articles(BaseModel):
    article: List[Article]

# ************************************************
# Define the configuration for the graph
# ************************************************

openai_key = os.getenv("OPENAI_APIKEY")

graph_config = {
    "llm": {
        "api_key": openai_key,
        "model": "openai/gpt-4o-mini",
    },
    "verbose": True,
    "headless": False,
}

# ************************************************
# Create the SmartScraperGraph instance and run it
# ************************************************

smart_scraper_graph = SmartScraperGraph(
    source="https://www.wired.com",
    prompt="Extract me all the articles",
    schema=Articles,
    config=graph_config
)

result = smart_scraper_graph.run()
print(json.dumps(result, indent=4))
