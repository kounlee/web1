from flask import Flask, render_template, request
from flask_pymongo import pymongo

app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb://localhost:27017/koun_project"
#app.config["SECRET_KEY"] = "abcd"
#mongo = PyMongo(app)

@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/maker",methods=["GET"])
def maker():
    return render_template("maker.html")


@app.route("/notice",methods=["GET"])
def notice():
    return render_template("notice.html")


@app.route("/problem",methods=["GET"])
def problem():
    if request.method == 'GET' :
        name = request.args.get()
        print()
    return render_template("problem.html")


if __name__=="__main__":
    app.run(debug=True, port=9000)
