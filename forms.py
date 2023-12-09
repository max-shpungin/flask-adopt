"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, TextAreaField
from wtforms.validators import Optional, InputRequired, AnyOf, URL

class AddPetForm(FlaskForm):
    """Form to add a pet."""

    name = StringField(
        "Name",
        validators=[InputRequired()])

    species = StringField(
        "Species",
        validators=[InputRequired(),
                    AnyOf(values=[
                        'cat',
                        'dog',
                        'porcupine'])]
    )

    photo_url = StringField(
        "Photo url",
        validators=[Optional(), URL()])

    age = SelectField(
        "Age",
        validators=[InputRequired(),
                    AnyOf(values=[
                        'baby',
                        'young',
                        'adult',
                        'senior'])],
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
