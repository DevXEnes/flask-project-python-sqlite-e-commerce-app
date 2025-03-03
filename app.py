from flask import Flask, render_template, request
from db import check_user_credentials, create_user

app = Flask(__name__)


@app.route("/register", methods=["GET", "POST"])  # Notice the leading slash here
def register():
    if request.method == "POST":
        personame = request.form["personname"]
        new_username = request.form["username"]
        email = request.form["email"]
        new_pass = request.form["password"]
        if (
            create_user(
                username=new_username, password=new_pass, name=personame, email=email
            )
            == False
        ):
            return "HTML Eroor 404"
        else:
            mess = "Your registration has been received"
            return render_template("login.html", error_mes=mess)

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def login():
    err = "Invalid Passoword and Username"
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        response = check_user_credentials(username=username, password=password)
        if response == True:
            return render_template("index.html", namea=username)
        else:
            return render_template("login.html", error_mes=err)
    message = " "
    return render_template("login.html", error_mes=message)


if __name__ == "__main__":
    app.run(debug=True)
