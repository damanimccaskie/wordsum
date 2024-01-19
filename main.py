import nltk
from nltk.tokenize import word_tokenize, sent_tokenize  
from flask import Flask, render_template, request

nltk.download('punkt')
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["user-input"]
        result = analyze_text(text)
        return render_template("index.html", result=result)
    return render_template("index.html", result=None)

def analyze_text(text):
    words = word_tokenize(text)
    characters = len(text)
    sentences = sent_tokenize(text)
    paragraphs = text.split('\n')

    return {
        "word-count": len(words),
        "char-count": characters,
        "sent-count": len(sentences),
        "para-count": len(paragraphs)
    }


if __name__ == "__main__":
    app.run(debug=True)