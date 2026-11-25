from flask import Flask,render_template,redirect,url_for,session,flash

app = Flask(__name__)
app.secret_key = "libray_management_system_190877_by_wtforms"


@app.route("/")
def index():
  """This is Home Page"""
  return render_template("member_login.html")



if __name__ == "__main__":
  app.run(debug=True)