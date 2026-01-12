# web_crawler

A multithreaded web crawling and indexing system implemented in Python.  
The project is designed for large-scale content collection, text processing, and inverted index generation, with a focus on search engine and information retrieval research.

---

## Overview

`web_crawler` is a modular web crawling framework capable of fetching web pages concurrently, extracting hyperlinks, processing textual content using natural language processing techniques, and storing structured indexing data for downstream search and retrieval tasks.

The system is suitable for experimentation in search engines, crawling strategies, indexing pipelines, and NLP-based document processing.

---

## Features

- Concurrent web crawling using thread pools  
- URL discovery and normalization  
- Content extraction with HTML parsing  
- NLP-based text processing:
  - Tokenization
  - Stopword removal
  - Stemming
- Inverted index generation  
- Metadata extraction (title and description)  
- CSV-based persistent storage  

---

## Project Structure

```

web_crawler/
│
├── crawl.py                    # Basic URL extraction utility
├── WEB_sypder.py                # Main multithreaded crawler
├── indexing/
│   └── advanced_indexing.py     # NLP-based indexing logic
│
├── advanced_inverted_index.csv  # Generated inverted index
├── advanced_doc_info.csv        # Document metadata
└── README.md

````

---

## Technologies Used

- Python 3
- Requests
- BeautifulSoup
- NLTK
- Concurrent Futures
- CSV

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/web_crawler.git
cd web_crawler
pip install -r requirements.txt
````

NLTK resources are downloaded automatically during execution if not already available.

---

## Usage

Run the main crawler:

```bash
python WEB_sypder.py
```

The crawler:

1. Starts from predefined seed URLs
2. Fetches and parses web pages concurrently
3. Extracts and indexes textual content
4. Stores indexing and metadata results in CSV files

---

## Output Files

* `advanced_inverted_index.csv`
  Contains the inverted index mapping terms to document IDs.

* `advanced_doc_info.csv`
  Contains document-level metadata including URL, title, and description.
