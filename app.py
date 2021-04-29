from flask import Flask, render_template
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html")


@app.route('/secret')
def tom_has_a_secret():
    return 'Tom has a secret'


@app.route('/blog.html')
def blog():
    titles = ['Tom', 'Is', 'The', 'Best']
    return render_template("blog.html", titles=titles)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/portfolio.html')
def portfolio():
    return render_template("portfolio.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
