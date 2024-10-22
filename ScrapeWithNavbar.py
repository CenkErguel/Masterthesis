from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
import csv


def scrape_data(urls):
    page_num = 0
    sum_articles = 0
    user_ID = 3860
    url_counter = 44543

    csv_file = open('Dataset.csv', 'w')
    csv_writer = csv.writer(csv_file, delimiter=';')
    csv_writer.writerow(
        ['ID',
         'Company',
         'Rating Date',
         'City',
         'Jobstatus',
         'Position',
         'Business Unit',
         'Header',
         'Text',
         'Rating'])
    driver = webdriver.Safari()

    for url in urls:
        one_url = url
        one_url = url+'/kommentare'
        driver.get(one_url)

        # Das muss nach den Clicks kommen und dann jedes mal wenn der nächste Reiter durchgeklickt wird nochmal!
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')

        time.sleep(3)

        # Click through the second navbar "Mitarbeiter", "Bewerber", "Azubis", etc.
        for div in soup.find_all('nav', class_='navbar company-profile-subnav'):
            for li in div.find_all('li', {'class':['active', '']}):
                #print(len(div.find_all('li')))
                print(li)

                # If "Mitarbeiter" is not available go to next > "Bewerber"
                if not li.text:
                    li = li.next_sibling
                    # If "Bewerber" is not available go to next > "Azubi"
                    if not li.text:
                        li = li.next_sibling

                navbar_item = li.text
                #print(navbar_item)
                driver.find_element_by_link_text(navbar_item).send_keys("\n")
                navbar_item_number = int(li.a.span.text.replace(".", ""))

                #print(navbar_item_number, type(navbar_item_number))

                control_value = 0
                #print(control_value, type(control_value))

                time.sleep(2)

                if driver.find_elements_by_css_selector('.btn.btn-default.btn-block.ng-isolate-scope'):
                    driver.find_element_by_css_selector('.btn.btn-default.btn-block.ng-isolate-scope').send_keys("\n")

                while control_value != navbar_item_number and control_value < navbar_item_number:

                    page_source = driver.page_source
                    soup = BeautifulSoup(page_source, 'lxml')

                    try:
                        if driver.find_elements_by_css_selector('.btn.btn-default.btn-block.ng-isolate-scope'):
                            driver.find_element_by_css_selector('.btn.btn-default.btn-block.ng-isolate-scope').send_keys("\n")

                        control_value = len(soup.find_all('article', class_='company-profile-review'))
                        #print(control_value)

                    except:

                        #page_source = driver.page_source
                        #soup = BeautifulSoup(page_source, 'lxml')

                        control_value = len(soup.find_all('article', class_='company-profile-review'))
                        #print('EXCEPT', control_value)

                page_source = driver.page_source
                soup = BeautifulSoup(page_source, 'lxml')

                sum_articles = len(soup.find_all('article', class_='company-profile-review'))
                #print(sum_articles)

                for art in soup.find_all('article', class_='company-profile-review'):
                    user_ID = user_ID + 1

                    rating_date = art.ul.li.span.next_sibling.text

                    # Find all Review-Bodies, which include the reviews
                    for review_body in art.find_all('div', class_='review-body'):

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

                                    # Include the sidebar information as well
                                    for review_details in art.find_all('div', class_='review-details user-content hidden-xs'):

                                        # Set standard value to 'n/a'
                                        company = 'n/a'
                                        city = 'n/a'
                                        jobstatus = 'n/a'
                                        position = 'n/a'
                                        business_unit = 'n/a'

                                        for details in review_details.find_all('div', class_='text-sm text-gray-base-70 text-light text-uppercase'):

                                            # Correct formatting
                                            format_details = details.text.replace('\n', ' ').strip()
                                            correct_details = details.next_sibling.text.replace('\n', ' ').strip()

                                            if format_details == 'Firma':
                                                company = correct_details
                                            elif format_details == 'Stadt':
                                                city = correct_details
                                            elif format_details == 'Jobstatus':
                                                jobstatus = correct_details
                                            elif format_details == 'Position/Hierarchie':
                                                position = correct_details
                                            elif format_details == 'Unternehmensbereich':
                                                business_unit = correct_details

                                    csv_writer.writerow(
                                                        [user_ID,
                                                         company,
                                                         rating_date,
                                                         city,
                                                         jobstatus,
                                                         position,
                                                         business_unit,
                                                         h2,
                                                         p,
                                                         rating_star])
        url_counter = url_counter + 1
        print(url_counter)

    csv_file.close()
    #print(sum_articles)

    #driver.quit()

