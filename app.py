"""Create route URL"""
from flask import Flask

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
    """About information the site"""
    return 'it\'s site Book shop'

if __name__ == "__main__":
    pass
