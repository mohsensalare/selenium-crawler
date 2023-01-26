from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://car.ir/prices")

model_name = None
while model_name != "":
    model_name = input("مدل خودرو را وارد کنید:")
    # find search box
    driver.find_element(By.XPATH, "/html/body/main/div/div/aside/div/div[2]/div[2]/div/div/input").send_keys(model_name)
    driver.find_element(By.XPATH, "/html/body/main/div/div/aside/div/div[2]/div[2]/div/div/input").send_keys(Keys.ENTER)
    sleep(3)
    try:
        table = driver.find_elements(By.CLASS_NAME, "price-table")
        if not table:
            print("خودرو یافت نشد")
            driver.find_element(By.CLASS_NAME, "action--remove-all-filters").click()
            continue
        for car in table:
            # find table rows
            rows = car.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                data = row.find_elements(By.TAG_NAME, "td")
                if data:
                    print("مدل", data[0].text)
                    print("قیمت کارخانه:", data[1].text)
                    print("قیمت در بازار آزاد:", data[2].text)
                    print("اخرین بروزرسانی قیمت:", data[3].text)

    except Exception as err:
        pass
    driver.find_element(By.CLASS_NAME, "action--remove-all-filters").click()
driver.quit()
