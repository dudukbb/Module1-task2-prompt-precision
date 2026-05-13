import os
import re

from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from models import UserStore

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

app = Flask(__name__)
app.config["SECRET_KEY"] = "round2-improved-secret"

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
        confirm_password = request.form.get("confirm_password", "")

        if not email or not password or not confirm_password:
            flash("All fields are required.", "error")
            return render_template("register.html", email=email)

        if not EMAIL_RE.match(email):
            flash("Please provide a valid email address.", "error")
            return render_template("register.html", email=email)

        if len(password) < 6:
            flash("Password must be at least 6 characters.", "error")
            return render_template("register.html", email=email)

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return render_template("register.html", email=email)

        created = user_store.create_user(email, generate_password_hash(password))
        if not created:
            flash("An account with this email already exists.", "error")
            return render_template("register.html", email=email)

        flash("Registration successful. Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html", email="")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not email or not password:
            flash("Email and password are required.", "error")
            return render_template("login.html", email=email)

        user = user_store.get_user(email)
        if user is None or not check_password_hash(user.password_hash, password):
            flash("Invalid email or password.", "error")
            return render_template("login.html", email=email)

        session["email"] = user.email
        flash("Welcome back.", "success")
        return redirect(url_for("dashboard"))

    return render_template("login.html", email="")


@app.route("/dashboard")
def dashboard():
    email = session.get("email")
    if not email:
        flash("Please log in to continue.", "error")
        return redirect(url_for("login"))

    return render_template("dashboard.html", email=email)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("email", None)
    flash("You have been logged out.", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
