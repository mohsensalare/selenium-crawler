from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# open page
driver.get("https://gisheh7.ir/boxoffice")

# find table
table = driver.find_element(By.TAG_NAME, "tbody")

# get list movies
rows = table.find_elements(By.TAG_NAME, "tr")

# Print the information for each movie
for row in rows:
    data = row.find_elements(By.TAG_NAME, "td")
    print("*******************")
    print("رتبه:", data[0].text)
    print("فیلم:", data[1].text)
    print("پخش:", data[2].text)
    print("شروع اکران:", data[3].text)
    print("هفته:", data[4].text)
    print("روز:", data[5].text)
    print("تعداد بلیت:", data[6].text)
    print("فروش هفتگی (ریال):", data[7].text)
    print("*******************")

# Close the browser
driver.quit()
