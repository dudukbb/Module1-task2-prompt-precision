import os
import re

from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from models import UserStore

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
PASSWORD_RE = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$")

app = Flask(__name__)
app.config["SECRET_KEY"] = "round3-precise-secret"

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
            flash("Please complete all fields.", "error")
            return render_template("register.html", email=email)

        if not EMAIL_RE.match(email):
            flash("Enter a valid email address, for example name@example.com.", "error")
            return render_template("register.html", email=email)

        if not PASSWORD_RE.match(password):
            flash(
                "Password must be at least 8 characters and include uppercase, lowercase, and a number.",
                "error",
            )
            return render_template("register.html", email=email)

        if password != confirm_password:
            flash("Password confirmation does not match.", "error")
            return render_template("register.html", email=email)

        created = user_store.create_user(email, generate_password_hash(password))
        if not created:
            flash("An account with this email already exists.", "error")
            return render_template("register.html", email=email)

        flash("Account created successfully. You can now sign in.", "success")
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
        flash("Signed in successfully.", "success")
        return redirect(url_for("dashboard"))

    return render_template("login.html", email="")


@app.route("/dashboard")
def dashboard():
    email = session.get("email")
    if not email:
        flash("Please sign in to access your dashboard.", "error")
        return redirect(url_for("login"))

    return render_template("dashboard.html", email=email)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("email", None)
    flash("You are now logged out.", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
