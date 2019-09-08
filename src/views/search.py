from sqlalchemy.orm.exc import NoResultFound
from flask_api import status
from flask_restful import Resource, abort
from flask import request, current_app, jsonify

from db_client import (get_company_with_products_by_id,
                       get_companies,
                       get_products_by_company)


class CompanyProductsById(Resource):
    def get(self, company):
        response = None
        if company:
            try:
                response = get_company_with_products_by_id(company)
            except Exception as e:
                abort(status.HTTP_500_INTERNAL_SERVER_ERROR, message=str(e))
        if not response:
            return abort(status.HTTP_400_BAD_REQUEST)
        return jsonify(response)


class ListCompaniesProducts(Resource):
    def get(self):
        companies = None
        reponse_dict = []
        try:
            companies = get_companies()
        except Exception as e:
            abort(status.HTTP_500_INTERNAL_SERVER_ERROR, message=str(e))
        if not companies:
            return abort(status.HTTP_400_BAD_REQUEST)

        for company in companies:
            response_dict.update({company.name: []})
            product = {}
            try:
                product = 
            except Exception as e:
                abort(status.HTTP_500_INTERNAL_SERVER_ERROR, message=str(e))
