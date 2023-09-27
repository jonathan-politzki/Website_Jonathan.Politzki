from flask import Flask, request, jsonify
from transformers import pipeline
import requests


app = Flask(__name__)

@app.route('/get-response', methods=['POST'])
def get_response():
    user_input = request.json.get('user_input', '')
    
    # Load your response generator model
    generator = pipeline('text-generation', model='YourModelNameHere')
    response = generator(user_input, max_length=100)[0]['generated_text']

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

url = "http://127.0.0.1:5000/get-response"
data = {"user_input": "Hello, world!"}
response = requests.post(url, json=data)
print(response.json())