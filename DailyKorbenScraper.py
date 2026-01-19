# utiliser korben pour faire des postes automatiques sur linkedin ou m'envoyer les datas sur un canal telegram ou whatsapp

import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)

url = "https://korben.info/"

driver.get(url)

elements = driver.find_elements(By.CLASS_NAME, 'article-card-content')

scrapped_data = {"data": []}

article_limiter = 5
count = 1

for e in elements:
    if count < article_limiter:
        cur = str(e.text)
        scrapped_data["data"].append({
            "data": cur
        })
        count += 1

with open("./daily-korben-front/app/Dailyscrap_selenium.json", "w", encoding="utf-8") as f:
    json.dump({"Extracted datas": scrapped_data}, f, ensure_ascii=False, indent=4)

driver.quit()