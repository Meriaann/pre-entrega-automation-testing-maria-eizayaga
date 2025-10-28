from selenium import webdriver 
import time 
driver = webdriver.Chrome() # O Firefox(), Edge()
driver.get("https://www.google.com") 
print("Título:", driver.title)
time.sleep(5) 
driver.quit()