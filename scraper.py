import json
from typing import re

import requests
from bs4 import BeautifulSoup





def scrapping():

    URL = "https://www.goodreads.com/book/popular_by_date"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,
                         'html5lib')

    books = []

    data = soup.find_all('article', "BookListItem")
    for d in data:
        quote = {}
        ratings = {}

        # Title
        title = d.find("h3", attrs={"class", 'Text Text__title3 Text__umber'})
        quote['title'] = title.text

        # url
        url = title.find("a")
        quote['url'] = url['href']

        # author
        author = d.find('a', attrs={"class", "ContributorLink"})
        quote['author'] = author.text

        # rating
        rating = d.find('span', attrs={"class", "Text Text__body3 Text__semibold Text__body-standard"})
        ratings["ratings_score"] = rating.text
        # 59511272
        # total rating value
        trating = d.find("div", attrs={"class", "AverageRating"})
        x = str(trating.text).split()
        ratings["total_rating"] = x[0]

        # total shelvings value
        tshelvings = trating.find_next_sibling("div", text=True)
        x = str(tshelvings.text).split()
        ratings["total shelvings"] = x[0]

        # adding rating list
        quote["ratings"] = ratings

        description = d.find('span', attrs={"class", "Formatted"})
        t= str(description.text).splitlines()
        x=str(t).replace("'", "")
        x=str(x).replace("[", "")
        x = str(x).replace(",", "")
        x = str(x).replace("  ", "")
        quote["description"]=x

        books.append(quote)



    # f = open("Books.json", "a")
    # f.write(json.dumps(books))
    # f.close()
    print(books)
