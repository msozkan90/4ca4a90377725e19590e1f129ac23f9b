from flask import Flask,render_template,request
import requests
import os
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
load_dotenv() 
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
csrf = CSRFProtect(app)

class CurrencyClass():
    def __init__(self,TRY,USD,EUR) -> None:
        self.TRY=TRY
        self.USD=USD
        self.EUR=EUR
    def func1(self,date):
        if date == "":
            response = requests.request("GET", "{}/latest?symbols=&base={}".format(os.getenv("BASE_URL_API_1"),os.getenv("BASE_CURRENCY")), headers={"apikey":os.getenv("API_KEY_1")}, data = {})
        else:
            response = requests.request("GET", "{}/{}?symbols={}%2C{}%2C{}&base={}".format(os.getenv("BASE_URL_API_1"),date,os.getenv("CURRENCY_2"),os.getenv("CURRENCY_3"),os.getenv("CURRENCY_1"),os.getenv("BASE_CURRENCY")), headers={"apikey":os.getenv("API_KEY_1")}, data = {})
        result = response.json()
        currency_list=[result["rates"][os.getenv('CURRENCY_1')],result["rates"][os.getenv('CURRENCY_2')],result["rates"][os.getenv('CURRENCY_3')]]
        self.make_list(currency_list)
        return currency_list
    def func2(self,date):
        if date == "":   
            response = requests.request("GET","{}latest?apikey={}&base_currency={}".format(os.getenv("BASE_URL_API_2"),os.getenv("API_KEY_2"),os.getenv("BASE_CURRENCY")), headers={"apikey":os.getenv("API_KEY_2")}, data = {})
            result = response.json()
            currency_list=[result["data"][os.getenv('CURRENCY_1')],result["data"][os.getenv('CURRENCY_2')],result["data"][os.getenv('CURRENCY_3')]]
        else:
            response = requests.request("GET", "{}historical?apikey={}&date_from={}&date_to={}&base_currency={}".format(os.getenv("BASE_URL_API_2"),os.getenv("API_KEY_2"),date,date,os.getenv("BASE_CURRENCY")), headers={"apikey":os.getenv("API_KEY_2")}, data = {})
            result = response.json()
            currency_list=[result["data"][date][os.getenv('CURRENCY_1')],result["data"][date][os.getenv('CURRENCY_2')],result["data"][date][os.getenv('CURRENCY_3')]]
        self.make_list(currency_list)
    
    def make_list(self,list_curr):
        self.TRY.append(list_curr[0])
        self.USD.append(list_curr[1])
        self.EUR.append(list_curr[2])       
    
    def run_all(self,date):
        self.func1(date)
        self.func2(date)
        return [(1/min(self.TRY)),(1/min(self.USD)),(1/min(self.EUR))]

@app.route("/",methods = ["GET","POST"])
@csrf.exempt
def index():
    zipList=""
    zipList_date=""
    run = CurrencyClass(TRY=[],USD=[],EUR=[])
    result=run.run_all(date="") 
    name_curr=[os.getenv("CURRENCY_1"),os.getenv("CURRENCY_2"),os.getenv("CURRENCY_3")]
    zipList=zip(name_curr,result)
    if request.method == "POST":
        run = CurrencyClass(TRY=[],USD=[],EUR=[])
        date=request.form['date']
        result=run.run_all(date)
        zipList_date=zip(name_curr,result)
        return render_template("index.html",zipList_date=zipList_date,zipList=zipList,base_curr=os.getenv("BASE_CURRENCY"),date=date)
    return render_template("index.html",zipList=zipList,zipList_date=zipList_date,base_curr=os.getenv("BASE_CURRENCY"))

if __name__ == "__main__":
    app.run(debug=True)



