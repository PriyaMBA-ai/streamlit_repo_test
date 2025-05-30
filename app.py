from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    content = request.get_json()
    question = content['question']
    df = pd.read_json(content['data'])

    # Dummy response logic for demonstration
    if "top customer" in question.lower():
        top = df.sort_values('sales', ascending=False).iloc[0]
        answer = f"Top customer is {top['customer']} with sales of {top['sales']}."
    else:
        answer = "Sorry, I can only tell you about the top customer for now."

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(port=5000)