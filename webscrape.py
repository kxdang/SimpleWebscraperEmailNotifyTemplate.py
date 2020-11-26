import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'YOUR WEBSITE URL'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup)

OOS = soup.select("div.promo-bug.out")
# this checks for the class names in a div element e.g div class="promo-bug out"

print(len(OOS))

if len(OOS) == 1:
    print('OUT OF STOCK ITEM')

else:
    print('IN STOCK')
    msg = 'Subject: Hello, there is stock!'
    fromaddr = 'YOURBOT@gmail.com'
    toaddrs = 'TOADDRESS@gmail.com'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("YOURBOT@gmail.com", "GMAIL PASSWORD")
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

    print('From: ' + fromaddr)
    print('To: ' + str(toaddrs))
    print('Message: ' + msg)
