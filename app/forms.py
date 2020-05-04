from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_wtf.file import FileRequired, FileAllowed
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class CreateCompanyForm(FlaskForm):
    companyName = StringField('Название компании', validators=[DataRequired()])
    logoCompany = FileField('Логотип', validators=[FileAllowed(['jpg', 'png', 'bmp' 'jpeg'])])
    tagLine = TextAreaField('Слоган', validators=[DataRequired()])
    foreword = TextAreaField('Предисловие', validators=[DataRequired()])
    aboutUs = TextAreaField('Секция "О нас"', validators=[DataRequired()])
    workWithUs = TextAreaField('Секция "Работа с нами"', validators=[DataRequired()])
    firstGameName = StringField('Название для первой игры')
    firstGamePicture = FileField('Картинка для первой игры', validators=[FileAllowed(['jpg', 'png', 'bmp' 'jpeg'])])
    secondGameName = StringField('Название для второй игры')
    secondGamePicture = FileField('Картинка для второй игры', validators=[FileAllowed(['jpg', 'png', 'bmp' 'jpeg'])])
    thirdGameName = StringField('Название для третьей игры')
    thirdGamePicture = FileField('Картинка для третьей игры', validators=[FileAllowed(['jpg', 'png', 'bmp' 'jpeg'])])
    submit = SubmitField('Создать компанию')

    def validate_companyName(self, companyName):
        pass
        # user = User.query.filter_by(username=username.data).first()
        # company = Company.query.filter_by(companyName=companyName.data).first()
        # if company is not None:
        #     raise ValidationError('Please use a different company name.')
