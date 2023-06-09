import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# 아래는 한글 문제 해결하는 코드
import matplotlib.font_manager as fm

font_name = fm.FontProperties(fname=r"C:\Windows\Fonts\malgun.ttf").get_name()
plt.rc("font", family=font_name)

import matplotlib as mlp
mlp.rcParams["axes.unicode_minus"] = False

from bs4 import BeautifulSoup
import requests
import time
import random
from tqdm import tqdm_notebook
from tqdm import tqdm
from fake_useragent import UserAgent

ua = UserAgent()

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import traceback


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    header_save = True
    while_tf = True
    total_start_time = datetime.now()
    while while_tf:
        try:
            menu_csv = pd.read_csv(r"test.csv", encoding="euc-kr")
            sch_list = menu_csv.sch_nm.unique()
        except:
            sch_list = np.array([])

        url = "https://www.foodsafetykorea.go.kr/portal/sensuousmenu/schoolMealsDetail.do?menu_grp=MENU_NEW03&menu_no=3017#"
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
        driver.get(url)

        DELAY_TIME = 0.5

        search_box = driver.find_element(By.CSS_SELECTOR, 'div.lcg div.right div.btn a')
        search_box.click()
        time.sleep(DELAY_TIME)

        input_box = driver.find_element(By.CSS_SELECTOR, 'input#search_keyword')

        input_box.send_keys("고등학교")
        input_box.send_keys(Keys.ENTER)
        time.sleep(3)

        year_box = driver.find_element(By.CSS_SELECTOR, 'select#select_year')

        tr_box = driver.find_elements(By.CSS_SELECTOR, 'tbody#listFrame tr')

        # for tr_idx, tr in enumerate(tr_box):
        #
        #     if tr_idx<5: continue

        tr_cnt = 0

        for tr in tqdm(tr_box):
            try:
                td_box = tr.find_elements(By.CSS_SELECTOR, 'td')
                a_box = tr.find_elements(By.CSS_SELECTOR, 'a')
                sch_nm = td_box[1].text

                if "미사용" in sch_nm: continue
                if sch_nm in sch_list: continue

                # 데이터가 하나도 없어서 매번 다시 체크하는 학교
                if "가은고등학교 (경상북도교육청)" == sch_nm: continue
                if "감포고등학교 (경상북도교육청)" == sch_nm: continue
                if "강구정보고등학교 (경상북도교육청)" == sch_nm: continue
                if "강릉제일고등학교부설방송통신고등학교 (강원도교육청)" == sch_nm: continue
                if "강원도농업계고등학교공동실습소 (강원도교육청)" == sch_nm: continue

                sch_nms = []
                menu_dates = []
                dts = []
                menus = []

                start_time = datetime.now()

                menu_url = a_box[1].click()

                time.sleep(1)

                y_cnt = 0
                for year_option in year_box.find_elements(By.CSS_SELECTOR, 'option'):

                    year_option.click()
                    time.sleep(DELAY_TIME)
                    year = year_option.text.replace(" ", "").replace("년", "")
                    m_cnt = 0
                    month_box = driver.find_element(By.CSS_SELECTOR, 'select#select_month')
                    for month_option in month_box.find_elements(By.CSS_SELECTOR, 'option'):
                        month_option.click()
                        time.sleep(DELAY_TIME)

                        month = month_option.text.replace(" ", "").replace("월", "")
                        month = "0" + month if len(month) == 1 else month

                        dl_box = driver.find_elements(By.CSS_SELECTOR, 'div#tab2 dl')
                        # print(sch_nm, year, month, len(dl_box))

                        if len(dl_box) < 2: continue
                        for dl_idx, dl in enumerate(dl_box):
                            try:
                                dt = dl.find_element(By.CSS_SELECTOR, 'dt').text
                                if dt == "석식":
                                    day = dl_box[dl_idx].find_element(By.XPATH, '../div[@class="top"]').text
                                    dt = dl_box[dl_idx].find_element(By.CSS_SELECTOR, 'dt').text
                                    menu = dl_box[dl_idx].find_element(By.CSS_SELECTOR, 'dd').text.replace(",","")
                                    menu_date = year+"."+month+"."+day
                                    # print(sch_nm, menu_date, dt, menu)
                                    sch_nms.append(sch_nm)
                                    menu_dates.append(menu_date)
                                    dts.append(dt)
                                    menus.append(menu)

                                    day = dl_box[dl_idx-1].find_element(By.XPATH, '../div[@class="top"]').text
                                    dt = dl_box[dl_idx-1].find_element(By.CSS_SELECTOR, 'dt').text
                                    menu = dl_box[dl_idx-1].find_element(By.CSS_SELECTOR, 'dd').text.replace(",","")
                                    menu_date = year+"."+month+"."+day
                                    # print(sch_nm, menu_date, dt, menu)
                                    sch_nms.append(sch_nm)
                                    menu_dates.append(menu_date)
                                    dts.append(dt)
                                    menus.append(menu)
                            except:
                                pass


                        # print("\n")


                data = {
                    'sch_nm': sch_nms,
                    'menu_date': menu_dates,
                    'dt': dts,
                    'menu': menus
                }
                df = pd.DataFrame(data)
                df.to_csv("test.csv", encoding="euc-kr", mode='a', index=False, header=header_save)
                if header_save: header_save = False

                search_box.click()
                time.sleep(DELAY_TIME)

                end_time = datetime.now()
                print(f"{sch_nm} => {end_time - start_time}")

                with open("log.txt", "a") as file:
                    file.write(f"{end_time} :: {sch_nm} => {end_time - start_time}\n")
                tr_cnt += 1
            except:
                print(f"{sch_nm} error")
                with open("error.txt", "a") as file:
                    file.write(sch_nm+"\n")
                break

        if tr_cnt == len(tr_box): while_tf = False
    total_end_time = datetime.now()

    print(f"total => {total_end_time - total_start_time}")
