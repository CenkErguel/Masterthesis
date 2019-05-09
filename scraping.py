from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('https://www.kununu.com/de/gothaer-versicherungsbank-vvag').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Header', 'Rating'])


# Aktuell werden die </br> Tags nicht richtig in die CSV eingetragen. Muss noch behoben werden

# Iterate over all 'review-body' classes
for review_body in soup.find_all('div', class_='review-body'):

    # Iterate over all 'h2' Tags inside of each 'review-body' class
    for review_body_header2 in review_body.find_all('h2'):

        # Check if there is an empty string, if yes fill in 'None'
        if review_body_header2.text == '':
            print()

            review_h2 = 'None'
            print(review_h2)

            review_p = review_body_header2.next_sibling.text
            print(review_p)

            print()
            csv_writer.writerow([review_h2,review_p])
        elif review_body_header2.next_sibling.text == '':
            print()

            review_h2 = review_body_header2.text
            print(review_h2)

            review_p = 'None'
            print(review_p)

            print()
            csv_writer.writerow([review_h2, review_p])
        else:
            print()

            review_h2 = review_body_header2.text
            print(review_h2)

            review_p = review_body_header2.next_sibling.text
            print(review_p)

        print()
        csv_writer.writerow([review_h2, review_p])

csv_file.close()
