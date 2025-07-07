from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.app_context().push()
db = SQLAlchemy(app)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    publisher = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


@app.route("/")
def index():
    return "Hello, World!"

@app.route("/books")
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        output.append({'id': book.id, 'title': book.title, 'author': book.author, 'publisher': book.publisher})
    return output

@app.route("/books/<id>")
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'title': book.title, 'author': book.author, 'publisher': book.publisher}

@app.route("/books", methods=["POST"])
def add_book():
    book = Book(title=request.json['title'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route("/books/<id>", methods=["DELETE"])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return {'result': True}