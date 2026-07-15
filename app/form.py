from pathlib import Path

from flask import Flask, render_template, request

app = Flask(__name__, template_folder=str(Path(__file__).resolve().parent.parent / "templates"))
@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method =="POST":
        name = request.form.get("username")
        message = request.form.get("message")
        return render_template("thank_you.html", name=name, message=message)
    return render_template("feedback.html")


if __name__ == "__main__":
    app.run(debug=True)

