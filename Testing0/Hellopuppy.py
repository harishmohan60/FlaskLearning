from flask import Flask
app = Flask(__name__)

@app.route('/home')
def index():
    return '<h1>Hello Puppy!</h1>'

@app.route('/about')
def info():
    return "<h1>About Puppies</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This is a page for {}</h1>".format(name)

@app.route('/puppy1/<name>')
def puppy1(name):
    return  "Upper Case: {}".format(name.upper())

@app.route('/puppy2/<name>')
def puppy2(name):
    return "TestingDebug: {}".format(name[-1])

if __name__ == '__main__':
    app.run(debug=True)