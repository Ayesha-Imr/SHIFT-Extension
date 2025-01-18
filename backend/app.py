from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import analysis, get_alternatives

app = Flask(__name__)
CORS(app)

@app.route('/analyse', methods=['POST'])
def analyse():
    data = request.json
    extractedText = data.get('extractedText')
    print(extractedText)
    # Perform analysis 
    print(f"Received text: {extractedText}")
    analysis_result = analysis(extractedText)
    print(analysis_result)
    return jsonify({"message": "Analysis completed", "result": analysis_result})

@app.route('/alternatives', methods=['POST'])
def alternatives():
    data = request.json
    description = data.get('description')
    print("description received at backend: ", description)
    # Perform alternative fetching using the get_alternatives function
    alternatives_result = get_alternatives(description)
    print(alternatives_result)
    return jsonify({"message": "Alternatives fetched", "alternatives": alternatives_result})

if __name__ == '__main__':
    app.run(debug=True)
