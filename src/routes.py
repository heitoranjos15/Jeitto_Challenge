from src.views import search, make_recharge


def add_routes(api):
    api.add_resource(
        search.CompanyProductsById,
        '/CompanyProducts/<int:company>',
        endpoint="get_company_products_by_id"
    )
    api.add_resource(
        search.ListCompaniesProducts,
        '/CompanyProducts',
        endpoint="list_company_products"
    )
    # api.add_resource(
    #     search.Recharge,
    #     '/PhoneRecharges/<int:id>',
    #     endpoint="get_recharge_by_id"
    # )
    # api.add_resource(
    #     search.Recharge,
    #     '/PhoneRecharges/<string:phone_number>',
    #     endpoint="list_phone_recharges"
    # )
    # api.add_resource(
    #     MakeRecharge,
    #     '/PhoneRecharges',
    #     endpoint="phone_recharge"
    # )
