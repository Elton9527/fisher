from flask import Flask
from helper import is_isbn_or_key
app = Flask(__name__)

@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    pass


@app.route('/')
def hello_world():
    return  "Hello World"

if __name__ == "__main__":
    app.run()