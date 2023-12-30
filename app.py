from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import Levenshtein

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_similarity', methods=['POST'])
def get_similarity():
    data = request.form
    text1 = data['text1']
    text2 = data['text2']

    # Calculate Levenshtein distance
    distance = Levenshtein.distance(text1, text2)

    # Normalize the distance to get a similarity score (0 to 1)
    max_len = max(len(text1), len(text2))
    similarity_score = round(1 - distance / max_len, 2)

    return render_template('index.html', similarity_score=similarity_score, text1=text1, text2=text2)

if __name__ == '__main__':
    app.run(debug=True)
