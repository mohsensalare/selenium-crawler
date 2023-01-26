from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
# باز کردن سایت
driver.get("https://isignal.ir/%D8%A7%D8%B1%D8%B2-%D8%AF%DB%8C%D8%AC%DB%8C%D8%AA%D8%A7%D9%84/")
# یافتن جدول ارز ها
coins = driver.find_elements(By.CLASS_NAME, "table-row")
for coin in coins:
    # تفکیک و نمایش داده ها
    index = coin.find_element(By.CLASS_NAME, "index-column").text
    name = coin.find_element(By.TAG_NAME, "a").text
    price = coin.find_element(By.CLASS_NAME, "market-close").text
    rial_price = coin.find_element(By.XPATH, '//*[@id="_signalCryptoList"]/div[3]/div[1]/div/div/div/div[1]/div[1]/div[3]/div/div[1]/div[4]').text
    print(f"{index}-{name}:${price}-{rial_price} ریال ")