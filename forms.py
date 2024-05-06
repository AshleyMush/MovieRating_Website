from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL, Email, Length, ValidationError, InputRequired

class RateMovieForm(FlaskForm):
    rating = StringField(label="Your Rating Out of 10 e.g 7.5", validators=[DataRequired()])
    review = TextAreaField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Submit")