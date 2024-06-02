from flask import Flask, render_template, request
import re
import random
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

patterns_responses = [
    (r"hi|hello|hey", ["Hello! How can I help you today?", "Hi there! How can I help you today?", "Hey! How can I help you today?"]),
    (r"how are you|how are things", ["I am doing good, how about you?", "Doing well! How about you?"]),
    (r"(.*) your name?", ["I am an AI chatbot created by Ram. You can call me Ram."]),
    (r"what can you do", ["I can help answer your questions, provide information, and assist with various tasks. Just let me know what you need!"]),
    (r"where are you located", ["I exist in the digital realm, accessible wherever you need me!"]),
    (r"who created you", ["I was created by Ram."]),
    (r"how does your technology work", ["I utilize natural language processing and machine learning algorithms to understand and respond to your queries."]),
    (r"can you help me with (.*)", ["Of course! What do you need help with?"]),
    (r"do you have a personality", ["I try to be friendly and helpful, but ultimately, I'm just a program running some code!"]),
    (r"are you human", ["No, I’m not a human. I’m an AI chatbot designed to assist you."]),
    (r"do you sleep", ["No, I'm available 24/7 to help you whenever you need assistance."]),
    (r"how old are you", ["I was created by Ram, so you could say I'm as old as my development."]),
    (r"what languages do you speak", ["I can understand and respond in multiple languages, including English, Hindi, and many others."]),
    (r"tell me a joke", ["Sure! Why don't scientists trust atoms? Because they make up everything!"]),
    (r"what's the weather like today", ["I don’t have real-time data, but you can check the weather on your preferred weather app or website."]),
    (r"what's the meaning of life", ["That's a big question! Philosophers have debated it for centuries. Some say it's about finding happiness, others say it's about personal growth and fulfillment."]),
    (r"recommend a (.*)", ["Certainly! What genre or type of cuisine are you interested in?"]),
    (r"what's the capital of (.*)", ["The capital of {0} is..."]),
    (r"help me with my homework", ["I can certainly try! What subject are you working on?"]),
    (r"do you learn over time", ["I don’t learn from individual interactions, but I’m built on models that have been trained on vast amounts of data to understand and generate human-like text."]),
    (r"how can I use you", ["You can use me to get answers to questions, generate text, learn new information, and much more. Just ask away!"]),
    (r"is my data safe with you", ["I don’t store personal data from interactions. However, always be cautious about sharing sensitive information online."]),
    (r"which model|what model|which version", ["This is the AI Chatbot 4 model, named MindSphere."]),
]

def wikipedia_search(query):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": 3  
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def fetch_wikipedia_page(page_id):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "pageid": page_id,
        "format": "json",
        "prop": "text",
        "section": 0
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        result = response.json()
        return result['parse']['text']['*']
    return None

def clean_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = soup.find_all('p')
    paragraph_texts = [p.get_text() for p in paragraphs if p.get_text().strip() != '']
    clean_text = "\n\n".join(paragraph_texts)
    clean_text = re.sub(r'\[\d+\]', '', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    return clean_text

def scrape_wikipedia_search_results(question):
    results = wikipedia_search(question)
    if results:
        search_results = results.get('query', {}).get('search', [])
        if search_results:
            response_texts = []
            for result in search_results:
                page_id = result.get('pageid', '')
                page_content = fetch_wikipedia_page(page_id)
                if page_content:
                    clean_content = clean_html(page_content)
                    response_texts.append(clean_content)
            return "\n\n".join(response_texts)
    return None

def respond(user_input):
    for pattern, responses in patterns_responses:
        match = re.match(pattern, user_input.lower())
        if match:
            response = random.choice(responses).format(*match.groups())
            return response
    search_results = scrape_wikipedia_search_results(user_input)
    if search_results:
        return search_results
    else:
        return "Sorry, I couldn't find any relevant information."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["user_input"].strip()
    response = respond(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)
