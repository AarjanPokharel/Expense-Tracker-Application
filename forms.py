from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField, SelectField, PasswordField,
                     TextField, TextAreaField, SubmitField, IntegerField, FileField, ValidationError, DateField, DecimalField)

# from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, EqualTo, Required
from flask_wtf.file import FileField, FileAllowed
from categories import cats
from models import Users


class profiles(FlaskForm):
    name = StringField('Name')
    email = StringField('Email')
    image = FileField('Update Image', validators=[
                      FileAllowed(['jpg', 'png', 'jpeg','jfif'])])
    budget = IntegerField('Monthly Budget', validators=[DataRequired()])
    income = IntegerField('Monthly Income', validators=[DataRequired()])
    submit = SubmitField('Update')


class loginForm(FlaskForm):
    email1 = StringField('Email', validators=[DataRequired(), Email(message=('Not a valid email address!'))])
    password1 = PasswordField('Password', validators=[DataRequired()])
    submit1 = SubmitField('Log In')


class registrationForm(FlaskForm):
    username2 = StringField('UserName', validators=[DataRequired()])
    email2 = StringField('Email', validators=[DataRequired(), Email(message=('Not a valid email address!'))])
    password2 = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'pass_confirm', message='Passwords must match')])
    pass_confirm = PasswordField(
        'Confirm Password', validators=[DataRequired()])
    submit2 = SubmitField('Register')

    def check_email(self, field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')


class transactionForm(FlaskForm):
    amount = IntegerField('Amount', validators=[DataRequired()])
    date = DateField('Date of Transaction', validators=[DataRequired(), ], format='%d/%m/%Y', render_kw={'placeholder': '2/1/2022 for January 2, 2022'})
    description = TextField('Description', validators=[DataRequired()])
    flow = RadioField('flow', coerce=int, choices=[
                      (1, 'Income'), (2, 'Expense')], validators=[DataRequired()])
    submit = SubmitField('Add Transaction')
    category = SelectField(
        u'Category', choices=cats, validators=[DataRequired()])
