from flask import Flask, render_template
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/tomisagod')
def tom_is_a_god():
    return 'Tom is the greatest'


@app.route('/blog')
def blog():
    return render_template("blog.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
