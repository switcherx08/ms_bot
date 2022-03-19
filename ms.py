import requests
import pybase64
#from jinja2 import Template
''''

toheaders1 = "Basic YWRtaW5AcGhvdG9jaHVkbzoxMDAxOTdHQQ=="
print(toheaders1)
headers = {"Authorization": (toheaders1)}
path = "entity/purchaseorder"
response = requests.get("https://online.moysklad.ru/api/remap/1.1/" + (path), headers=headers)
print(headers)
'''''
URL_API = "https://online.moysklad.ru/api/remap/1.2/"
res = None
value = None
orderznum = None
items = []
toheaders1 = "Basic YWRtaW5AcGhvdG9jaHVkbzoxMDAxOTdHQQ=="
headers = {"Authorization": (toheaders1)}
def statusresponse():
    if response.status_code == 401:
        print("Авторизация не прошла")
    if response.ok:
        print(response)
        print(response.text)

org = "7ecce034-fd8b-11ea-0a80-02e70008ddc4"
def getmainbalance():
    path = "report/money/byaccount"
    response1 = requests.get(f"https://online.moysklad.ru/api/remap/1.1/{path}?organization={org}", headers=headers).json()
    value = response1
    return value
MAINBALANCE = getmainbalance()
def getordersz():
    path = "entity/purchaseorder"
    limit = 8
    result = []
    resp = requests.get(f"{URL_API}{path}?limit={limit}", headers=headers).json()
    for orderznum in resp['rows']:
         result.append([orderznum['name'], orderznum['moment']])
    return (result)
GETORDERSZ = getordersz()

def gettoday():
    import datetime as dt
    path = "report/sales/plotseries"
    moment_now = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    moment_from = dt.datetime(2022, 3, 13)
    r = requests.get(f"{URL_API}{path}?momentFrom={moment_from}&momentTo={moment_now}&interval=hour", headers=headers).json()
    return r
def gettodayorders():
    import datetime as dt
    path = "report/orders/plotseries?"
    moment_now = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    moment_from = dt.datetime(2022, 3, 13)
def     

print (gettoday())

#print (getordersz())

resptest = requests.get(f"https://online.moysklad.ru/api/remap/1.1/entity/purchaseorder", headers=headers).json()
#for test in resptest['rows']:
#   print(test['name'])




