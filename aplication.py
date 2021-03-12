"""Create route URL"""
from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello_world() -> str:
    """Index page"""
    return "hellow"

@app.route('/book/<int:book_id>')
def show_book(book_id) -> int:
    """Show book with given id"""
    return 'Book %d' % book_id

@app.route('/about/')
def about()-> str:
    """Show about information the site"""
    return 'it\'s site Book shop'

with app.test_request_context():
    url_for('static', filename='style.css')

if __name__ == "__main__":
    app.run(debug=True)
