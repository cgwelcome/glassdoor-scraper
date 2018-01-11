import requests
from bs4 import 
from http.cookiejar import CookieJar

r = requests.Session()
headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36' }
response = r.get('https://www.glassdoor.ca/Overview/Working-at-Media-10-EI_IE1079906.11,19.htm', headers=headers)
