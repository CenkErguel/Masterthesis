from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.kununu.com/de/gothaer-versicherungsbank-vvag'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()

# closing the connection
uClient.close()

# html parsing
page_soup = soup(page_html, 'html.parser')

# grabs each review title

reviews = page_soup.findAll("div", {"class": "review-body"})
review1 = reviews[0]


print(reviews)
