from requests import request
import unittest

BASE = "http://localhost:5001/"


class TestFruitpal(unittest.TestCase):

    def test_given_example(self):
        response = request(method='GET', url=BASE + "api/fruitpal?commodity=mango&price=53&volume=405")
        self.assertEqual(response.status_code, 200)
        expected = {'obj': {'data': [{'country': 'BR', 'total_price': 22040.1}, {'country': 'MX', 'total_price': 21967.2}], 'length': 2}}
        self.assertEqual(response.json(), expected)

    def test_big_response(self):
        response = request(method='GET', url=BASE + "api/fruitpal?commodity=orange&price=35&volume=500")
        self.assertEqual(response.status_code, 200)
        expected = {'obj': {'data': [{'country': 'GB', 'total_price': 18525.0}, {'country': 'US', 'total_price': 18475.0}, {'country': 'BR', 'total_price': 18090.0}, {'country': 'RU', 'total_price': 18060.0}, {'country': 'MX', 'total_price': 18025.0}, {'country': 'CN', 'total_price': 17725.0}], 'length': 6}}
        self.assertEqual(response.json(), expected)

    def test_small_response(self):
        response = request(method='GET', url=BASE + "api/fruitpal?commodity=apple&price=45&volume=100")
        self.assertEqual(response.status_code, 200)
        expected = {'obj': {'data': [{'country': 'GB', 'total_price': 4598.0}], 'length': 1}}
        self.assertEqual(response.json(), expected)

    def test_invalid_params(self):
        response = request(method='GET', url=BASE + "api/fruitpal?commodity=grape&price=4r5&volume=100")
        self.assertEqual(response.status_code, 400)
        expected = {'message': {'price': 'Price of the commodity is required and must be an integer.'}}
        self.assertEqual(response.json(), expected)


def print_given_input():
    response = request(method='GET', url=BASE + "api/fruitpal?commodity=mango&price=53&volume=405")
    print('API call: {}/{}'.format(BASE, 'api/fruitpal?commodity=mango&price=53&volume=405'))
    print('Output: ', response.json())


if __name__ == '__main__':
    print_given_input()
    unittest.main()

