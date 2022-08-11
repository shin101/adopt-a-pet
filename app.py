from flask import Flask, request, render_template, redirect, flash, url_for
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
#below code won't change any behavior but gets rid of annoying messsage otherwise SQLAlchemy will yell at you
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'hihi'

# will print out SQL version of what you just typed in python
app.config['SQLALCHEMY_ECHO'] = True
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all() 

@app.route('/')
def homepage():
    pets = Pet.query.all()
    return render_template("/homepage.html",pets=pets)

@app.route('/add',methods=['GET','POST'])
def pet_form():
    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash('added new pet')
        return redirect('/')
    else:
        return render_template("/form.html", form=form)

@app.route('/display/<int:pet_id>', methods=['GET','POST'])
def display_form(pet_id):
    """page that shows some information about the pet"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.add(pet)
        db.session.commit()
        flash('successfully edited pet')
        return redirect(('/'))
    else:
        return render_template("/display.html", form=form, pet=pet)
