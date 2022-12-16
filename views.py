from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__,"views")

@views.route("/")
def home():
  return render_template("index.html", name="Tim")

@views.route("/profile")
def profile():
  args = request.args
  name = args.get('name')
  return render_template("index.html", name=name) 

@views.route("/json")
def get_json():
  return jsonify({'first_name': 'Tim', 'last_name': 'Collins'})

@views.route("/data")
def get_data():
  data = request.json
  return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
  return redirect(url_for("views.get_json"))
