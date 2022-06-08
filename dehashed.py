import json
import requests 
import time
import sys
import pandas
from requests.auth import HTTPBasicAuth

delay_counter = 1/5 # delay for the requests to the api call in seconds 

def config_loader():
    #write a function that loads a json file named config.json 
    #and returns the data as a dictionary
    with open('config.json', 'r') as f:
        data = json.load(f)
    return data

def dehashed_api_call_delay(url):
    #write a function that makes an api call to the dehashed api 
    #and returns the data as a dictionary
    time.sleep(delay_counter)
    header={"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Accept":"application/json"}
    response = requests.get(url, auth=HTTPBasicAuth(config_loader()['username'], config_loader()['password']),headers=header)
    data = response.json()
    return data

def dehashed_api_url_generator(search_term,size=1000):
    #write a function that takes a search term and returns 
    #the url for the api call
    url = 'https://api.dehashed.com/search?query={0}&size={1}'.format(search_term,size)
    return url

def json_to_excel(data):
    #write a function to convert the json data to an excel file
    #and save it as dehashed.xlsx
    df = pandas.DataFrame(data)
    df.to_excel('dehashed.xlsx')

def main():
    try:
        search = sys.argv[1]
        data = dehashed_api_call_delay(dehashed_api_url_generator(search))
        json_to_excel(data['entries'])
    except IndexError:
        print("Usage: dehashed.py <search_term>")
    except Exception as e:
        print(e)

main()
