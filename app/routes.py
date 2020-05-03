from flask import render_template, url_for, flash, redirect
from app.forms import LoginForm
from app.models import User
from flask_login import current_user, login_user
from app import app

PARAMETERS = {'title': 'Test'
              }

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', **PARAMETERS)


@app.route('/company/<companyName>')
def company(companyName):
    PARAMETERS['title'] = f"{companyName} - on Test"
    PARAMETERS['logoPic'] = url_for("static", filename="images/test_logo.png")
    PARAMETERS['companyName'] = companyName
    return render_template('company.html', **PARAMETERS)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    PARAMETERS['form'] = form
    return render_template('login.html', **PARAMETERS)
