from app.extensions import db

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=True)
    
    appointments = db.relationship('Appointment', backref='doctor', lazy=True)
