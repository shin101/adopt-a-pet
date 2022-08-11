from unicodedata import name
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    name = StringField("Animal Name", validators=[InputRequired()],)
    species = SelectField("Animal Species", choices=[("cat","Cat"),("dog","Dog"),("porcupine", "Porcupine")], validators=[InputRequired()],)
    photo_url = StringField("Photo URL",validators=[Optional(),URL()],)
    age = IntegerField("Age of Pet", validators=[Optional(),NumberRange(min=0, max=30,message="num must be between 0 to 30")],)
    notes = TextAreaField("Notes Section", validators=[Optional(),Length(min=10)],)

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL",validators=[Optional(),URL()],)
    notes = TextAreaField("Notes Section", validators=[Optional(),Length(min=10)],)
    available = BooleanField("Availability")




    