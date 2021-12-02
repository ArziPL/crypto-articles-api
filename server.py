from logging import debug
from flask import Flask
from flask import jsonify
import script

app = Flask(__name__)
host = "127.0.0.1"
port = 5000

@app.route("/")
def default_path():
    return "Use => GET /articles"

@app.route("/articles")
def articles():
    articles = script.get_articles()
    return jsonify(articles)

if __name__ == '__main__':
   app.run(host=host, port=port)