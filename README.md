# Currency App

Currency App is an application that allows you to follow the exchange rates instantly or according to a date you specify.

## Installation
First of all we need to create virtual environment.
```bash
python -m venv venv (windows)
python3 -m venv venv (macOS)
```
You need to change .env_example file name to .env
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install inside of requirements.
You can run the application easily with below code

```bash
your_file_path/venv/Scripts/Activate.ps1 (windows)
source/venv/bin/activate (macOS)
```
- After setup and activate virtual environment. We need to install requirements.txt
```bash
pip install -r requirements.txt
```

## Usage
- You can run the application easily with below code
```python
flask run
```
- If you want to add new api to application follow the below description.
- You need to add below function to CurrencyClass in app.py. After add below function you need to give own api values to the variables.

```python

def your_function_name(self,date):
    if date == "":   
        response = requests.request("GET","YOUR-API-URL-FOR-LATEST-CURRENCY", headers={"YOUR-API-KEY"}, data = {})
        result = response.json()
        currency_list=[result["YOUR-API-RESPONSE-TITLE"][os.getenv('CURRENCY_1')],result["YOUR-API-RESPONSE-TITLE"][os.getenv('CURRENCY_2')],result["YOUR-API-RESPONSE-TITLE"][os.getenv('CURRENCY_3')]]
    else:
        response = requests.request("GET", "YOUR-API-URL-FOR-HISTORICAL-CURRENCY", headers={"YOUR-API-KEY"}, data = {})
        result = response.json()
        currency_list=[result["YOUR-API-RESPONSE-TITLE"][date][os.getenv('CURRENCY_1')],result["YOUR-API-RESPONSE-TITLE"][date][os.getenv('CURRENCY_2')],result["YOUR-API-RESPONSE-TITLE"][date][os.getenv('CURRENCY_3')]]
    self.make_list(currency_list)

```
- YOUR-API-URL-FOR-LATEST-CURRENCY = Your api's URL for latest currency values (you need to write this input like example given below.)
- Example 
```python
You need to configure your path like this example
BASE_URL_API_2 = https://api.freecurrencyapi.com/v1/
API_KEY_2 = Your api key
BASE_CURRENCY = change from .env file
"{}latest?apikey={}&base_currency={}".format(os.getenv("BASE_URL_API_2"),os.getenv("API_KEY_2"),os.getenv("BASE_CURRENCY"))
```
- YOUR-API-URL-FOR-HISTORICAL-CURRENCY = Your api's URL for historical currency values (you need to write this input like example given below.)
- Example 
```python
You need to configure your path like this example
BASE_URL_API_2 = https://api.freecurrencyapi.com/v1/
API_KEY_2 = Your api key
BASE_CURRENCY = change from .env file
"{}historical?apikey={}&date_from={}&date_to={}&base_currency={}".format(os.getenv("BASE_URL_API_2"),os.getenv("API_KEY_2"),date,date,os.getenv("BASE_CURRENCY"))
Another example your historical path maybe different like this example. You need to configure.
"{}/{}?symbols={}%2C{}%2C{}&base={}".format(os.getenv("BASE_URL_API_1"),date,os.getenv("CURRENCY_2"),os.getenv("CURRENCY_3"),os.getenv("CURRENCY_1"),os.getenv("BASE_CURRENCY"))
```
- YOUR-API-KEY=Your api key
- YOUR-API-RESPONSE-TITLE = When you request your api, the api return a response. The response has a title of currency like rates or data. Write here your own api's title
- After write your function you need to run your function like below.
```python
def run_all(self,date):
    self.func1(date)
    self.func2(date)

    self.your_function_name(date)  #here

    return [(1/min(self.TRY)),(1/min(self.USD)),(1/min(self.EUR))]
```
- If you want to change base currency or currency you can change from .env file
```python
BASE_CURRENCY="TRY"
CURRENCY_1="TRY"
CURRENCY_2="EUR"
CURRENCY_3="USD"
```


## License

[MIT](https://choosealicense.com/licenses/mit/)