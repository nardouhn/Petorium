from app.models.pet_model import Pet
from app.extensions import db

def create_pet(name, species, breed, age, owner_id):
    pet = Pet(
        name=name,
        species=species,
        breed=breed,
        age=age,
        owner_id=owner_id
    )
    db.session.add(pet)
    db.session.commit()
    return pet

def get_pets_by_user(user_id):
    return Pet.query.filter_by(owner_id=user_id).all()
