# FAQ Generator

A tool to generate FAQs related to articles using web scraping and the OpenAI API. 

This prohect was developed during hackathon conducted by Bajaj Finserv Private Ltd

## Features

- **Web Scraping**: Extracts text from articles using BeautifulSoup.
- **FAQ Generation**: Utilizes OpenAI API to generate FAQs from the extracted text.
- **Flask Application**: Provides a web interface to input article URLs and view generated FAQs.

## Requirements

- Python 3.x
- Flask
- BeautifulSoup4
- OpenAI API key

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/awxsoul/FAQ_generator.git
    cd FAQ_generator
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key:
    ```bash
    export OPENAI_API_KEY='your-api-key-here'
    ```

## Usage

1. Run the Flask application:
    ```bash
    python main.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000`.

3. Enter the URL of the article you want to generate FAQs for and click "Submit".

Note : Generator is desgin to only extract article from Bajaj Finserv Article Information Website

## File Structure

- `main.py`: The main Flask application.
- `text_scrap.py`: Script for web scraping the article text.
- `text_ques.py`: Script for generating FAQs using the OpenAI API.
- `templates/`: HTML templates for the Flask application.
- `static/`: Static files for the Flask application (CSS, JS, etc.).
---
