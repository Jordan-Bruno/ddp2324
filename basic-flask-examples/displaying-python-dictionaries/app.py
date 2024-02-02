from flask import Flask, render_template
from inventory import inventory_dict

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", inventory_dict=inventory_dict)


if __name__ == "__main__":
    app.run(debug=True)
