
#!/usr/bin/env python3

import json
import requests
import random 
def agents():
    with open('core/agents.json') as f:
        data = json.load(f)
        js_data = data['agents']
        agents = js_data[random.randint(0, 140)]
        return agents




def active():
    try:
        headers={
				'Host': 'www.googletagmanager.com',
				'User-Agent': agents(),
				'Accept': '*/*',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate, br',
				'Referer': 'https://honeypots.tech/p/HBomb/user/',
				'Connection': 'keep-alive',
				'If-Modified-Since': 'Mon, 27 Jul 2020 06:00:00 GMT',
				'Cache-Control': 'max-age=0',
				'TE': 'Trailers'
        }
        
        url = "https://www.googletagmanager.com/gtag/js?id=UA-166299719-1"
        r = requests.get(url, headers=headers)
        print(r.status_code  )     
    except Exception :
        print(r.status_code)
        print("\tPlease Restart HBomb Tool")
