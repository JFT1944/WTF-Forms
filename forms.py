from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import AnyOf, URL, Optional, NumberRange

class AddNewPet(FlaskForm):
    '''Form for adding adoption worthy animals'''

    name = StringField("name")
    species = StringField("species", validators=[AnyOf(values=['cat', 'dog', 'porcupine'])])
    picture = StringField("picture ", validators=[Optional(), URL()])
    age = FloatField("Age of Animal", validators=[NumberRange(min=0, max=30)])
    notes = StringField("notes")
    # available = BooleanField("Avalable")

    # def validate_species():

class Edit_Pet(FlaskForm):
    '''FORM FOR EDITING ADOPTION WORTHY ANIMALS'''

    picture = StringField("picture ", validators=[Optional(), URL()])
    notes = StringField("notes")
    available = BooleanField("Available")