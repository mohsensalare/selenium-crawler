from selenium import webdriver
from selenium.webdriver.common.by import By

league = {
    "1": "بوندسلیگا-آلمان",
    "2": "لالیگا-اسپانیا",
    "3": "لیگ-برتر-انگلیس",
    "4": "سری-آ-ایتالیا",
    "5": "لیگ-یک-فرانسه",
    "6": "لیگ-برتر-ایران",
}
for key, value in league.items():
    print(key + "-" + value)

id = input("لطفا عدد لیگ انتخابی را وارد کنید")

driver = webdriver.Chrome()
# دریافت صفحه لیگ بر اساس ایدی لیگ
driver.get(f"https://www.varzesh3.com/football/league/{id}/")
# دریافت جدول تیم ها
teams = driver.find_element(By.XPATH,
                            "/html/body/section/main/div[2]/div/div/section/div[2]/div/div[1]/div/table/tbody")
# دریافت هدر جدول
thead = driver.find_element(By.XPATH,
                            "/html/body/section/main/div[2]/div/div/section/div[2]/div/div[1]/div/table/thead/tr")
# تفکیک تیم ها
teams = teams.find_elements(By.TAG_NAME, "tr")
# تفکیک ستون ها
thead = thead.find_elements(By.TAG_NAME, "th")

for team in teams:
    # تقکیک ستون های مربوط به تیم
    team = team.find_elements(By.TAG_NAME, "td")
    print("رتبه" + " : " + team[0].text)
    print(thead[1].text + " : " + team[1].text)
    print(thead[2].text + " : " + team[2].text)
    print(thead[3].text + " : " + team[3].text)
    print(thead[4].text + " : " + team[4].text)
    print(thead[5].text + " : " + team[5].text)
    print(thead[6].text + " : " + team[6].text)
    print(thead[8].text + " : " + team[8].text)
    print(thead[9].text + " : " + team[9].text)
input()
