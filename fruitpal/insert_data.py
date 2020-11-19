"""
Data ingestion service to insert data into our database and keep it updated.
"""

from requests import request

BASE = "http://localhost:5001/"

#  Inserting Mango
print('Inserting Mango')
response = request(method='PUT', url=BASE + "api/fruitpal?commodity=mango&country=MX&fixed_overhead=32&variable_overhead=1.24")
print(response.status_code, response.json())
response = request(method='PUT', url=BASE + "api/fruitpal?commodity=mango&country=BR&fixed_overhead=20&variable_overhead=1.42")
print(response.status_code, response.json())

#  Inserting Apple
print('Inserting Apple')
response = request(method='PUT', url=BASE + "api/fruitpal?commodity=apple&country=GB&fixed_overhead=15&variable_overhead=0.98")
print(response.status_code, response.json())

# Inserting Banana
print('Inserting Banana')
response = request(method='PUT', url=BASE + "api/fruitpal?commodity=banana&country=US&fixed_overhead=18&variable_overhead=0.29")
print(response.status_code, response.json())

# Inserting Orange
print('Inserting Orange')
response = request(method='PUT', url=BASE + "api/fruitpal?commodity=orange&country=CN&fixed_overhead=8&variable_overhead=0.45")
print(response.status_code, response.json())
response = request(method='PUT', url=BASE + "api/fruitpal?commodity=orange&country=US&fixed_overhead=16&variable_overhead=1.95")
print(response.status_code, response.json())
response = request(method='PUT', url=BASE + "api/fruitpal?commodity=orange&country=GB&fixed_overhead=19&variable_overhead=2.05")
print(response.status_code, response.json())
response = request(method='PUT', url=BASE + "api/fruitpal?commodity=orange&country=RU&fixed_overhead=14&variable_overhead=1.12")
print(response.status_code, response.json())
response = request(method='PUT', url=BASE + "api/fruitpal?commodity=orange&country=MX&fixed_overhead=12&variable_overhead=1.05")
print(response.status_code, response.json())
response = request(method='PUT', url=BASE + "api/fruitpal?commodity=orange&country=BR&fixed_overhead=13&variable_overhead=1.18")
print(response.status_code, response.json())

# Inserting invalid or bad data
print('Inserting invalid or bad data')
response = request(method='PUT', url=BASE + "api/fruitpal?commodity=orange&fixed_overhead=8&variable_overhead=0.45")
print(response.status_code, response.json())
response = request(method='PUT', url=BASE + "api/fruitpal?commodity=orange&country=US&fixed_overhead=1aa6&variable_overhead=1.95")
print(response.status_code, response.json())
response = request(method='PUT', url=BASE + "api/fruitpal?commodity=orange&country=GB&fixed_overhead=19&variable_overhead=2.aa05")
print(response.status_code, response.json())

