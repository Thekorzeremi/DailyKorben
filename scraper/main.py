import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless=new')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)

url = "https://korben.info/"
driver.get(url)

print("Scrapping started !")

cards = driver.find_elements(By.CLASS_NAME, 'article-card')

scrapped_data = {"data": []}
count = 1

for card in cards:
    if count > 3:
        break

    try:
        img_meta = card.find_element(By.CSS_SELECTOR, 'meta[itemprop="image"]')
        image_url = img_meta.get_attribute("content")
    except:
        image_url = None

    content_block = card.find_element(By.CLASS_NAME, 'article-card-content')
    raw = content_block.text.strip()
    lines = raw.split("\n")

    title = lines[0] if len(lines) > 0 else ""
    content = "\n".join(lines[4:]) if len(lines) >= 5 else ""

    print(f"Scrapping article {count}")
    print(f"Title : {title}")
    print(f"Image : {image_url}")

    scrapped_data["data"].append({
        "title": title,
        "content": content,
        "image": image_url
    })

    count += 1

with open("../daily-korben-front/public/data/data.json", "w", encoding="utf-8") as f:
    json.dump({"Extracted datas": scrapped_data}, f, ensure_ascii=False, indent=4)

print("Scrapping ended !")
driver.quit()