from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.kununu.com/de/gothaer-versicherungsbank-vvag"
# driver = webdriver.Chrome('/Users/macintosh/Desktop/Master Thesis/01 Code/chromedriver')
driver = webdriver.Safari()
driver.get(url)
html = driver.page_source.encode('utf-8')
page_num = 0
button = driver.find_element_by_css_selector('.btn.btn-primary.btn-block.ng-isolate-scope').click()
current_url = driver.current_url

time.sleep(10)



try:
    while driver.find_elements_by_css_selector('.btn.btn-default.btn-block.ng-isolate-scope') or driver.find_elements_by_css_selector('.btn.btn-default.btn-block.ng-isolate-scope'):
        driver.find_element_by_css_selector('.btn.btn-default.btn-block.ng-isolate-scope').click()
        page_num += 1
        print("getting page number "+str(page_num))
        current_url = driver.current_url
        # print(current_url)
        time.sleep(4)
except:
    source = requests.get(current_url).text
    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('scrape.csv', 'w')
    csv_writer = csv.writer(csv_file, delimiter=';')
    csv_writer.writerow(['Header', 'Text', 'Rating'])


    # Delete all <br/> Tags
    for linebreak in soup.find_all('br'):
        linebreak.extract()


    for review_body in soup.find_all('div', class_='review-body'):

        # find every h2-Tag in review-body
        for header in review_body.find_all('h2'):

            # just extract the text and not the tags
            h2 = header.text
            p1 = header.next_sibling
            if header.next_sibling.text == '':
                p = header.next_sibling.next_sibling.text.replace('\n', ' ').strip()
            else:
                p = header.next_sibling.text.replace('\n', ' ').strip()

            # to iterate over the correct rating-group class, the .next_sibling is used, because otherwise it takes just the ratings of the first rating-group
            for rating_group in review_body.next_sibling.find_all('div', class_='rating-group'):
                rating_h2 = rating_group.span.text.replace('\n', ' ').strip()
                rating_star = rating_group.div.span.text.replace('\n', ' ').strip()
                h2
                p

                # check if the rating_h2 is the same as the h2 of the review-body
                if rating_h2 == h2:
                    csv_writer.writerow([h2, p, rating_star])
                    # print(h2)
                    # print(p)
                    # print(rating_star)

    csv_file.close()

    driver.quit()

