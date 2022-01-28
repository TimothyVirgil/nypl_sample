from django.http import HttpRequest
from django.shortcuts import render
from bs4 import BeautifulSoup
import lxml
import requests
import json
import random
from decouple import config
import re

#TODO: run more tests for dates/months
#TODO: get better matching for dates or refactor to make more consistent
#TODO: set better exception handling for broken or non-existent image links

def img_capture(request,date):
    '''Pass a date into NYPL's digital collection API, 
    capture a random image with it's name and date created.'''   

    if not re.match('\d\d\d\d-\d\d-\d\d', date):
        return render(request, 'error.html')

    url = f'http://api.repo.nypl.org/api/v1/items/search?q={date}&field=dateCreated&publicDomain=true&per_page=100'
    auth = config('TOKEN')
    headers = {'Authorization': auth}

    call = requests.get(url, headers=headers).json()[
        'nyplAPI']['response']

    num_results = call['numResults']
    if int(num_results) > 100:
        choices = 100
    
    else:
        choices = num_results
    
    while True:
        curr_choice = random.randint(0,choices-1)
        curr_item = call['result'][curr_choice]
        if curr_item['typeOfResource'] == 'still image':
            img_url = curr_item['itemLink']
            obj_name = curr_item['title']
            obj_url = curr_item['apiUri']
            break

    try:
        obj_date = requests.get(obj_url,headers=headers).json()['nyplAPI']['response']['mods']['originInfo']['dateCreated']['$']
    
    except:
        #sometimes there is a list of origininfo
        obj_list = requests.get(obj_url,headers=headers).json()['nyplAPI']['response']['mods']['originInfo']
        for item in obj_list:
            if 'dateCreated' in item:
                obj_date = item['dateCreated']['$']
                break
            else:
                continue

    res = requests.get(img_url)
    soup = BeautifulSoup(res.text, 'lxml')

    img_link = soup.select('.deriv-link')[1].attrs['href']

    context = {'img_link': img_link,
               'obj_name': obj_name,
               'obj_date': obj_date
               }

    return render(request, 'base.html', context)