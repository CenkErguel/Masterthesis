from selenium import webdriver
from bs4 import BeautifulSoup
import time


url = "https://www.kununu.com/de/sitemap"
driver = webdriver.Safari()
driver.get(url)

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

links = []
hrefs = []
#list_links = len(driver.find_elements_by_css_selector('.links-fine'))

# Take all links from the column 'Firmen als Arbeitgeber'
list_links = 30

# DONE
for link in range(29,30):
    # Ä, Ö and Ü has not enough values, so they need to be catched
    if link == 2:
        driver.find_elements_by_css_selector('.links-fine')[link].click()
        time.sleep(5)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        list_links_inner = len(driver.find_elements_by_css_selector('.links-fine'))
        print(list_links_inner)
        for div in soup.find_all('div', class_='sitemap-content'):
            list_links_inner = len(driver.find_elements_by_css_selector('.links-fine'))
            print(list_links_inner)
            for href in div.find_all('div', class_='col-xs-12'):
                number_links = len(div.find_all('div', class_='col-xs-12'))
                if 'https://' in href.a['href']:
                    hrefs.append(href.a['href'])
            print(hrefs)
            print(len(hrefs))
            driver.execute_script("window.history.go(-1)")
            time.sleep(5)
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'lxml')
    elif link == 17:
        driver.find_elements_by_css_selector('.links-fine')[link].click()
        time.sleep(5)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        list_links_inner = len(driver.find_elements_by_css_selector('.links-fine'))
        print(list_links_inner)
        for div in soup.find_all('div', class_='sitemap-content'):
            list_links_inner = len(driver.find_elements_by_css_selector('.links-fine'))
            print(list_links_inner)
            for href in div.find_all('div', class_='col-xs-12'):
                number_links = len(div.find_all('div', class_='col-xs-12'))
                if 'https://' in href.a['href']:
                    hrefs.append(href.a['href'])
            print(hrefs)
            print(len(hrefs))
            driver.execute_script("window.history.go(-1)")
            time.sleep(5)
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'lxml')
    elif link == 24:
        driver.find_elements_by_css_selector('.links-fine')[link].click()
        time.sleep(5)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        list_links_inner = len(driver.find_elements_by_css_selector('.links-fine'))
        print(list_links_inner)
        for div in soup.find_all('div', class_='sitemap-content'):
            list_links_inner = len(driver.find_elements_by_css_selector('.links-fine'))
            print(list_links_inner)
            for href in div.find_all('div', class_='col-xs-12'):
                number_links = len(div.find_all('div', class_='col-xs-12'))
                if 'https://' in href.a['href']:
                    hrefs.append(href.a['href'])
            print(hrefs)
            print(len(hrefs))
            driver.execute_script("window.history.go(-1)")
            time.sleep(5)
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'lxml')
    else:
        driver.find_elements_by_css_selector('.links-fine')[link].click()
        time.sleep(5)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        list_links_inner = len(driver.find_elements_by_css_selector('.links-fine'))
        print(list_links_inner)
        for link_inner in range(list_links_inner):
            time.sleep(10)
            driver.find_elements_by_css_selector('.links-fine')[link_inner].click()
            time.sleep(10)
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'lxml')
            list_links_inner_inner = len(driver.find_elements_by_css_selector('.col-xs-12'))

            # Gets all links
            for div in soup.find_all('div', class_='sitemap-content'):
                for href in div.find_all('div', class_='col-xs-12'):
                    number_links = len(div.find_all('div', class_='col-xs-12'))
                    if 'https://' in href.a['href']:
                        hrefs.append(href.a['href'])
                print(hrefs)
                print(len(hrefs))
            driver.execute_script("window.history.go(-1)")
            time.sleep(10)
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'lxml')
            if link_inner + 1 == list_links_inner:
                #driver.execute_script("window.history.go(-1)")
                time.sleep(5)
                driver.execute_script("window.history.go(-1)")
                time.sleep(5)
                page_source = driver.page_source
                soup = BeautifulSoup(page_source, 'lxml')
