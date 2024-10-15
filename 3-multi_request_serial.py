import os
import json
from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info

load_dotenv()

# Define the configuration for the graph
graph_config = {
    "llm": {
        "api_key": os.getenv("OPENAI_API_KEY"),
        "model": "openai/gpt-4o",
    },
    "verbose": True,
    "headless": False,
}

# List of URLs to scrape
urls_to_scrape = [
    "https://www.wired.com",
    "https://www.wired.com/category/politics/",
    "https://www.wired.com/category/science/",
    "https://www.wired.com/category/business/",
]

# Loop through each URL, create a SmartScraperGraph instance, and run it
total_res = []
for url in urls_to_scrape:
    smart_scraper_graph = SmartScraperGraph(
        prompt="Extract me all the articles",
        source=url,
        config=graph_config,
    )

    result = smart_scraper_graph.run()
    print(f"Scraped {url}:\n{json.dumps(result, indent=4)}")

    graph_exec_info = smart_scraper_graph.get_execution_info()
    print(prettify_exec_info(graph_exec_info))
    total_res.append(prettify_exec_info)

print(total_res)
