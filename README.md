# MindSphere GPT

MindSphere GPT is a Flask-based chatbot web application that responds to user queries using predefined conversational responses and dynamic Wikipedia information retrieval. It matches user input against regex-based intent patterns and, when no predefined match exists, automatically searches Wikipedia, scrapes relevant page data, cleans the content, and returns meaningful textual responses.

The app provides a simple browser interface where users can chat with the AI in real time.

---

## Overview

The application runs a Flask server that:

* Serves a chat-based web interface
* Processes user input in `/chat`
* Matches user text against conversational patterns
* Returns randomized predefined answers where applicable
* Falls back to Wikipedia search for general knowledge queries
* Scrapes top Wikipedia pages, extracts content, cleans formatting, and returns readable responses

If no useful result is found, the chatbot informs the user accordingly.

---

## Features

* Real-time chatbot conversation
* Predefined conversational responses covering common questions
* Regex-based intent detection
* Live Wikipedia search fallback
* Wikipedia content scraping using the MediaWiki API
* HTML content cleaning to extract readable paragraphs
* Simple and clean web UI
* Flask backend with POST-based communication

---

## Tech Stack

* **Backend:** Python, Flask
* **Web Scraping / Data Retrieval:** requests, BeautifulSoup, Wikipedia API
* **Frontend:** HTML (Jinja2 template)
* **Deployment Support:** gunicorn

---

## Project Structure

```
MindSphere-GPT-main/
│
├── app.py                     # Core Flask app and chatbot logic
├── requirements.txt           # Python dependencies
│
└── templates/
    └── index.html             # Chat UI
```

---

## Installation

1. Ensure Python is installed.
2. Extract the project folder.
3. Open a terminal in the project directory.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

The application runs in debug mode.
Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## How It Works

1. User enters a message in the chat UI.
2. The request is sent to:

```
POST /chat
```

3. The backend:

   * Checks predefined regex-based conversation patterns.
   * If matched, returns a randomized associated response.
   * Otherwise:

     * Searches Wikipedia using the MediaWiki Search API.
     * Fetches top matching pages.
     * Extracts HTML content.
     * Cleans and formats content using BeautifulSoup.
     * Returns the processed text.

4. The response is displayed in the chat UI.

---

## Notes

* Internet connection is required for Wikipedia responses.
* If Wikipedia does not return any useful result, the chatbot replies:

  ```
  Sorry, I couldn't find any relevant information.
  ```
* The bot introduces itself as an AI chatbot named **MindSphere**, created by **Ram**.

---

## Dependencies

Defined in `requirements.txt`, including:

* Flask
* requests
* beautifulsoup4
* gunicorn
* requests-oauthlib

---

## License

No license file is included in this project.
