from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('sign.html')


if __name__ == '__main__':
    app.run(debug=True)
