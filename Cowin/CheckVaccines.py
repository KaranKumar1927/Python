from os import truncate
from MainMethod import *
import requests
import json
import datetime
#https://www.google.com/settings/security/lesssecureapps

dateToday = datetime.date.strftime(datetime.date.today(), "%d-%m-%Y")

def getVaccineAvailibility(pinCode,dateToday):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'referer': 'https://www.cowin.gov.in/'
    }

    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='+pinCode+'&date='+dateToday
    response = requests.get(url,headers=headers)

    return response.json()

yourPinCode = ["560063","560064","600118"]
availibilityCheck = getVaccineAvailibility(yourPinCode[2],dateToday)
f= open('C:\PythonPracs\Cowin\messageTemplate.txt',mode='at',encoding='utf-8')
f.truncate(0)
for x in availibilityCheck.get('centers'):
    result = x.get("sessions")[0].get("available_capacity")
    if(result>0):
       
        f.writelines("\nVaccine Available at\n")
        f.writelines("--------------------------------------------------\n")
        f.writelines(f"State Name : {x.get('state_name')}\n")
        f.writelines(f"District Name : {x.get('district_name')}\n")
        f.writelines(f"Center Name :{x.get('name')}\n")
        f.writelines(f"Vaccine : {x.get('sessions')[0].get('vaccine')}\n")
        f.writelines(f"Vaccine Available : {x.get('sessions')[0].get('available_capacity')}\n")
        f.writelines("---------------------------------------------------\n")
        sendMail()
f.close()           
             



