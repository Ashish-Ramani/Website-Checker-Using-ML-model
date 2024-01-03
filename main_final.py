import requests
import json
import time
import datetime

text = "test.txt"

with open(text, 'r') as file:
    html_data = file.read()
    abc = html_data.split()
    ret = []
    for i in abc:
        if i.find('https:') == 0 or i.find('http:') == 0:
            ret.append(i)
    for url_https in ret:
        url = "https://www.virustotal.com/api/v3/urls"
        
        payload = { "url": f"{url_https}" }
        headers = {
            "accept": "application/json",
            "x-apikey": "virustotal API",#API
            "content-type": "application/x-www-form-urlencoded"
        }

        response1 = requests.post(url, data=payload, headers=headers)
        data = response1.json()
        analysis_id = data["data"]["id"]
        id_parts = analysis_id.split("-")
        id = id_parts[1]
        url_id=(url+"/"+id)
        headers1 = {
            "accept": "application/json",
            "x-apikey": "virustotal API",#API
        }
        response = requests.get(url_id, headers=headers1)
        url_vote=(url+"/"+id+"/votes?limit=10")
        headers = {
            "accept": "application/json",
            "x-apikey": "virustotal API",#API
        }

        response_vote = requests.get(url_vote, headers=headers)
        data1=response.json()
        last_analysis_stats = data1["data"]["attributes"]["last_analysis_stats"]
        print(last_analysis_stats)
        value = f"['{url_https}':{last_analysis_stats}], \n"
        print(datetime.datetime.now())
        time.sleep(15)
        with open('data.txt','a') as file:
            file.write(str(value))
