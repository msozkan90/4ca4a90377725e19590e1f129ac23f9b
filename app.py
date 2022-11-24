from flask import Flask,render_template,request
import requests

app = Flask(__name__)

import requests

base="TRY"
date="2020-03-03"

Urls=[ 
    f"https://api.apilayer.com/exchangerates_data/latest?symbols=&base={base}",

     f"https://api.freecurrencyapi.com/v1/latest?apikey=1zlJTNqgEBcVtQQsZfcFslbgln3CE0KzpAykQL94&base_currency={base}",
      
    ]

HistoryUrls=[  
    f"https://api.apilayer.com/exchangerates_data/{date}?symbols=symbols&base={base}",
    f"https://api.freecurrencyapi.com/v1/historical?apikey=1zlJTNqgEBcVtQQsZfcFslbgln3CE0KzpAykQL94&date_from={date}&date_to={date}&base_currency={base}",

    ]


ApiKeys=[  "DLDK3ipbf0Lo85OVjj5pchPyDfLk1HOS",
           "1zlJTNqgEBcVtQQsZfcFslbgln3CE0KzpAykQL94"
    ]
# headers= {
#   "apikey": "DLDK3ipbf0Lo85OVjj5pchPyDfLk1HOS",
#   "apikey": "1zlJTNqgEBcVtQQsZfcFslbgln3CE0KzpAykQL94"
# }
payload=[  {},
           {}
    ]
parameter=[  "rates",
             "data"
    ]

def get_headers(apikey):
    headers= {
    "apikey": apikey}
    return headers


USD=[]
TRY=[]
EUR=[]


def get_current_currency():
    for index, item in enumerate(Urls, start=0):
        response = requests.request("GET", Urls[index], headers=get_headers(ApiKeys[index]), data = payload[index])
        result = response.json()
        USD.append(result[parameter[index]]["USD"])       
        TRY.append(result[parameter[index]]["TRY"])
        EUR.append(result[parameter[index]]["EUR"])

        currency=get_cheaper_curency(USD,TRY,EUR)
    return currency


def get_cheaper_curency(USD,TRY,EUR):
    print(USD)
    print(TRY)
    print(EUR)
    usd=min(USD)
    tl=min(TRY)
    eur=min(EUR)
    return [usd,tl,eur]





# @app.route("/",methods = ["GET","POST"])
# def index():
#     name_curr=["usd","tl","eur"]
#     result=get_current_currency()
#     print(result)
#     if request.method == "POST":
#         return render_template("index.html")
#     zipList=zip(name_curr,result)
#     return render_template("index.html",zipList=zipList)


@app.route("/",methods = ["GET","POST"])
def index():
    name_curr=["usd","tl","eur"]

    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)
