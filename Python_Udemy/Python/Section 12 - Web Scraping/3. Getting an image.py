# ---------------------------------------------------------------------------- #
#                        Getting an Image from a Website                       #
# ---------------------------------------------------------------------------- #

import requests
import bs4

result = requests.get('https://en.wikipedia.org/wiki/Malaysia')

soup = bs4.BeautifulSoup(result.text, 'html.parser')

# NOTE: unsure how to find flag using class '.mw-file-element' since will return most images (not like video)
flag = soup.find('img', attrs={'class': 'mw-file-element', 'alt': 'A blue rectangle with a gold star and crescent in the canton, with 14 horizontal red and white stripes on the rest of the flag'})
# print(flag)

# We can call the info in the html element like a dictionary
flag_source = flag['src']
print(flag_source)

# Now we got image source can make request on that url
image_link = requests.get('https:' + flag_source)

# Now we can save the image locally
    # Mode is wb - write binary
with open ('C://Users//aiman//OneDrive//Desktop//Malaysia_Flag.jpg', mode='wb') as image:
    image.write(image_link.content)



