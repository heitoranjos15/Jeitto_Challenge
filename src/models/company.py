from database import db


class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
