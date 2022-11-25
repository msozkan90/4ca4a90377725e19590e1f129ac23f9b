from flask import Flask,render_template,request
import requests
import os
from dotenv import load_dotenv
load_dotenv() 
app = Flask(__name__)

base="TRY"

def get_date_currency_api_1(date):
    if date == "":
        response = requests.request("GET", f"https://api.apilayer.com/exchangerates_data/latest?symbols=&base={base}", headers={"apikey": "DLDK3ipbf0Lo85OVjj5pchPyDfLk1HOS"}, data = {})
    else:
        response = requests.request("GET", f"https://api.apilayer.com/exchangerates_data/{date}?symbols=EUR%2CUSD%2CTRY&base={base}", headers={"apikey": "DLDK3ipbf0Lo85OVjj5pchPyDfLk1HOS"}, data = {})
    result = response.json()
    currency_list=[result["rates"]["TRY"],result["rates"]["EUR"],result["rates"]["USD"]]
    return currency_list

def get_date_currency_api_2(date):
    if date == "":   
        response = requests.request("GET", f"https://api.freecurrencyapi.com/v1/latest?apikey=1zlJTNqgEBcVtQQsZfcFslbgln3CE0KzpAykQL94&base_currency={base}", headers={"apikey": "1zlJTNqgEBcVtQQsZfcFslbgln3CE0KzpAykQL94"}, data = {})
        result = response.json()
        currency_list=[result["data"]["TRY"],result["data"]["EUR"],result["data"]["USD"]]
    else:
        response = requests.request("GET", f"https://api.freecurrencyapi.com/v1/historical?apikey=1zlJTNqgEBcVtQQsZfcFslbgln3CE0KzpAykQL94&date_from={date}&date_to={date}&base_currency={base}", headers={"apikey": "1zlJTNqgEBcVtQQsZfcFslbgln3CE0KzpAykQL94"}, data = {})
        result = response.json()
        currency_list=[result["data"][date]["TRY"],result["data"][date]["EUR"],result["data"][date]["USD"]]
    return currency_list

def get_all_currency(date):
    TRY=[]
    USD=[]
    EUR=[]
    list1=get_date_currency_api_1(date)
    list2=get_date_currency_api_2(date)
    TRY.append(list1[0])
    TRY.append(list2[0])
    EUR.append(list1[1])
    EUR.append(list2[1])
    USD.append(list1[2])
    USD.append(list2[2])
    usd=1/min(USD)
    tl=1/min(TRY)
    eur=1/min(EUR)
    return [tl,usd,eur]

# @app.route("/",methods = ["GET","POST"])
# def index():

#     zipList=""
#     name_curr=["TL","USD","EUR"]
#     date=""
#     result=get_all_currency(date)
#     zipList=zip(name_curr,result)
#     if request.method == "POST":
#         date=request.form['date']
#         result=get_all_currency(date)
#         zipList_date=zip(name_curr,result)
#         return render_template("index.html",zipList_date=zipList_date,zipList=zipList)
#     return render_template("index.html",zipList=zipList)


@app.route("/",methods = ["GET","POST"])
def index():
    
    zipList= os.getenv("BASE_URL_API_1")
    zipList2= os.getenv("BASE_URL_API_2")
    print(zipList)
    print(zipList2)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
