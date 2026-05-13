from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from models import UserStore

app = Flask(__name__)
app.config["SECRET_KEY"] = "round1-basic-secret"

user_store = UserStore()


@app.route("/")
def home():
    if session.get("email"):
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not email or not password:
            flash("Email and password are required.", "error")
            return render_template("register.html")

        created = user_store.create_user(email, generate_password_hash(password))
        if not created:
            flash("Email already exists.", "error")
            return render_template("register.html")

        flash("Account created. Please sign in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = user_store.get_user(email)
        if user is None or not check_password_hash(user.password_hash, password):
            flash("Invalid email or password.", "error")
            return render_template("login.html")

        session["email"] = user.email
        flash("Logged in successfully.", "success")
        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    email = session.get("email")
    if not email:
        flash("Please log in first.", "error")
        return redirect(url_for("login"))

    return render_template("dashboard.html", email=email)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("email", None)
    flash("Logged out.", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
