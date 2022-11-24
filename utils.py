import requests

Urls=[  "https://api.apilayer.com/exchangerates_data/latest?symbols=&base=TRY",
        "https://v6.exchangerate-api.com/v6/ae224d4a7302a1a8e8efa3d8/latest/TRY"
    ]


ApiKeys=[  "DLDK3ipbf0Lo85OVjj5pchPyDfLk1HOS",
           "ae224d4a7302a1a8e8efa3d8"
    ]
headers= {
  "apikey": "DLDK3ipbf0Lo85OVjj5pchPyDfLk1HOS",
  "apikey": "ae224d4a7302a1a8e8efa3d8"
}
payload=[  {},
           {}
    ]
parameter=[  "rates",
             "conversion_rates"
    ]

def get_headers(apikey):
    headers= {
    "apikey": apikey}
    return headers


USD=[]
TRY=[]
EUR=[]



def get_current_currency():
    for index, val in enumerate(Urls):
        response = requests.request("GET", Urls[index], headers=get_headers(ApiKeys[index]), data = payload[index])

        status_code = response.status_code
        result = response.json()
        USD.append(result[parameter[index]]["USD"])
        print(result[parameter[index]]["USD"])
        TRY.append(result[parameter[index]]["TRY"])
        print(result[parameter[index]]["TRY"])
        EUR.append(result[parameter[index]]["EUR"])
        print(result[parameter[index]]["EUR"])
        currency=get_cheaper_curency(USD,TRY,EUR)
        return currency

get_current_currency()



def get_cheaper_curency(USD,TRY,EUR):
    usd=min(USD)
    tl=min(TRY)
    eur=min(EUR)
    return [usd,tl,eur]

