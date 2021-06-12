import requests
import json


def getVaccineAvailibility(pinCode,date):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'referer': 'https://www.cowin.gov.in/'
    }

    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='+pinCode+'&date='+date
    response = requests.get(url,headers=headers)

    return response.json()

yourPinCode = str(input("Enter the pin code "))
#dateToCheck = str(input("Enter the Date to check "))
availibilityCheck = getVaccineAvailibility(yourPinCode,"18-05-2021")
for x in availibilityCheck.get('centers'):
    result = x.get("sessions")[0].get("available_capacity")
    if(result>0):
        print("Vaccine Available at")
        print("State Name : " ,x.get("state_name"))
        print("District Name : " ,x.get("district_name"))
        print("Center Name :",x.get("name"))
        print("Vaccine : ",x.get("sessions")[0].get("vaccine"))
        print("Vaccine Available : ",x.get("sessions")[0].get("available_capacity"))
 
        
        

