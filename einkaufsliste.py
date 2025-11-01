from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Die Einkaufsliste
einkaufsliste = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        essen = request.form.get("essen")
        if essen:
            einkaufsliste.append(essen)
    return render_template("index.html", liste=einkaufsliste)

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(einkaufsliste):
        einkaufsliste.pop(index)
    return render_template("index.html", liste=einkaufsliste)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
