from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('sign.html')


@app.route('/api', methods=["GET", "POST"])
def api():
    if request.method == 'POST':
        data = request.get_json()

        if {'name', 'position', 'phone', 'email', 'location'}.issubset(data.keys()):
            return "xyz"
    return ""


if __name__ == '__main__':
    app.run(debug=True)
