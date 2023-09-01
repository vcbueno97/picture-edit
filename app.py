from flask import Flask, render_template, request, url_for
from PIL import Image


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/edit", methods=["POST"])
def edit():
    user_img = request.files.get("img")

    with Image.open(user_img) as im:
        px = im.load()

    for x in range(im.size[0]):
        for y in range(im.size[1]):
            px[x, y] = (0, 0, 0)
    im.save("static/output.png")
    
    return render_template("edit.html")



