from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

verb = input("لطفا کلمه فارسی خود را وارد کنید:\n")

driver = webdriver.Chrome()
# حلقه تکرار برای دریافت چندین اسم
while verb != '':
    driver.get("https://nameniko.com/")
    # یافتن کادر سرچ و تایپ نام دریافتی
    driver.find_element(By.XPATH, "/html/body/header/div/div/div/div/div[1]/div/div/input").send_keys(verb)
    # انتظار برای دریافت اطلاعات در کادر سرچ
    sleep(10)
    # تایپ دکمه اینتر برای رفتن به صفحه مربوط به نام
    driver.find_element(By.XPATH, "/html/body/header/div/div/div/div/div[1]/div/div/input").send_keys(Keys.ENTER)
    print("معنی: ", driver.find_element(By.XPATH, "/html/body/section[4]/div/div/div/section[1]/div/div").text)
    print("جنسیت: ",
          driver.find_element(By.XPATH,
                              "/html/body/section[4]/div/div/div/section[2]/div/div/table/tbody/tr[1]/td[2]").text)
    print("افراد دارای این نام: ",
          driver.find_element(By.XPATH,
                              "/html/body/section[4]/div/div/div/section[2]/div/div/table/tbody/tr[3]/td[2]/span").text)
    print("ریشه: ", driver.find_element(By.XPATH,
                                        "/html/body/section[4]/div/div/div/section[2]/div/div/table/tbody/tr[1]/td[2]").text)
    # یافتن بخش تگ ها و جدا کردن تگ ها با یافتن تک a در html
    tags = driver.find_element(By.XPATH,
                               '/html/body/section[4]/div/div/div/section[2]/div/div/div/div[1]').find_elements(
        By.TAG_NAME, 'a')
    print("تگ ها")
    for tag in tags:
        print(tag.text)
    verb = input("لطفا کلمه فارسی خود را وارد کنید:\n")
