from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
import csv


url = "https://www.kununu.com/de/gothaer-versicherungsbank-vvag"
url = url+'/kommentare'
# driver = webdriver.Chrome('/Users/macintosh/Desktop/Master Thesis/01 Code/chromedriver')
driver = webdriver.Safari()
driver.get(url)
page_num = 0
sum_div = 0


# Das muss nach den Clicks kommen und dann jedes mal wenn der nächste Reiter durchgeklickt wird nochmal!
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

csv_file = open('scrape_new.csv', 'w')
csv_writer = csv.writer(csv_file, delimiter=';')
csv_writer.writerow(['Company', 'City', 'Jobstatus', 'Position', 'Business Unit', 'Header', 'Text', 'Rating'])


time.sleep(5)

# Click through the second navbar "Mitarbeiter", "Bewerber", "Azubis", etc.
for div in soup.find_all('nav', class_='navbar company-profile-subnav'):
    for li in div.find_all('li'):
        navbar_item = li.text
        print(li.text)
        driver.find_element_by_link_text(navbar_item).click()

        hasLoadMore = True
        while hasLoadMore:
            time.sleep(5)
            try:
                if driver.find_elements_by_css_selector('.btn.btn-default.btn-block.ng-isolate-scope'):
                    driver.find_element_by_css_selector('.btn.btn-default.btn-block.ng-isolate-scope').click()
                    page_num += 1
                    print("getting page number "+str(page_num))
                    time.sleep(5)
                else:
                    hasLoadMore = False
            except:
                hasLoadMore = False

        # for review_details in soup.find_all('div', class_='review-details user-content hidden-xs'):
        #     for details in review_details.find_all('div', class_='text-sm text-gray-base-70 text-light text-uppercase'):
        #
        #         # Correct formatting
        #         format_details = details.text.replace('\n', ' ').strip()
        #         correct_details = details.next_sibling.text.replace('\n', ' ').strip()
        #
        #         if format_details == 'Firma':
        #             company = correct_details
        #         elif format_details == 'Stadt':
        #             city = correct_details
        #         elif format_details == 'Jobstatus':
        #             jobstatus = correct_details
        #         elif format_details == 'Position/Hierarchie':
        #             position = correct_details
        #         elif format_details == 'Unternehmensbereich':
        #             business_unit = correct_details

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')

        # Find all Review-Bodies, which include the reviews
        for review_body in soup.find_all('div', class_='review-body'):

            #print(len(soup.find_all('div', class_='review-body')))
            #sum_div = len(soup.find_all('div', class_='review-content')) + sum_div

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
                        #csv_writer.writerow([company, city, jobstatus, position, business_unit, h2, p, rating_star])
                        csv_writer.writerow([h2, p, rating_star])

csv_file.close()
#print(sum_div)

#driver.quit()

