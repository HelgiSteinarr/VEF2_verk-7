from bottle import *

user_secret = "5M2GLGXVK2H2W7L3XFR2HPEQ98NFFDZH5LUYQWI2VYF527XINLLQM3LW32IMNY5K"


@route("/")
def index():
    # Cookie content stored in variables for cleaner code
    username_cookie = request.get_cookie("username", secret=user_secret)
    password_cookie = request.get_cookie("password", secret=user_secret)

    if username_cookie and password_cookie:  # If set
        redirect("/secret")
    else:
        return template("login_template")


@route("/login", method="post")
def login():
    username = request.forms.get("username")
    password = request.forms.get("password")
    if username is not None and password is not None:
        if username == "admin" and password == "admin":
            response.set_cookie("username", username, secret=user_secret)
            response.set_cookie("password", password, secret=user_secret)
            redirect("/secret")
        else:
            return template("login_template", error="Rangar login upplýsingar")
    redirect("/")


@route("/secret")
def secret():
    username = request.get_cookie("username", secret=user_secret)
    password = request.get_cookie("password", secret=user_secret)
    if username is not None and password is not None:
        if username == "admin" and password == "admin":
            return template("secret_template")
    redirect("/")

@route("/logout")
def logout():
    response.delete_cookie("username", secret=user_secret)
    response.delete_cookie("password", secret=user_secret)
    redirect("/")


@route("/static/css/<filename:re:.*\.css>")
def send_css(filename):
    return static_file(filename, root='static/css')


run(host='localhost', port=8080)