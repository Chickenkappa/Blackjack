from flask import Flask, request, render_template
from api import get

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        card1 = int(request.form["first_card"])
        card2 = int(request.form["second_card"])
        sum = int(request.form["sum"])
        cardD = int(request.form["dealer_card"])
        result = get(card1, card2, cardD, sum)
        return render_template("result.html", result=result)
    elif request.method == "GET":
        return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True)
