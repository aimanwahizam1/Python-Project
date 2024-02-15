# ---------------------------------------------------------------------------- #
#                                 Web Scraping                                 #
# ---------------------------------------------------------------------------- #

import requests
import bs4

# ---------------------------------- Format ---------------------------------- #

# 1. use requests.get
# 2. make bs4.beautifulsoup
# 3. work with soup to get what you want

# ----------------------------- Grabbing a title ----------------------------- #
# NOTE: this works on any website just an example
    # example.com

# Getting the website
result = requests.get('http://www.example.com')

# This will print out the html source code as a STRING
# print(result.text)

# But the string above is no use to us. So we use beautiful soup
soup = bs4.BeautifulSoup(result.text,"html.parser")
# print(soup)

# Getting title
    # Passed in one of the <title></title> tags to get info in between
    # NOTE: returns a list of all of those tags! e.g. h1 might have loads of tags
title = soup.select('title')[0].getText()
print(title)

# Getting paragraph 
site_paragraph = soup.select('p')[0].getText()
print(site_paragraph)