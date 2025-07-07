from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/correct', methods=['POST'])
def correct():
    text = request.form.get('text')
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    return render_template('index.html', original_text=text, corrected_text=corrected_text)

if __name__ == '__main__':
    app.run(debug=True)
