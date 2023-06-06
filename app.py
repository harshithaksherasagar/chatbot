import requests
from flask import Flask, render_template, request,json
import os
import openai


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    condition = request.form['condition']
    severity = request.form['severity']

    # Call the ChatGPT API and get the response
    response1 = get_chatbot_response(condition, severity)
    response=response1.choices[0]['text'].strip()

    return response
def get_chatbot_response(condition, severity):
    openai.api_key = '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'
    response = openai.Completion.create(

        engine="text-davinci-002",
        prompt=f"what is health condition with {condition} and {severity} severiaty",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5
    )


    return response
if __name__ == '__main__':
    app.run(debug=True)
