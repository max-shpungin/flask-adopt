"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, TextAreaField
from wtforms.validators import Optional, InputRequired

class AddPetForm(FlaskForm):
    """Form to add a pet."""

    name = StringField(
        "Name",
        validators=[InputRequired()])

    species = StringField(
        "Species",
        validators=[InputRequired()])

    photo_url = StringField(
        "Photo url",
        validators=[Optional()]) # Validate url?

    age = SelectField(
        "Age",
        validators=[InputRequired()],
        choices=[
            ('baby', 'baby'),
            ('young', 'young'),
            ('adult', 'adult'),
            ('senior', 'senior')]
    )

    notes = TextAreaField(
        "Notes",
        validators=[Optional()]
    )