import requests
import time
import os
from twilio.rest import Client

# api keys from twilio dashboard, needed for text message setup.
TWILIO_ACCOUNT = os.environ['TWILIO_ACCOUNT']
TWILIO_TOKEN = os.environ['TWILIO_TOKEN']
TO_PHONE = '+1xxxYYYzzzz' # some phone number here
FROM_PHONE = '+1xxxYYYzzzz' # your twilio phon number here.

# get the list of cities you would be willing to drive to.
CITY_CHECK_LIST = ['BERKELEY', 'WALNUT CREEK', 'CONCORD','OAKLAND']


def get_cvs_availability():
    headers = {
    'authority':'www.cvs.com',
    'sec-fetch-site': 'same-origin',
    'referer': 'https://www.cvs.com/immunizations/covid-19-vaccine'}

    # you need to change this url if you want to check in a state outside of California.
    r = requests.get(
        'https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.CA.json?vaccineinfo', 
        headers=headers)

    res = r.json()
    locations = r.json()['responsePayloadData']['data']['CA']

    availability_list = []
    for c in locations:
        city = c['city']
        status = c['status']

        # get the list of cities you care about 
        if city in CITY_CHECK_LIST:
            print(city, ' ', status)
            
            if status != 'Fully Booked':
                availability_list.append(city)
    
    return availability_list
        
availability_list = get_cvs_availability()

# if there are any availabilities in your check list, send a text message.
if len(availability_list) > 0:
    client = Client(TWILIO_ACCOUNT, TOKEN)
    locations_str = ', '.join(availability_list)
    
    message = client.messages.create(
        to=TO_PHONE, 
        from_=FROM_PHONE,
        body="Vaccine Available at {}. https://www.cvs.com/vaccine/intake/store/covid-screener/covid-qns".format(
            locations_str))