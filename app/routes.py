from flask import render_template, url_for, flash, redirect, request
from app.forms import LoginForm, RegistrationForm, CreateCompanyForm
from app.models import User, Company
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user
from app import app
from .database import db

PARAMETERS = {'title': 'Test'
              }


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', **PARAMETERS)


@app.route('/company/<companyId>')
def company(companyId):
    company = Company.query.filter_by(id=companyId).first()
    PARAMETERS['title'] = f"{company.companyName} - on Test"
    PARAMETERS['logoPic'] = url_for("static", filename="images/test_logo.png")
    PARAMETERS['companyName'] = company.companyName
    PARAMETERS['tagLine'] = company.tagLine
    PARAMETERS['foreword'] = company.foreword
    PARAMETERS['workWithUs'] = company.workWithUs
    PARAMETERS['aboutUs'] = company.aboutUs
    return render_template('company.html', **PARAMETERS)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('No user found')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    PARAMETERS['form'] = form
    return render_template('login.html', **PARAMETERS)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Поздравляю, вы зарегистрированы!')
        return redirect(url_for('login'))
    PARAMETERS['form'] = form
    return render_template('register.html', **PARAMETERS)


@app.route('/createCompany', methods=['GET', 'POST'])
def createcompany():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    form = CreateCompanyForm()
    if form.validate_on_submit():
        company = Company(companyName=form.companyName.data,
                          tagLine=form.tagLine.data,
                          foreword=form.foreword.data,
                          aboutUs=form.aboutUs.data,
                          workWithUs=form.workWithUs.data
                          )
        db.session.add(company)
        db.session.commit()
        flash('Поздравляю ваша компания создана!')
    PARAMETERS['form'] = form
    return render_template('createcompany.html', **PARAMETERS)
