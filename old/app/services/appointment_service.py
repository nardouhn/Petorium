from app.models.appointment_model import Appointment
from app.extensions import db

def create_appointment(pet_id, user_id, doctor_id, date):
    appointment = Appointment(
        pet_id=pet_id,
        user_id=user_id,
        doctor_id=doctor_id,
        date=date
    )
    db.session.add(appointment)
    db.session.commit()
    return appointment
