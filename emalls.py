from selenium import webdriver
from selenium.webdriver.common.by import By
import time

product_name = input("product name:")

driver = webdriver.Chrome()

driver.get("https://emalls.ir")
#  =یافتن کادر جست و جو و وارد کردن نام محصول
driver.find_element(By.XPATH, "/html/body/form/header/div/div/div/div/div[2]/div[1]/input").send_keys(product_name)
time.sleep(1)
#  کلیک روی دکمه جست و جو
driver.find_element(By.XPATH, "/html/body/form/header/div/div/div/div/div[2]/div[1]/a").click()
time.sleep(1)
# کلیک روی اولین نتیجه یافت شده
driver.find_element(By.XPATH, "/html/body/form/div[10]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div").click()
time.sleep(1)
# تفکیک فروشگاه ها
rows = driver.find_elements(By.CLASS_NAME, "shop-row")
for row in rows:
    shop_name = row.find_element(By.CLASS_NAME, "shoplogotitle").text
    price = row.find_element(By.CLASS_NAME, "shop-price").text
    if shop_name and price:
        print(f"{shop_name}:{price}")
