from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Route for the home page
@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        username = request.form.get("username")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        gender = request.form.get("gender")

        # Validation
        if not full_name.strip():
            flash("Full Name is required.", "error")
        elif not username.strip():
            flash("Username is required.", "error")
        elif not re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", email):
            flash("Please enter a valid email address.", "error")
        elif not re.match(r"^\d{10}$", phone):
            flash("Please enter a valid phone number (10 digits).", "error")
        elif len(password) < 6:
            flash("Password must be at least 6 characters long.", "error")
        elif password != confirm_password:
            flash("Passwords do not match.", "error")
        elif not gender:
            flash("Please select a gender.", "error")
        else:
            # Successful registration
            flash("Registration Successful!", "success")
            return redirect(url_for("register"))

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)