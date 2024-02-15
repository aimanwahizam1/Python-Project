# ---------------------------------------------------------------------------- #
#                        Getting a Class from a Website                        #
# ---------------------------------------------------------------------------- #

import requests
import bs4

# --------------------- Get context table from Wiki Page --------------------- #

result = requests.get('https://en.wikipedia.org/wiki/Malaysia')

soup = bs4.BeautifulSoup(result.text, "html.parser")

# NOTE: the below is slightly different since the html element encountered is like:
# <div class="vector-toc-text">
# 			<span class="vector-toc-numb">
#                 2
#           </span>
#     History
# </div>
# So need to go into span and find next element/sibling which is the text we want to get (i.e. "History")

contents_title = soup.find_all('span', attrs={'class': 'vector-toc-numb'})

for i in contents_title:
    print(i.find_next_sibling(text=True))
