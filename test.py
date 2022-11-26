
import os
import threading
from threading import Thread
import requests
# class ClassName():

#     def func1(self,date):
#         if date == "":
#             response = requests.request("GET", "{}/latest?symbols=&base={}".format(os.getenv("BASE_URL_API_1"),os.getenv("BASE_CURRENCY")), headers={"apikey":os.getenv("API_KEY_1")}, data = {})
#         else:
#             response = requests.request("GET", "{}/{}?symbols=EUR%2CUSD%2CTRY&base={}".format(os.getenv("BASE_URL_API_1"),date,os.getenv("BASE_CURRENCY")), headers={"apikey":os.getenv("API_KEY_1")}, data = {})
#         result = response.json()
#         currency_list=[result["rates"]["TRY"],result["rates"]["EUR"],result["rates"]["USD"]]
#         return currency_list
#     def func2(self,date):
#         if date == "":   
#             response = requests.request("GET","{}latest?apikey={}&base_currency={}".format(os.getenv("BASE_URL_API_2"),os.getenv("API_KEY_2"),os.getenv("BASE_CURRENCY")), headers={"apikey":os.getenv("API_KEY_2")}, data = {})
#             result = response.json()
#             currency_list=[result["data"]["TRY"],result["data"]["EUR"],result["data"]["USD"]]
#         else:
#             response = requests.request("GET", "{}historical?apikey={}&date_from={}&date_to={}&base_currency={}".format(os.getenv("BASE_URL_API_2"),os.getenv("API_KEY_2"),date,date,os.getenv("BASE_CURRENCY")), headers={"apikey":os.getenv("API_KEY_2")}, data = {})
#             result = response.json()
#             currency_list=[result["data"][date]["TRY"],result["data"][date]["EUR"],result["data"][date]["USD"]]
#         return currency_list

#     def runall(self,date):
#         if __name__ == '__main__':
#             Thread(target = self.func1(date)).start()
#             Thread(target = self.func2(date)).start()
# run = ClassName()
# run.runall(date="2020-10-10") # will run all the def's in the same time




class ClassName():
    def __init__(self,TRY,USD,EUR) -> None:
        self.TRY=TRY
        self.USD=USD
        self.EUR=EUR
    def func1(self,date):
        if date == "":
            response = requests.request("GET", "{}/latest?symbols=&base={}".format(os.getenv("BASE_URL_API_1"),os.getenv("BASE_CURRENCY")), headers={"apikey":os.getenv("API_KEY_1")}, data = {})
        else:
            response = requests.request("GET", "{}/{}?symbols=EUR%2CUSD%2CTRY&base={}".format(os.getenv("BASE_URL_API_1"),date,os.getenv("BASE_CURRENCY")), headers={"apikey":os.getenv("API_KEY_1")}, data = {})
        result = response.json()
        currency_list=[result["rates"]["TRY"],result["rates"]["EUR"],result["rates"]["USD"]]
        self.make_list(currency_list)
        return currency_list
    def func2(self,date):
        if date == "":   
            response = requests.request("GET","{}latest?apikey={}&base_currency={}".format(os.getenv("BASE_URL_API_2"),os.getenv("API_KEY_2"),os.getenv("BASE_CURRENCY")), headers={"apikey":os.getenv("API_KEY_2")}, data = {})
            result = response.json()
            currency_list=[result["data"]["TRY"],result["data"]["EUR"],result["data"]["USD"]]
        else:
            response = requests.request("GET", "{}historical?apikey={}&date_from={}&date_to={}&base_currency={}".format(os.getenv("BASE_URL_API_2"),os.getenv("API_KEY_2"),date,date,os.getenv("BASE_CURRENCY")), headers={"apikey":os.getenv("API_KEY_2")}, data = {})
            result = response.json()
            currency_list=[result["data"][date]["TRY"],result["data"][date]["EUR"],result["data"][date]["USD"]]
        self.make_list(currency_list)
    
    def make_list(self,list_curr):
        self.TRY.append(list_curr[0])
        self.USD.append(list_curr[1])
        self.EUR.append(list_curr[2])       
    
    def runall(self,date):
        if __name__ == '__main__':
            self.func1(date)
            self.func2(date)
        return [(1/min(self.TRY)),(1/min(self.USD)),(1/min(self.EUR))] 
run = ClassName(TRY=[],USD=[],EUR=[])
result=run.runall(date="") # will run all the def's in the same time
print(result)
# class ClassName2():
#     def __init__(self,TRY,USD,EUR) -> None:
#         self.TRY=TRY
#         self.USD=USD
#         self.EUR=EUR
#     def func1(self):
#         currency_list=["1","2"]
#         self.TRY=currency_list
#         print(currency_list)
#         return currency_list
#     def func2(self):
#         currency_list=["3","4"]
#         self.TRY.append(currency_list)
#         return currency_list

#     def runall(self):
#         method_list = [func for func in dir(ClassName2) if callable(getattr(ClassName2, func)) and not func.startswith("__")]
#         for i in method_list:
#             print(exec("self."+i)) 
#             print(self.TRY)       

# run=ClassName2(TRY="",USD="",EUR="")
# run.runall()