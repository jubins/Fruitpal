from flask import Flask
from flask_restful import Api, Resource, marshal_with
from flask_sqlalchemy import SQLAlchemy

from validators import GetTradeRequestArgs, PutTradeRequestArgs
from models import PricingModel, ResourceFields


app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fruitpal.db"
db = SQLAlchemy(app)


class CommodityModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(10), nullable=False)
    commodity = db.Column(db.String(100), nullable=False)
    fixed_overhead = db.Column(db.Numeric(10, 5), nullable=False)
    variable_overhead = db.Column(db.Numeric(10, 5), nullable=False)
    __table_args__ = (db.UniqueConstraint('country', 'commodity', 'fixed_overhead', 'variable_overhead', name='_ccountry_commodity_overheads_uc'),
                      )

    def __repr__(self):
        return f"id={self.id}, country={self.country}, fixed_overhead={self.fixed_overhead}, variable_overhead={self.variable_overhead}"


class Trade(Resource):
    def get(self):
        args = GetTradeRequestArgs()
        results = CommodityModel.query.filter_by(commodity=args.get('commodity')).all()
        response = {'obj': {'data': list(), 'length': len(results)}}
        country_to_price = dict()
        country_to_formula = dict()
        for result in results:
            country = getattr(result, 'country')
            total_price, formula = PricingModel.compute_fixed_overhead(args.get('price'),
                                                              args.get('volume'),
                                                              getattr(result, 'variable_overhead'))
            country_to_price[country] = float(total_price)
            country_to_formula[country] = formula
        sorted_country_to_price = sorted(country_to_price, key=country_to_price.get, reverse=True)
        for country in sorted_country_to_price:
            response['obj']['data'].append({'country': country,
                                            'total_price': "{:.2f}".format(country_to_price.get(country)),
                                            'formula': country_to_formula.get(country),
                                            })
        return response

    @marshal_with(ResourceFields.put_schema())
    def put(self):
        try:
            args = PutTradeRequestArgs()
            commodity = CommodityModel(
                id=args.get('id'),
                commodity=args.get('commodity'),
                country=args.get('country'),
                fixed_overhead=args.get('fixed_overhead'),
                variable_overhead=args.get('variable_overhead')
            )
            db.session.add(commodity)
            db.session.commit()
            return commodity, 201
        except Exception as err:
            return "Record already exists in the database", 400


api.add_resource(Trade, '/api/fruitpal')
db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=90, debug=True)

