from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import csv

url = 'https://eurovisionworld.com/odds/eurovision'

driver = webdriver.Chrome()
driver.get(url)

data = []

today = datetime.today().strftime('%Y-%m-%d')

## Headers
head = ['date', 'position', 'country', 'song', 'winning chance']

thead = driver.find_element(By.XPATH, '//*[@id="page"]/div[2]/main/div[1]/div[2]/div[3]/div[1]/table/thead')

for r in thead.find_elements(By.XPATH, './tr'):
    row = []
    for c in r.find_elements(By.XPATH, './th'):
        casa = c.text + ' '
        print(casa)