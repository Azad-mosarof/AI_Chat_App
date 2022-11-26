from flask import Flask, jsonify, request
import openai

openai.api_key = "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"

app = Flask(__name__)

@app.route("/get_answer", methods=["POST"])
def get_answer():
    promt = request.get_json()['prompt']
    return jsonify(openai.Completion.create(
    model="text-davinci-002",
    prompt=promt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )["choices"][0]["text"])

if __name__ == "__main__":
    app.run()
    
