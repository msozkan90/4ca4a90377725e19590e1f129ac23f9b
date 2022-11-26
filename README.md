# 4ca4a90377725e19590e1f129ac23f9b


# Currency App


Currency App is an application that allows you to follow the exchange rates instantly or according to a date you specify.

## Installation
First of all we need to create virtual environment.
```bash
python -m venv venv (windows)
python3 -m venv venv (macOS)
```

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
- You need to add below function to CurrencyClass. After add below function you need to give own api values to the variables.

```python

def your_function_name(self,date):
    if date == "":   
        response = requests.request("GET","YOUR-API-URL-FOR-LATEST-CURRENCY", headers={"YOUR-API-KEY"}, data = {})
        result = response.json()
        currency_list=[result["YOUR-API-RESPONSE-TITLE"][os.getenv('CURRENCY_1')],result["YOUR-API-RESPONSE-TITLE"][os.getenv('CURRENCY_2')],result["YOUR-API-RESPONSE-TITLE"][os.getenv('CURRENCY_3')]]
    else:
        response = requests.request("GET", "YOUR-API-URL-FOR-LATEST-CURRENCY", headers={"YOUR-API-KEY"}, data = {})
        result = response.json()
        currency_list=[result["YOUR-API-RESPONSE-TITLE"][date][os.getenv('CURRENCY_1')],result["YOUR-API-RESPONSE-TITLE"][date][os.getenv('CURRENCY_2')],result["YOUR-API-RESPONSE-TITLE"][date][os.getenv('CURRENCY_3')]]
    self.make_list(currency_list)

```
- YOUR-API-URL-FOR-LATEST-CURRENCY = Your api's URL for latest currency values 
- YOUR-API-KEY=Your api key
- YOUR-API-RESPONSE-TITLE = When you request your api, the api return a response. The response has a title of currency like rates or data. Write here your own api's title



## License

[MIT](https://choosealicense.com/licenses/mit/)