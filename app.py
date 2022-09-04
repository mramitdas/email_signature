from flask import Flask, render_template, request

app = Flask(__name__)

icons = {
    "github": "https://github.com/mramitdas/imStore/raw/main/github.png",
    "hackerrank": "https://github.com/mramitdas/imStore/raw/main/hackerank.png",
    "instagram": "https://github.com/mramitdas/imStore/raw/main/insta.png",
    "linkedin": "https://github.com/mramitdas/imStore/raw/main/linkedin.png",
    "youtube": "https://github.com/mramitdas/imStore/raw/main/youtube.png",

    "location": "https://github.com/mramitdas/imStore/raw/main/location.png",
    "mail": "https://github.com/mramitdas/imStore/raw/main/mail.png",
    "phone": "https://github.com/mramitdas/imStore/raw/main/phone.png"
}


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('sign.html')


@app.route("/api", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        data = request.get_json()

        if {'name', 'position', 'phone', 'mail', 'location', 'image_url'}.issubset(data.keys()):

            social_icons = []
            # Social icons processing
            for account in data['social_accounts']:
                account_icon = icons[account]
                account_url = data['social_accounts'][account]

                social_icons.append([account_url, account_icon])

            return render_template('dynamic_sign.html',
                                   name=data['name'], position=data['position'],

                                   phone=[data['phone'], icons['phone']],
                                   mail=[data['mail'], icons['mail']],
                                   location=[data['location'], icons['location']],

                                   image=data['image_url'], social_icons=social_icons)

        return "Error: 400,\n" \
               "Essential: {'name', 'position', 'phone', 'mail', 'location', 'image_url'},\n" \
               "Optional: {'github', 'linkedin', 'youtube', 'hackerank', 'insta'}"


if __name__ == '__main__':
    app.run(debug=False)
