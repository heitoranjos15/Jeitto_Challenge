from src.models.company import Company
from src.models.product import Product
from database import db


def get_companies():
    response = Company.query.filter().all()
    return response


def get_products_by_company(company):
    response = Product.query.filter(Product.company == company).all()
    return response


def get_company_with_products_by_id(company_id):
    response = Company.query.join(
        Product,
        Company.id == Product.company
    ).filter(Company.id == company_id).first()
    return response
