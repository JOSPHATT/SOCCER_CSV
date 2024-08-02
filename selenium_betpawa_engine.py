
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
options = webdriver.ChromeOptions()

options.add_argument('--headless')

options.add_argument('--no-sandbox')

options.add_argument('--disable-dev-shm-usage')

options.add_argument('--disable-gpu')

options.add_argument('--disable-features=NetworkService,NetworkServiceInProcess')

options.add_argument('--enable-javascript')



dr = webdriver.Chrome(options=options)
#https://www.betpawa.co.ke/upcoming?marketId=OU&categoryId=2

dr.get("https://www.ke.sportpesa.com/en/sports-betting/football-1/")
#https://www.betpawa.co.ke/upcoming?marketId=OU&categoryId=2")
# Website used for scraping
dr.implicitly_wait(20)
elements = dr.find_elements(By.XPATH, "//*")
print(len(elements))

Upcoming_Games={}
C=0
for element in elements:
    try:
        extracted_text = element.get_attribute('innerText')
        c=str(C)
        Upcoming_Games[c]=extracted_text
        C=C+1
    except:
        continue
#quitting the browser
dr.quit()

def upcoming_games():
    return Upcoming_Games

if __name__ == '__upcoming_games__':
    upcoming_games()

