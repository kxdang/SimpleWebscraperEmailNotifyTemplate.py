import requests
from bs4 import BeautifulSoup
import smtplib

PRODUCT_URL = 'https://www.lenovo.com/ca/en/perkopolisgold/accessories-and-monitors/monitors/home/C32q-20A19315FD031-5inch-Monitor-HDMI/p/65F8GCC1US?clickid=2Ql3Su2FsxyLWyRwUx0Mo38cUkEwi-yuNVhpyA0&irgwc=1&PID=341376&acid=ww%3Aaffiliate%3Abv0as6&clickid=WkJ2rVXMUxyOTt8wUx0Mo3bwUkEwvcX5UUZRSE0&irgwc=1&PID=341376&acid=ww%3Aaffiliate%3Abv0as6'
URL = 'https://www.lenovo.com/ca/en/perkopolisgold/gatekeeper/showpage?toggle=PasscodeGatekeeper'
POST_URL = 'https://www.lenovo.com/ca/en/perkopolisgold/gatekeeper/authGatekeeper'

headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}
session = requests.Session()

response = session.get(URL, headers=headers)

soup = BeautifulSoup(session.get(URL, headers=headers).text, 'html.parser')

# CSRFToken
CSRFT_token = soup.findAll("input")[2].get('value')
# returns the csrf-token on initial request

print(CSRFT_token)

payload = {
  'gatekeeperType': 'PasscodeGatekeeper',
  'passcode': 'GoldPerk2020',
  'CSRFToken': CSRFT_token
}
temp = session.post(POST_URL, headers=headers, data=payload)

getRequest = session.get(PRODUCT_URL, headers=headers)

soupRequest = BeautifulSoup(getRequest.text, 'html.parser') # still points back to the login even with cookies/payload in post
print('Unavailable' if soupRequest.find('strong').text == 'Temporarily Unavailable' else 'Available')