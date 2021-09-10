from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome('c:/bin/chromedriver')
browser.get(url)
time.sleep(10)
def scrap():
    headers=['name','light_Years_from_earth','planet_mass','stellar_magintude','disovery_date']
    planet_data = []
    for i in range(0,452):
        soup = BeautifulSoup(browser.page_source,'html.parser')
        for ultag in soup.find_all('ul',attrs={'class','exoplanet'}):
            li_tag = ultag.find_all('li')
            temp = []
            for index,li_tag in enumerate(li_tag):
                if index == 0:
                    temp.append(li_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp.append(li_tag.contents[0])
                    except:
                        temp.append('')
            planet_data.append(temp)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('data.csv','w')as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrap()