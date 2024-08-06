# save_static.py
# Python Script to Render and Save Static HTML
from flask import Flask, render_template
from list_texts import LIST_TEXTS
import random
import os

# Initialize Flask app
app = Flask(__name__)

# Function to get a random quote
def get_random_file():
    return random.choice(LIST_TEXTS)

# Create a context to render the template with random quotes
with app.app_context():
    # Generate quotes
    quote1 = get_random_file()
    quote2 = get_random_file()
    
    # Render template with quotes
    rendered_html = render_template('index.html', quote1=quote1, quote2=quote2)
    
    # Define the path to save the rendered HTML
    output_path = 'docs/index.html'  # GitHub Pages can use 'docs' or root directory
    
    # Ensure the 'docs' directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save the rendered HTML
    with open(output_path, 'w') as f:
        f.write(rendered_html)
