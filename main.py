import os, datetime, time, csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path=os.path.join("/Users/lorenz/PycharmProjects/roberta4NF/", "chromedriver_99_0_4844_51"))

linkliste = []
with open('asin_liste.csv', newline='') as csvfile:
    liste = csv.reader(csvfile, delimiter=' ')
    for e in liste:
        linkliste.append("https://amazon.it/dp/"+str(e[0]))

def print_start():
    print("***********************************")
    print("***********************************")
    print("ROBERTA FOR NEWFLAG BOT is started")
    print("***********************************")
    print("***********************************")

print_start()
#driver.get('https://10fastfingers.com/typing-test/german')
images_counter = 0
bullets_counter = 0

for link in linkliste[3:9]:
    with open("asin_results.csv", "a", newline="") as csvfile:
        result_writer = csv.writer(csvfile, delimiter=" ")
        print("GETTING LINK", link)
        result_writer.writerow(("GETTING LINK", link))
        driver.get(link)
        try:
            driver.find_element(By.CSS_SELECTOR, value="#a-autoid-0").click()
        except:
            pass
        try:
            driver.find_element(By.CSS_SELECTOR, value="#feature-bullets > div > a").click()
        except:
            pass
        try:
            title = driver.find_element(By.ID, value="productTitle").text
            print("PRODUCT TITLE: ", title)
            result_writer.writerow(("PRODUCT TITLE: ", title))
        except Exception as e:
            print("PRODUCT NOT ACCESSIBLE")
            result_writer.writerow("PRODUCT NOT ACCESSIBLE")
            print("Error in Product Access", e)
            continue
        try:
            images_counter = len(driver.find_elements(By.CSS_SELECTOR, value=".a-spacing-small.item.imageThumbnail.a-declarative"))
            print("Images found: ", images_counter)
            result_writer.writerow(("Images found: ", images_counter))
        except Exception as e:
            print("IMAGES COULD NOT BE CRAWLED")
            result_writer.writerow("IMAGES COULD NOT BE CRAWLED")
            print("Error in Images", e)
            images_counter = 0
        try:
            bulletpoints_container = driver.find_element(By.CSS_SELECTOR, value=".a-unordered-list.a-vertical.a-spacing-mini")
            bulletpoints = bulletpoints_container.find_elements(By.CSS_SELECTOR, value=".a-list-item")
            bullets_counter = len(bulletpoints)
            print("Bulletpoints found: ", bullets_counter)
            result_writer.writerow(("Bulletpoints found: ", bullets_counter))
            for i,j in enumerate(bulletpoints):
                print("Bulletpoint", i, ":", "Wordcount :", len(str.split(j.text)), "Value :", j.text)
                result_writer.writerow(("Bulletpoint", i, ":", "Wordcount :", len(str.split(j.text)), "Value :", j.text))
        except Exception as e:
            print("BULLETS COULD NOT BE CRAWLED!")
            result_writer.writerow("BULLETS COULD NOT BE CRAWLED!")
            print("Error in Bullets", e)
        result_writer.writerow("*********")

driver.close()