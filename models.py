"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

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


####################HELPERS##########################

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)
