# Fruitpal

A tool for trading tropical fruits which allows a trader to understand the full
cost of buying fruit from various countries of origin.

### Setup
1. **Start the server**: Type `docker-compose up --build` to start the server. Make sure you are in the main project directory that contains the `docker-compose.yml` file and have docker/docker-compose installed and running.
2. **Insert the data**: Next step is to insert data in our database, for that go the fruitpal directory and run `insert_data.py` script.
    ```
    Type below commands in terminal or command prompt and make sure you have Python 3 installed:
    $ cd fruitpal
    $ python insert_data.py
    ```
    If you get an import error for `requests` module, follow below steps:
    
    Create a virtual environment in Python and activate it using below commands
    ```
    $ python3 -m venv venv
    $ source/venv/bin/active
    ```
    Install the `requests` module using below command
    ```
    pip install requests==2.25.0
    ```
    Follow Step 2 again.
    
    Once the script is run successfully, data is inserted into the SQLite database. I have created a separate API call just to ingest data to make service more scalable. Below is an example API call `insert_data.py` makes. 
    ```
    PUT /api/fruitpal?commodity=mango&country=MX&fixed_overhead=32&variable_overhead=1.24
    ```
3. **Run the tests**: Run the test cases using below command. Response is sorted by total cost from highest to lowest. Look at the input and output section below for more details.
    ```
    $ python tests.py
    ```

### Input
A trader using this tool will specify the contemplated purchase, including:
1. The commodity (e.g. mangos)
2. The price per ton (in dollars)
3. The trade volume (in tons)

Example:
A trader who wants to know the full cost of buying 405 tons of mangos at $53 a ton would make API call that would look like this:
```text
GET /api/fruitpal?commodity=mango&price=53&volume=405
```
You can try below in your browser (feel free to change commodity, price or volume in the API call):
```
http://localhost:5001/api/fruitpal?commodity=mango&price=53&volume=405
```

### Output
The API response is a list of all available countries of origin, and, for each:
- The country code
- The total cost of the purchase
The list is sorted by total cost from highest to lowest.

Example:

In response to the example input, the trader would see following output of the API:
```json
{
    "obj": {
        "length": 2,
        "data": [
            {
                "country": "BR",
                "total_price": "22040.1",
                "formula": "(1.42 + 34) * 500"
            },
            {
                "country": "MX",
                "total_price": "21967.2",
                "formula": "(1.24 + 34) * 500"
            }
        ]
    }
}
```

This means the 405 tons of mangos would cost $22,040.10 if bought in Brazil and $21,967.20 if
bought in Mexico.


### Contact
- Jubin Soni
- jubinsoni27@gmail.com