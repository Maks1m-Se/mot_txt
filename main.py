from flask import Flask, render_template, request
from list_texts import list_texts
import random
import os

# Set the working directory to the directory of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

# Function to get a random filename from a given directory
def get_random_file(directory):
    print("Current working directory:", os.getcwd())
    print("Contents of directory:", os.listdir(directory))
    files = os.listdir(directory)
    return os.path.join(directory, random.choice(files)).replace("\\","/")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    # Get the guessed code from the form
    user_code = request.form['user_code']
    user_position = int(request.form['position'])
    
    result_optional = '' #initial empty optional message

    # Check if the guess is correct
    if user_position in CORRECT_CODES and user_code == CORRECT_CODES[user_position]:
        day = user_position
        result1 = f'{user_code} ist RICHTIG!'
        result2 = f'Du darfst das {day}. Türchen öffnen.'
        print(OPTIONAL_MESSAGES.keys(), list(OPTIONAL_MESSAGES.keys()))
        if user_code in OPTIONAL_MESSAGES.keys():
            result_optional = OPTIONAL_MESSAGES[user_code]
        # Select a random happy sound and gif
        res_sound = get_random_file('static/sounds/happy_sounds')
        res_img = get_random_file('static/images/happy_kittens')
        print('happy paths:\n', res_sound)
        print(res_img)
    else:
        result1 = f'{user_code} für das {user_position}. Türchen ist leider falsch.'
        result2 = 'Versuch es nochmal'
        # Select a random sad sound and gif
        res_sound = get_random_file('static/sounds/sad_sounds')
        res_img = get_random_file('static/images/sad_kittens')
        print('sad paths:\n', res_sound)
        print(res_img)

    # Return the result to the user
    return render_template('result.html',
                           result1=result1, result2=result2,
                           result_optional=result_optional,
                           res_sound=res_sound, res_img=res_img)

if __name__ == '__main__':
    app.run(debug=True)