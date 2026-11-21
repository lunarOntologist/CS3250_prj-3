from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length, NumberRange, ValidationError
from wtforms.fields import DateTimeLocalField


class SignUpForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(min=2, max=80)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    passwd = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=8)]
    )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    passwd = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
    submit = SubmitField('Login')


class CreateEventForm(FlaskForm):
    title = StringField(
        'Event Title',
        validators=[DataRequired(), Length(min=3, max=120)]
    )
    description = TextAreaField(
        'Description',
        validators=[DataRequired(), Length(min=5)]
    )
    location = StringField(
        'Location',
        validators=[DataRequired(), Length(min=2, max=200)]
    )
    start_time = DateTimeLocalField(
        'Start Time',
        format='%Y-%m-%dT%H:%M',
        validators=[DataRequired()]
    )
    end_time = DateTimeLocalField(
        'End Time',
        format='%Y-%m-%dT%H:%M',
        validators=[DataRequired()]
    )
    capacity = IntegerField(
        'Capacity',
        validators=[DataRequired(), NumberRange(min=1, message='Capacity must be at least 1.')]
    )
    submit = SubmitField('Create Event')

    def validate_end_time(self, field):
        if self.start_time.data and field.data and field.data <= self.start_time.data:
            raise ValidationError('End time must be after start time.')