from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/connect')
def connect():
    return render_template('connect.html')

if __name__ == '__main__':
    app.run(debug=True)
