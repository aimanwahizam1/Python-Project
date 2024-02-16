# https://books.toscrape.com/

# GOAL: get the title of every book with 2 star rating

import requests
import bs4

# NOTE:
# there are multiple pages
# Home page: https://books.toscrape.com/catalogue/page-1.html
# Page 2: https://books.toscrape.com/catalogue/page-2.html ...

# Make base url with curly brackets for varying page numbers
    # Then use base_url.format(number) to get different pages


# PLAN (from looking at source code):
    # Get .product_pod classes
    # Filter by p class = 'star-rating Two'
    # Get title

""" res = requests.get(base_url.format(1))

soup = bs4.BeautifulSoup(res.text, 'html.parser')

books = soup.select('.product_pod') """

# So we can check each book to see if we can .select '.star-rating.Two'
    # If nothing comes up then its not two star rated!
""" example = books[0]
print(example.select('.star-rating.Three')) """


# Final code:

two_star_titles = []

# ----------------------------------- Way 1 ---------------------------------- #

""" base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
# Loop for every page
for n in range(1, 51):
    # Make varying url
    scrape_url = base_url.format(n)
    # Request url
    res = requests.get(scrape_url)

    # Soup it
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Logic for each page
    books = soup.select('.product_pod')

    for book in books:
        if book.select('.star-rating.Two'):
            two_star_titles.append((book.select('a')[1]['title']))

print(two_star_titles) """

# ----------------------------------- Way 2 ---------------------------------- #

# Using a while loop (case where we didn't know there were 50 pages)
# Here try to use the next page button href

url = 'https://books.toscrape.com/catalogue/page-1.html'


while True:
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    books = soup.select('.product_pod')

    for book in books:
        if book.select('.star-rating.Two'):
            two_star_titles.append((book.select('a')[1]['title']))

    next_page = soup.select_one('a:-soup-contains("next")')

    if next_page:
        url = 'https://books.toscrape.com/catalogue/' + next_page['href']
    else:
        break

print(two_star_titles)
print(len(two_star_titles))