"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get("/")
def display_homepage():
    """Shows page about pet details."""
    pets = Pet.query.all()

    return render_template("list.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Processes form submission for adding new pets."""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data

        new_pet = Pet(
            name= name,
            species=species,
            photo_url=photo_url,
            age=age,
        )

        db.session.add(new_pet)
        db.session.commit()

        flash (f"Everyone say hi to {name}!!!")
        return redirect('/')

    else: #we're explicit because we want to be leave us alone
        return render_template('/add-pet.html', form=form)


