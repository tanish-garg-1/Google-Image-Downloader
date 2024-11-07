from flask import Flask, render_template, request, redirect, url_for
from downloader import download_images
from utils.emailer import send_email

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        keyword = request.form["keyword"]
        num_images = int(request.form["num_images"])
        email = request.form["email"]

        # Download images
        zip_path = download_images(keyword, num_images)

        # Send email with the download link
        send_email(email, zip_path)

        return redirect(url_for("index"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
