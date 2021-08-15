from flask import render_template,request,redirect
from flask_app import app

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/dojos")
def index():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("dojo.html", all_dojos = dojos)

@app.route("/dojos/<int:id>")
def display_dojo(id):
    data={
        'id':id
    }
    dojo = Dojo.get_dojo_ninjas(data)
    print(dojo)
    return render_template("dojo_show.html", dojo = dojo)

@app.route("/ninjas")
def display_ninja():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("ninja.html", all_dojos = dojos)

@app.route("/add_ninja", methods =["POST"])
def create_ninja():
    data = {
        "dojo_id": request.form["dojo_id"],
        "first_name": request.form["first_name"],
        "last_naem" : request.form["last_naem"],
        "age" : request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    id = Ninja.add_ninja(data)
    print(id)
    print("#####################")
    return redirect(f"/dojos/{data['dojo_id']}")

@app.route("/make_dojo", methods=["POST"])
def create_dojo():
    data = {
        "name":request.form["dojo_name"]
    }
    Dojo.add_dojo(data)
    return redirect("/dojos")