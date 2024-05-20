from selenium import webdriver
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

start = datetime.datetime.now()
print('Время старта: ' + str(start))
options = webdriver.FirefoxOptions()
options.page_load_strategy = 'eager'
options.add_argument('--headless')
options.add_argument('--disable-cache')
driver = webdriver.Firefox(options=options)
wait = WebDriverWait(driver, 5, 0.1)

o = open('output_bio.txt', 'a', encoding="utf-8")


def bio_candidate():
    left_bio = driver.find_elements('xpath', '//div[contains(@class, "bio-left")]')
    right_bio = driver.find_elements('xpath', '//div[contains(@class, "bio-right")]')
    fio_s = ('xpath', '//div[contains(@class, "name")]')
    wait.until(EC.visibility_of_element_located(fio_s))
    fio = driver.find_element('xpath', '//div[contains(@class, "bio-left")]')
    party_member_len = len(driver.find_elements('xpath', '//div[contains(@class, "party")]'))

    if party_member_len > 0:
        party_member = driver.find_element('xpath', '//div[contains(@class, "party")]')
        o.write(f'{party_member.text}$')
    else:
        o.write('Не указано')
    svo_len = len(driver.find_elements('xpath', '//div[contains(@class, "smo")]'))
    if svo_len > 0:
        svo = driver.find_element('xpath', '//div[contains(@class, "smo")]')
        o.write(f'{svo.text}$')
    else:
        o.write('Не указано')
    birth_info = 'Не указано'
    activity = 'Не указано'
    job_place = 'Не указано'
    job_post = 'Не указано'
    education = 'Не указано'
    alma_mater = 'Не указано'
    about = 'Не указано'
    contact = 'Не указано'
    deputat = 'Не указано'
    for j in range(len(left_bio)):  # начинаем шерстить таблицу
        if left_bio[j].text == 'Дата и место рождения:' or left_bio[j].text == 'Дата рождения:':
            birth_info = right_bio[j].text.replace('\n', ' ')
        if left_bio[j].text == 'Сфера деятельности:':
            activity = right_bio[j].text.replace('\n', ' ')
        if left_bio[j].text == 'Место работы:':
            job_place = right_bio[j].text.replace('\n', ' ')
        if left_bio[j].text == 'Должность:':
            job_post = right_bio[j].text.replace('\n', ' ')
        if left_bio[j].text == 'Образование:':
            education = right_bio[j].text.replace('\n', ' ')
        if left_bio[j].text == 'Учебные заведения:':
            alma_mater = right_bio[j].text.replace('\n', ' ')
        if left_bio[j].text == 'О себе:':
            about = right_bio[j].text.replace('\n', ' ')
        if left_bio[j].text == 'Страницы в соцсетях:':
            contact = right_bio[j].text.replace('\n', ' ')
        if left_bio[j].text == 'Депутатство:':
            deputat = right_bio[j].text.replace('\n', ' ')
    o.write(
        f'{fio.text}${birth_info}${activity}${job_place}${job_post}${education}${alma_mater}${about}${deputat}${contact}\n')


with open('candidates_links.txt', 'r+', encoding="utf-8") as f:
    full = f.readlines()
    for i in range(len(full)):
        link = full[i]
        driver.get(link)
        bio_candidate()
        print(f'{i + 1}/{len(full)} COMPLETE')  # Прогресс выполнения, можно переделать, чтобы нормально выглядело
o.close()
f.close()
driver.quit()
finish = datetime.datetime.now()
print('Время окончания: ' + str(finish))
print('Время работы: ' + str(finish - start))
