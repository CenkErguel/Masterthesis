from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('https://www.kununu.com/de/gothaer-versicherungsbank-vvag').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('scrape.csv', 'w')
csv_writer = csv.writer(csv_file, delimiter=';')
csv_writer.writerow(['Header', 'Text', 'Rating'])


# Delete all <br/> Tags
for linebreak in soup.find_all('br'):
    linebreak.extract()


# Iterate over all 'review-body' classes
# for review_body in soup.find_all('div', class_='review-body'):
#     # Iterate over all 'h2' Tags inside of each 'review-body' class
#     for review_body_header2 in review_body.find_all('h2'):
#
#         # Check if there is an empty string, if yes fill in 'None'
#         if review_body_header2.text == '':
#             print()
#
#             review_h2 = 'None'
#             print(review_h2)
#
#             review_p = review_body_header2.next_sibling.text
#             print(review_p)
#
#             print()
#             csv_writer.writerow([review_h2, review_p])
#         elif review_body_header2.next_sibling.text == '':
#             print()
#
#             review_h2 = review_body_header2.text
#             print(review_h2)
#
#             review_p = 'None'
#             print(review_p)
#
#             print()
#             csv_writer.writerow([review_h2, review_p])
#         else:
#             print()
#
#             review_h2 = review_body_header2.text
#             print(review_h2)
#
#             review_p = review_body_header2.next_sibling.text
#             print(review_p)
#
#         print()
#         csv_writer.writerow([review_h2, review_p])
#
# csv_file.close()


# for ratings in soup.find_all('div', class_='rating-group'):
#     print(ratings)

# for content in soup.find_all('div', class_='review-content'):
#     content2 = content.h2
#     print(content2.text)

# find every review-body class
for review_body in soup.find_all('div', class_='review-body'):
    # find every h2-Tag in review-body
    for header in review_body.find_all('h2'):
        # just extract the text and not the tags
        h2 = header.text
        p = header.next_sibling.text

        # to iterate over the correct rating-group class, the .next_sibling is used, because otherwise it takes just the ratings of the first rating-group
        for rating_group in review_body.next_sibling.find_all('div', class_='rating-group'):
            rating_h2 = rating_group.span.text.replace('\n', '').strip()
            rating_star = rating_group.div.span.text.replace('\n', '').strip()
            h2
            p

            # check if the rating_h2 is the same as the h2 of the review-body
            if rating_h2 == h2:
                csv_writer.writerow([h2, p, rating_star])
                # print(h2)
                # print(p)
                # print(rating_star)

csv_file.close()


