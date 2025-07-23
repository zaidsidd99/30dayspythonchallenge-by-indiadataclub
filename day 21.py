# from bs4 import BeautifulSoup
# import requests

# html_text= requests.get('https://www.naukri.com/psu-government-jobs').text
# print (html_text)




import requests
from bs4 import BeautifulSoup

url = 'https://indianexpress.com/section/cities/delhi/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

headlines = soup.find_all(['h1', 'h2', 'h3'])

for i, headline in enumerate (headlines, 1):
    text = headline.get_text(strip=True)
    if text:
     print(f"{i}. {text}")






























