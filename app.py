from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def count_letters():

    if request.method == "POST":

        text = request.form["text"]

        letters = 0

        for i in text:
            if i.isalpha():
                letters += 1

        return f"Harflar soni: {letters}"

    return render_template("index.html")

app.run(debug=True)
