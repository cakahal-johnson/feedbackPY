from SEO import db, app
from flask import get_flashed_messages, render_template, url_for, redirect, flash, redirect, request, abort, session
from SEO.models import Feedback


@app.route('/')
def index():
    return render_template("index.html", title="Home")


@app.route('/about')
def about():
    return render_template("about.html", title="About")


@app.route('/services')
def services():
    return render_template("services.html", title="Services")


@app.route('/contact')
def contact():
    return render_template("contact.html", title="Contact")


@app.route('/faq')
def faq():
    return render_template("faq.html", title="FAQ")


@app.route('/login')
def login():
    return render_template("login.html", title="Login")


@app.route('/register')
def register():
    return render_template("register.html", title="Register")


@app.route('/pricing')
def pricing():
    return render_template("pricing.html", title="Pricing")


@app.route('/project')
def project():
    return render_template("project.html", title="Project")


@app.route('/rating', methods=['GET', 'POST'])
def rating():
    if request.method == 'POST':
        customer = request.form['customer']
        email = request.form['email']
        service = request.form['service']
        star = request.form['star']
        comments = request.form['comments']
        # print(customer, email, service, star, comments)
        if customer == '' or email == '':
            # flash(f'Please enter required fields', 'danger')
            # return render_template('rating.html')
            return render_template('rating.html', message='Please enter required fields')
        return render_template('success.html')
    return render_template("rating.html", title="Rate Us")


@app.route('/thanks')
def thanks():
    return render_template("success.html", title="Thanks")





