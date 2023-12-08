"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import CheckConstraint

db = SQLAlchemy()


class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )

    name = db.Column(
        db.String(50),
        nullable=False
    )

    species = db.Column(
        db.String(50),
        nullable=False
    )

    photo_url = db.Column(
        db.Text,
        default='',
        nullable=False
    )

    age = db.Column(
        db.String(6),
        db.CheckConstraint('baby', 'young', 'adult', 'senior'), # TODO: check syntax
        nullable=False
    )

    notes = db.Column(
        db.Text,
        nullable=True
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )








####################HELPERS##########################

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)
