from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/mayashah/Downloads/chromedriver")
browser.get(START_URL)
time.sleep(9)

def scrape():
    headers = ["Proper mame", "Distance", "Mass", "Radius"]
    star_data = []
    for i in range(0, 201):
        time.sleep(2)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        star_table = soup.find('table')
        temp_list = []
        table_rows = star_table.find_all('tr')
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text.rstrip() for i in td]
            temp_list.append(row)
        star_data.append(temp_list)
    with open("webScraper.csv", 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)

scrape()