import requests
import bs4

# -------------------------------- Question 1 -------------------------------- #

# Get the HTML text from the homepage

""" res = requests.get("https://quotes.toscrape.com/page/1/")

soup = bs4.BeautifulSoup(res.text, 'html.parser')

print(soup) """

# -------------------------------- Question 2 -------------------------------- #

# Get the names of all authors on the first page

""" res = requests.get("https://quotes.toscrape.com/page/1/")

soup = bs4.BeautifulSoup(res.text, 'html.parser')

quotes = soup.select('.quote')

authors = []

for quote in quotes:
    authors.append(quote.select_one(".author").text)

print(sorted(set(authors))) """

# -------------------------------- Question 3 -------------------------------- #

# Get a list of all quotes on the first page

""" res = requests.get("https://quotes.toscrape.com/page/1/")

soup = bs4.BeautifulSoup(res.text, 'html.parser')

quotes = soup.select('.quote')

quote_list = []

for quote in quotes:
    quote_list.append(quote.select_one(".text").text)

print(quote_list) """

# -------------------------------- Question 4 -------------------------------- #

# Get the top 10 tags

""" res = requests.get("https://quotes.toscrape.com/page/1/")

soup = bs4.BeautifulSoup(res.text, 'html.parser')

top_ten = soup.select(".tag-item")

for tag in top_ten:
    print(tag.select_one(".tag").text) """

# -------------------------------- Question 5 -------------------------------- #

# Get all unique authors in all pages

url = 'https://quotes.toscrape.com/page/1/'

authors = []

while True:
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    quotes = soup.select(".quote")

    for quote in quotes:
        author_name = quote.select_one(".author").text

        if author_name not in authors:
            authors.append(author_name)

    next_page = soup.select_one('a:-soup-contains("Next ")')

    if next_page:
        url = 'https://quotes.toscrape.com' + next_page['href']
    else:
        break

print(authors)
