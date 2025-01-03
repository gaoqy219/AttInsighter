from flask import Flask, render_template, request
from ollama import generate

app = Flask(__name__, template_folder='/working')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    input_text = request.form['inputText']
    res=generate('attinsighter',input_text)
    return res['response']

if __name__ == '__main__':
    app.run(debug=True)