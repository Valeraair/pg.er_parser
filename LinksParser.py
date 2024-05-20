from selenium import webdriver
import time
import datetime

start = datetime.datetime.now()
print('Время старта: ' + str(start))
driver = webdriver.Firefox()
driver.get('https://pg.er.ru/candidates?region=78')  # Регион
time.sleep(10)


def contain_candidates():
    s = driver.find_elements('xpath', '//a[contains(@href, "candidate/")]')  # Ссылка на кандидата
    o = driver.find_element('xpath', '//*[@id="candidates"]/div[2]/div[1]/div/div[1]/div[2]/span')  # Округ
    for i in range(len(s)):
        f.write(f"{v.text};{s[i].get_attribute('href')};{o.text}\n")
        print(f"{v.text};{s[i].get_attribute('href')};{o.text}")


with open('output.txt', 'w', encoding="utf-8") as f:
    for j in range(1, 111):  # Доделать второе значение range, чтобы программа автоматически определяла количество
        # выборных кампаний
        v = driver.find_element('xpath', f'(//option[contains(text(), "Выборы д")])[{j}]')  # Выборная кампания
        time.sleep(1)
        v.click()
        time.sleep(1)
        contain_candidates()
        print(f"{j}/110 Complete")
finish = datetime.datetime.now()
print('Время окончания: ' + str(finish))
print('Время работы: ' + str(finish - start))
