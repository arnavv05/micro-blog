from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Sign In")

class RegForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    re_password = PasswordField("Re-enter Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")
    
    def validate_username(self, username):
        query = sa.select(User).where(User.username==username.data)
        user = db.session.scalar(query)
        if user is not None:
            raise ValidationError("Please choose a different username.")
        
    def validate_email(self, email):
        query = sa.select(User).where(User.email==email.data)
        user_email = db.session.scalar(query)
        if user_email is not None:
            raise ValidationError("Please use a different email address.")