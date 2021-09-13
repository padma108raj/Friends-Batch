"""
import os
cmd = "curl -vvv http://www.google.co.in"
os.system(cmd)
"""
import json
import requests


url = "http://www.google.co.in"
headers = {"content-type": "application/json", "Accept-Charset": "UTF-8"}
r = requests.post(url, data={"sample":"data"}, headers=headers) 
data = r.json() 
print(data)
