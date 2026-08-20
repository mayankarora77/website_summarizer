import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from IPython.display import Markdown, display
from openai import OpenAI
from groq import Groq
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("GROQ_API_KEY"))
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

system_prompt="""You are an expert web content extraction and summarization assistant.

Your task is to analyze the textual content extracted from a webpage and produce an accurate, concise, and well-structured summary.

Instructions:
- Focus only on the primary content of the webpage.
- Ignore navigation menus, headers, footers, advertisements, cookie notices, social media links, legal disclaimers, and other boilerplate content.
- Ignore repeated text and duplicated sections.
- Identify the purpose of the webpage.
- Preserve important facts, names, dates, products, companies, and statistics.
- If the page contains news, announcements, releases, or updates, summarize those separately.
- If the page contains documentation, explain what the documentation is about and its key topics.
- If the page is a blog article, summarize the central ideas and important takeaways.
- If the page is a product page, summarize the product, its features, and intended audience.
- Do not invent information that is not present.
- If information is missing or unclear, state that explicitly.
- Respond only in Markdown.
- Do not include introductory phrases such here is the summary"""

user_prompt="""The following text was extracted from a webpage.

Analyze it and produce:

1. Website Type
2. One-sentence Summary
3. Detailed Summary
4. Key Points
5. Important Entities (people, companies, products, technologies)
6. News or Announcements (if any)
7. Main Topics
8. Overall Purpose of the Page
"""
def messages_for(website):
    return[
        {"role":"system","content":system_prompt},
    {"role":"user","content":user_prompt + website}]

def sumarize(url):
    website=fetch_website_contents(url)
    response=client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages_for(website)
    )
    return response.choices[0].message.content
def main():
    """Main entry point for testing."""
    url = input("Enter a URL to summarize: ")
    print("\nFetching and summarizing...\n")
    summary = sumarize(url)
    print(summary)
main()