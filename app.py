from flask import Flask, render_template, request, url_for
from PIL import Image
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/edit", methods=["POST"])
def edit():
    user_img = request.files.get("img")

    im = Image.open(user_img) 

    im.save("static/userimg.png")
    
    if os.path.exists('static/userimg.png'):
        imgpath = url_for('static', filename='userimg.png')
    else:
        imgpath = url_for('static', filename='error.png')

    return render_template("edit.html", imgpath=imgpath)



