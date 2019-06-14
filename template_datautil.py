import pandas as pd
import requests
from datetime import datetime
import time

'''

This is the template data utility module. It features the same code as the solar_datautil. You may change the commented 
sections as per your requirement to parse your required APIs. The code inside the comments is for your immediate reference to help
you understand the general behavior. 

Change any instance of 'template' in this module to your task. This applies to the module name too. For example, if your task
is related to solar then change name from 'template_datautil.py' to 'solar_datautil.py'. Change 'get_template_data(api_call)'
to 'get_solar_data(api_call)' and so on.

IMPORTANT!!!!
DO NOT CHANGE CODE WHICH IS NOT COMMENTED OUT. SUCH CODE USUALLY REPRESENTS THE RETURN FUNCTIONS AND THE DRIVING FUNCTION
CALLS.
It is also important that you format your data in the appropriate data-types that the function uses in returning or making
calls.

DO NOT CHANGE THE FUNCTION NAMES. YOU MAY ADD NEW UTILITY FUNCTIONS, BUT DO NOT CHANGE THE EXISTING FUNCTION NAMES. 
This is to avoid later confusion with respect to the init_util function. 

'''


def get_template_data(api_call):

    data = requests.post(api_call)

    '''    
    humidity = []
    date = []
    temp = []
    desc = []
    pressure = []
    sea_level = []
    ws = []
    wd = []
    data = data.json()

    df = pd.DataFrame()
    for lists in data['list']:
        date.append(lists['dt_txt'])
        humidity.append(lists['main']['humidity'])
        temp.append(lists['main']['temp'])
        pressure.append(lists['main']['pressure'])
        sea_level.append(lists['main']['sea_level'])
        ws.append(lists['wind']['speed'])
        wd.append(lists['wind']['deg'])
        desc.append(lists['weather'][0]['description'])

    df['Date'] = date
    df['Temperature'] = temp
    df['Humidity'] = humidity
    df['Windspeed'] = ws
    df['Wind Direction'] = wd
    df['Pressure'] = pressure
    '''

    return (df)

'''
def utc2local(utc):
    epoch = time.mktime(utc.timetuple())
    offset = datetime.fromtimestamp(epoch) - datetime.utcfromtimestamp(epoch)
    return utc + offset
'''

def process_template(df):
    '''
    temp = []
    for x in df['Pressure']:
        x = x * 100
        temp.append(x)

    df['Pressure'] = temp
    df['Date'] = pd.to_datetime(df['Date'])
    df['seconds'] = pd.to_timedelta(df['Date']).dt.total_seconds()
    temp = []
    temp2 = []
    temp3 = []

    for x in df['seconds']:
        z = x % (60 * 60 * 24)
        temp.append(z)

    for x in df['Date']:
        temp2.append(x.timetuple().tm_yday)
        temp3.append(x.timetuple().tm_year)

    df['seconds'] = temp
    df['doy'] = temp2
    df['year'] = temp3
    print(df.columns)
    dates = df['Date']
    temp = []

    for d in dates:
        temp.append(utc2local(d))

    dates = temp
    data = df.values
    X = data[:, 1:]
    '''
    return (X, dates)


def make_request_template():
    '''
    app_id = '4d52e2109f7da2b9fb9579064db1c0f1'
    city_name = 'Singapore'
    country_code = 'SG'
    api_call = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city_name + ',' + country_code + '&appid=' + app_id + '&mode=json&units=metric'
    return (api_call)
    '''

def init_util():
    api_call = make_request_template()
    df = get_template_data(api_call)
    X, dates = process_template(df)
    return (X, dates)
