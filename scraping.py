from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
import csv

# Insert the website that should be scraped
#source = requests.get('https://www.kununu.com/de/gothaer-versicherungsbank-vvag').text

# Create BeautifulSoup Object
#soup = BeautifulSoup(source, 'lxml')

# Delete all <br/> Tags
# for linebreak in soup.find_all('br'):
#     linebreak.extract()


url = "https://www.kununu.com/de/gothaer-versicherungsbank-vvag"
# driver = webdriver.Chrome('/Users/macintosh/Desktop/Master Thesis/01 Code/chromedriver')
driver = webdriver.Safari()
driver.get(url)
page_num = 0

# First click on the "Mehr Bewertungen lesen" Button
more_buttons = driver.find_element_by_css_selector('.btn.btn-primary.btn-block.ng-isolate-scope').click()

# Wait 10 sec to load the page
time.sleep(10)

# Complete page source
#page_source = driver.page_source


hasLoadMore = True
while hasLoadMore:
    time.sleep(5)
    try:
        if driver.find_elements_by_css_selector('.btn.btn-default.btn-block.ng-isolate-scope') or driver.find_elements_by_css_selector('.btn.btn-default.btn-block.ng-isolate-scope'):
            driver.find_element_by_css_selector('.btn.btn-default.btn-block.ng-isolate-scope').click()
            page_num += 1
            print("getting page number "+str(page_num))
            # print(current_url)
            time.sleep(5)
    except:
        hasLoadMore = False

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'lxml')
csv_file = open('scrape_new.csv', 'w')
csv_writer = csv.writer(csv_file, delimiter=';')
csv_writer.writerow(['Header', 'Text', 'Rating'])


# Find all Review-Bodies, which include the reviews
for review_body in soup.find_all('div', class_='review-body'):

    # find every h2-Tag in review-body, e.g. "Arbeitsatmosphäre"
    for header in review_body.find_all('h2'):

        # just extract the text, not the tags
        h2 = header.text
        p1 = header.next_sibling
        p2 = p1.next_sibling
        if p1.text == '' and p2 is not None:
            p = p2.text.replace('\n', ' ').strip()

        else:
            p = p1.text.replace('\n', ' ').strip()


        # to iterate over the correct rating-group class, the .next_sibling is used, because otherwise it takes just the ratings of the first rating-group
        for rating_group in review_body.next_sibling.find_all('div', class_='rating-group'):
            rating_h2 = rating_group.span.text.replace('\n', ' ').strip()
            rating_star = rating_group.div.span.text.replace('\n', ' ').strip()
            h2
            p

            # check if the rating_h2 is the same as the h2 of the review-body
            if rating_h2 == h2:
                csv_writer.writerow([h2, p, rating_star])

csv_file.close()

#driver.quit()

