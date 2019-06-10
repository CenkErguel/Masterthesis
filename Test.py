from selenium import webdriver
import time

from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.kununu.com/de/gothaer-versicherungsbank-vvag').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('scrape_new.csv', 'w')
csv_writer = csv.writer(csv_file, delimiter=';')
csv_writer.writerow(['Header', 'Text', 'Rating'])
csv_file.close()
#print(soup)
# Delete all <br/> Tags
for linebreak in soup.find_all('br'):
    linebreak.extract()

url = "https://www.kununu.com/de/gothaer-versicherungsbank-vvag"
# driver = webdriver.Chrome('/Users/macintosh/Desktop/Master Thesis/01 Code/chromedriver')
driver = webdriver.Safari()
driver.get(url)
#html = driver.page_source.encode('utf-8')
page_num = 0
more_buttons = driver.find_element_by_css_selector('.btn.btn-primary.btn-block.ng-isolate-scope').click()
time.sleep(10)
page_source = driver.page_source
#print(page_source)

hasLoadMore = True
while hasLoadMore:
    time.sleep(5)
    try:
        if driver.find_elements_by_css_selector('.btn.btn-default.btn-block.ng-isolate-scope') or driver.find_elements_by_css_selector('.btn.btn-default.btn-block.ng-isolate-scope'):
            driver.find_element_by_css_selector('.btn.btn-default.btn-block.ng-isolate-scope').click()
            page_num += 1
            print("getting page number "+str(page_num))
            # print(current_url)
            time.sleep(1)
    except:
        hasLoadMore = False

page_source2 = requests.get('https://www.kununu.com/de/gothaer-versicherungsbank-vvag/kommentare').text
soup = BeautifulSoup(page_source2, 'lxml')
print("STEP1")



for review_body in soup.find_all('div', class_='review-body'):

    # find every h2-Tag in review-body
    for header in review_body.find_all('h2'):

        # just extract the text and not the tags
        h2 = header.text
        p1 = header.next_sibling
        if header.next_sibling.text == '':
            p = header.next_sibling.next_sibling.text.replace('\n', ' ').strip()
            print("ICERDE 1")
        else:
            p = header.next_sibling.text.replace('\n', ' ').strip()
            print("ICERDE 2")

        # to iterate over the correct rating-group class, the .next_sibling is used, because otherwise it takes just the ratings of the first rating-group
        for rating_group in review_body.next_sibling.find_all('div', class_='rating-group'):
            rating_h2 = rating_group.span.text.replace('\n', ' ').strip()
            rating_star = rating_group.div.span.text.replace('\n', ' ').strip()
            h2
            p
            print("ICERDE 3")
            # check if the rating_h2 is the same as the h2 of the review-body
            if rating_h2 == h2:
                csv_writer.writerow([h2, p, rating_star])
                print("ICERDE 4")
                # print(h2)
                # print(p)
                # print(rating_star)
print("STEP2")
csv_file.close()

driver.quit()

