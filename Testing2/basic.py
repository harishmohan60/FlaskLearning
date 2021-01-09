from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_logged_in = True
    puppies = ['Fluffy', 'Rufus', 'Spike']
    return render_template('basic.html', puppies=puppies, user_logged_in=user_logged_in)

if __name__ == '__main__':
    app.run(debug=None)