from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from google import genai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()

app = Flask(__name__)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/summary", methods=['GET','POST'])
def summary():
    if request.method == 'POST':
        data = request.get_json()
        query = data.get('text', '')
        text_length = data.get('text_length')  # default to 'medium'
        
    result = summarize(query, text_length)
    return jsonify(result)

def summarize(query,text_length):
    client = genai.Client(api_key=GEMINI_API_KEY)
    prompt = f"Summarize the following content in approximately {text_length} words or less:\n\n{query}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text


