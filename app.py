from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "anphotography123"

# ---------------- MAIL CONFIGURATION ---------------- #

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'abhijitnaikare7@gmail.com'
app.config['MAIL_PASSWORD'] = 'wyablsackygasigv'

mail = Mail(app)

# ---------------- HOME ---------------- #

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/wedding")
def wedding():
    return render_template("wedding.html")


@app.route("/prewedding")
def prewedding():
    return render_template("prewedding.html")


@app.route("/babyshoot")
def babyshoot():
    return render_template("babyshoot.html")


@app.route("/maternity")
def maternity():
    return render_template("maternity.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/bride")
def bride():
    return render_template("bride.html")


# ---------------- BOOK US ---------------- #

@app.route("/book", methods=["GET", "POST"])
def book():

    if request.method == "POST":

        first = request.form["first_name"]
        last = request.form["last_name"]
        mobile = request.form["mobile"]
        location = request.form["location"]
        email = request.form["email"]
        category = request.form.getlist("category")

        msg = Message(
            subject="New Booking Enquiry",
            sender=app.config['MAIL_USERNAME'],
            recipients=["abhijitnaikare7gmail.com"]
        )

        msg.body = f"""
NEW BOOKING ENQUIRY

Name : {first} {last}

Mobile : {mobile}

Location : {location}

Email : {email}

Category : {", ".join(category)}
"""

        try:
            mail.send(msg)
            flash("✅ Email Sent Successfully!")

        except Exception as e:
            flash("❌ Email Sending Failed!")
            print(e)

        return redirect("/book")

    return render_template("book.html")


# ---------------- RUN SERVER ---------------- #

if __name__ == "__main__":
    app.run(debug=True)