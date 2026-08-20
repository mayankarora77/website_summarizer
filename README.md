# Website Summarizer

An AI-powered website summarizer that scrapes webpage content and generates concise summaries using Large Language Models (LLMs).

## Features

- Scrapes webpage content from any public URL
- Removes unnecessary HTML elements such as:
  - Scripts
  - Styles
  - Images
  - Input fields
- Extracts clean text content
- Generates intelligent summaries using Llama models
- Supports both:
  - Ollama (local LLM)
  - Groq API

## Tech Stack

- Python
- Requests
- BeautifulSoup4
- OpenAI Python SDK
- Ollama
- Groq API

## Project Structure

```
website_summarizer/
│── scraper.py
│── code.ipynb
│── requirements.txt
│── .gitignore
│── README.md
│── .env.example
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/website-summarizer.git
cd website-summarizer
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

Example:

```text
GROQ_API_KEY=your_groq_api_key
```

If using Ollama, make sure the Ollama server is running locally:

```bash
ollama serve
```

## Usage

Run the notebook or execute the Python script.

Example URL:

```
https://openai.com
```

The application will:

1. Fetch the webpage.
2. Extract the main textual content.
3. Send the content to the LLM.
4. Return a concise summary.

## Example Output

- Website Type
- One-line Summary
- Detailed Summary
- Key Points

## Future Improvements

- Crawl multiple pages from the same website
- Extract metadata
- Support PDF summarization
- Generate structured JSON output
- Build a Streamlit web interface
- Add Retrieval-Augmented Generation (RAG)

## License

This project is licensed under the MIT License.