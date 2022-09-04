from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('sign.html')


@app.route('/api', methods=["GET", "POST"])
def api():
    if request.method == 'POST':
        data = request.get_json()

        if {'name', 'position', 'phone', 'mail', 'location'}.issubset(data.keys()):
            return render_template('dynamic_sign.html',
                                   name=data['name'], position=data['position'],
                                   phone=data['phone'], mail=data['mail'], location=data['location'])
    return "Error: 400,\n" \
           "Essential: {'name', 'position', 'phone', 'mail', 'location'},\n" \
           "Optional: {'github', 'linkedin', 'youtube', 'hackerank', 'insta'}"


if __name__ == '__main__':
    app.run(debug=True)
