from database import db


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    value = db.Column(db.Float(), nullable=False)
    company = db.Column(db.Integer(), db.ForeignKey('company.id'))
