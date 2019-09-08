from datetime import datetime
from database import db


class Recharge(db.Model):
    __tablename__ = 'recharge'
    id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    company = db.Column(db.Integer(), db.ForeignKey('company.id'))
    product = db.Column(db.Integer(), db.ForeignKey('product.id'))
    phone_number = db.Column(db.String(13))
