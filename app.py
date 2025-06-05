from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    blocks = None

    if request.method == "POST":
        block1 = random.randint(0, 1)
        block2 = random.randint(0, 1)
        blocks = ["正面" if block1 else "反面", "正面" if block2 else "反面"]

        if block1 != block2:
            result = "聖茭（一正一反）=> 神明同意"
        elif block1 == 1:
            result = "笑茭（兩正）=> 神明覺得好笑，請再問"
        else:
            result = "陰茭（兩反）=> 神明不同意"

    return render_template("index.html", blocks=blocks, result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render 會指定 PORT
    app.run(host="0.0.0.0", port=port, debug=True)