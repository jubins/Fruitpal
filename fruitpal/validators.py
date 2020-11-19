from flask_restful import reqparse


def GetTradeRequestArgs():
    get_trade_args = reqparse.RequestParser()
    get_trade_args.add_argument("commodity", type=str, help="Commodity name is required and must be a string.", required=True)
    get_trade_args.add_argument("price", type=int, help="Price of the commodity is required and must be an integer.", required=True)
    get_trade_args.add_argument("volume", type=int, help="Volume of the commodity is required and must be an integer.", required=True)
    return get_trade_args.parse_args()


def PutTradeRequestArgs():
    put_trade_args = reqparse.RequestParser()
    put_trade_args.add_argument("id", type=int, help="Commodity id is required and must be an integer.", required=False)
    put_trade_args.add_argument("commodity", type=str, help="Commodity name is required and must be a string.", required=True)
    put_trade_args.add_argument("country", type=str, help="Country of the commodity is required and must be a string.", required=True)
    put_trade_args.add_argument("fixed_overhead", type=float, help="Fixed overhead of the commodity is required and must be a float.", required=True)
    put_trade_args.add_argument("variable_overhead", type=float, help="Variable overhead of the commodity is required and must be a float.", required=True)
    return put_trade_args.parse_args()
