from flask import Flask, redirect, render_template, session, url_for, request
import csv

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/interests")
def interests():
    return render_template("interests.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/registered", methods = ["POST"])
def registered():
    if not request.form.get("name") or not request.form.get("where"):
        return render_template("index.html")
    file = open("registrants.csv", "a")
    writer = csv.writer(file)
    if request.form.get("otherpays"):
        writer.writerow((request.form.get("name"), request.form.get("where"), request.form.get("otherpays")))
    else:
        writer.writerow((request.form.get("name"), request.form.get("where")))
    file.close()
    return render_template("thanks.html")
