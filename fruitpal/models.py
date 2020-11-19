from flask_restful import fields


class ResourceFields(object):
    def __init__(self):
        pass

    @staticmethod
    def put_schema():
        return {
            'id': fields.Integer,
            'country': fields.String,
            'commodity': fields.String,
            'fixed_overhead': fields.Float,
            'variable_overhead': fields.Float,
        }


class PricingModel(object):
    def __init__(self):
        pass

    @staticmethod
    def compute_fixed_overhead(price, volume, overhead):
        return (price+overhead)*volume, f"({overhead:.2f} + {price}) * {volume}"

    @staticmethod
    def compute_variable_overhead(price, volume, overhead):
        return (price+overhead)*volume
