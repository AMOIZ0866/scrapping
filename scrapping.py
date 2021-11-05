import json
import os
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
import datefinder

"""
In the function were using Selenium to get the book urls link list
"""


def fetching_links_scrap():
    url = "https://www.goodreads.com/book/popular_by_date"
    # config the options
    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1200")

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
    driver = webdriver.Chrome(executable_path=DRIVER_BIN, chrome_options=options)
    driver.get(url)

    # Loop to get the books url list
    for x in range(15):
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Show more books')]"))).click()
        except:
            print("Reached bottom of page")
            break

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    links = []
    for item in soup.find_all('h3', class_="Text Text__title3 Text__umber"):
        links.append(item.find('a')['href'])
    getting_details(links)


"""
This function is used to get the details of each book by using beautiful Soup and Selenium
"""


def getting_details(links):
    # config the options
    bookdetails = []

    for d in links:
        options = Options()
        options.headless = False
        options.add_argument('disable-notifications')

        options.add_argument("--window-size=1920,1200")
        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

        driver = webdriver.Chrome(executable_path=DRIVER_BIN, chrome_options=options)
        t = time.time()
        driver.set_page_load_timeout(10)

        try:
            driver.get(d)
        except TimeoutException:
            driver.execute_script("window.stop();")
        print('Time consuming:', time.time() - t)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        books = {}

        try:
            pagesrow = soup.find("div", class_='row')
            pub_date = pagesrow.find_next_sibling("div", text=True).text
            matches = datefinder.find_dates(pub_date)
            for match in matches:
                books['publish_date'] = match.strftime("%Y %b %d")

        except:
            books['publish_date'] = "NONE"

        try:
            iSBN = soup.find("meta", property="books:isbn")
            books['ISBN'] = iSBN['content']
        except:
            books['ISBN'] = "NO ISBN"

        try:
            books['title'] = soup.find("h1", itemprop='name').text.strip()
        except:
            books['title'] = "NO TITLE"
        try:
            books['author'] = soup.find("span", itemprop='name').text.strip()
        except:
            books['author'] = "NO AUTHOR"

        try:
            books['rating_score'] = soup.find("span", itemprop='ratingValue').text.strip()
        except:
            books['rating_score'] = 0
        try:
            books['rating_count'] = soup.find("meta", itemprop='ratingCount').get('content')
        except:
            books['rating'] = 0

        data = soup.findAll('div', "elementList")
        gens = []
        for d in data:
            gen = d.find('div', class_="left")
            try:
                t = (str(gen.text).replace('\n', ''))
                t = t.replace(' ', "")
                gens.append(t)
            except:
                gens.append('No Genre')

        books['genre'] = gens
        try:
            desc = soup.find('div', id="description")
            books['Description'] = desc.text.strip()
        except:
            books['Description'] = "NONE"

        bookdetails.append(books)
        soup.clear()

    output_file = open('Data.json', 'w', encoding='utf-8', )
    json_object = json.dumps(bookdetails, indent=4)
    output_file.write(json_object)
