from flask import Flask, render_template, session, request, redirect, flash
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from models import db, connect_db, Pet
from forms import AddNewPet, Edit_Pet

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'Big Time Secret'


app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'cows'

connect_db(app)
app.app_context().push()




@app.route('/')
def home():
    '''RENDERS THE HOMEPAGE'''
    pets = Pet.query.all()
    print(pets)
    return render_template('home.html', pets=pets)
    

    # , pets=pets

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    '''This route adds a new pet to the DB'''
    form = AddNewPet()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        picture = form.picture.data
        age = form.age.data
        notes = form.notes.data
        # available = form.available.data
        newPet = Pet(name=name, species=species, photo_url=picture, age=age, notes=notes)
        db.session.add(newPet)
        db.session.commit()
        return redirect('/')
    
    else:
        return render_template('newpet.html', form=form)

@app.route('/<int:petid>', methods=['POST', 'GET'])
def pet_edit(petid):
    '''This route edits the already created Pet'''
    single_pet = Pet.query.get(petid)

    form = Edit_Pet()

    if form.validate_on_submit():
        picture = form.picture.data
        notes = form.notes.data
        available = form.available.data
        print(single_pet.notes)
        print(picture)
        print(notes)
        print(available)

# The following allows for the photos, notes and availability to be changed

        if picture != "":
            single_pet.photo_url = picture
            print('printing picture')
            print(single_pet.photo_url)
            # return ""
        if notes != "":
            single_pet.notes = notes
            print('printing notes')
            print(single_pet.notes)
            # return ""
        if available == True:
            single_pet.available = False
            print('printing available')
            # return ""
        print(single_pet.notes)
        db.session.add(single_pet)
        print(single_pet)
        db.session.commit()
        return redirect('/')


    else:    
        return render_template('pet_page.html', single_pet=single_pet, form=form)