from flask import Flask, render_template, request
from list_texts import LIST_TEXTS
import random
import os

# Set the working directory to the directory of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

# Function to get a random quote
def get_random_file():
    quote=random.choice(LIST_TEXTS)
    return quote

@app.route('/')
def index():
    return render_template('index.html', quote=get_random_file())


if __name__ == '__main__':
    app.run(debug=True)