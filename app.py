from flask import Flask, render_template, request
from analyzer import analyze_logs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = []

    if request.method == "POST":

        file = request.files["logfile"]

        if file:

            content = file.read().decode("utf-8")

            result = analyze_logs(content)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)