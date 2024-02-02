from flask import Flask, render_template, request, redirect, url_for
from inventory import inventory_dict

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", inventory_dict=inventory_dict)


@app.route("/add_item", methods=["POST"])
def add_item():
    item_id = int(request.form["id"])
    name = request.form["name"]
    description = request.form["description"]
    quantity = int(request.form["quantity"])

    inventory_dict[item_id] = [name, description, quantity]

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
