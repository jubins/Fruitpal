from requests import request

BASE = "http://localhost:5001/"


response = request(method='GET', url=BASE + "api/fruitpal?commodity=mango&price=53&volume=405")
print(response.json())

response = request(method='GET', url=BASE + "api/fruitpal?commodity=orange&price=35&volume=500")
print(response.json())
#
response = request(method='GET', url=BASE + "api/fruitpal?commodity=apple&price=45&volume=100")
print(response.json())

response = request(method='GET', url=BASE + "api/fruitpal?commodity=grape&price=4r5&volume=100")
print(response.json())
