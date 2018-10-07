from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import time
import sys, csv, re
import random
no = []
title = []


def main():
    go()

# 2. 메인 로직. 한 페이지에서 글 읽어오고 다음페이지로 넘어가서 또 읽어오고.. 반복
def go():
    driver = webdriver.Chrome("C:\python\driver/chromedriver.exe")
    #wait = WebDriverWait(driver, 2)
    link = []
    title, date_list, content = [],[],[]
    for i in range(1,31):
        for j in range(1,50):
            if i < 10 : date = "0"+str(i)
            else : date = str(i)
            url = 'https://entertain.naver.com'

            try:
                driver.get(url+ '/now #sid=106&date=2018-09-'+date+'&page='+str(j))
                time_ = random.sample(range(1, 3), 1)
                time.sleep(int(time_[0]))
                a = driver.page_source
                soup = BeautifulSoup(a, 'lxml')


                #ul이 2개로 나뉘어져서. 다 가지고 와서 ul 각각 for문돌면서 다시 그 안에서 li 별 for문돌면서 a 태그 찾아야할듯.
                ul_list = soup.find('div', {'class': 'left_cont'}).find('ul', {'class' : 'news_lst news_lst2'})#findAll('li')#findAll('ul')
                #ul_list = soup.find('ul', {'class' : 'news_lst news_lst2'}).findAll('li')

                #sys.exit()
                #for ul in ul_list:
                for li in ul_list.findAll('li'):
                    #link.append(li.find('li').find('a').attrs['href'])
                    link.append(li.find('a').attrs['href'])
            except:
                continue
            #이렇게 하면 링크 다 가지고와진다. 이제 이 for문 끝날 때까지 이걸 반복한다. -> 30개 * 200개 * 20개 => 12만개.
            #나중에 break 없애고 sleep 주석 제거.
            time_ = random.sample(range(1, 3), 1)
            time.sleep(int(time_[0]))
        time_2 = random.sample(range(1, 3), 1)
        time.sleep(int(time_2[0]))

    for news in link:
        try:
            driver.get(url+news)
            soup = BeautifulSoup(driver.page_source, "lxml")
            title_ = soup.find('h2', {'class': 'end_tit'}).text.strip()
            content_ = soup.find('div', {'id': 'articeBody'}).text.strip()
            content_ = content_.replace(",", "")
            date_ = soup.find('span', {'class': 'author'}).find('em').text.split(" ")[0].strip()
            title.append(title_)
            content.append(content_)
            date_list.append(date_)
            time_ = random.sample(range(1, 3), 1)
            time.sleep(int(time_[0]))

        except:
            continue

    with open('./entertain_news_9m.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for cnt, i in enumerate(title):
            #title_ = re.sub('[^a-zA-Z0-9 ㄱ-ㅣ가-힣]', ' ', title[cnt])
            #date_ = re.sub('[^a-zA-Z0-9 ㄱ-ㅣ가-힣]', ' ', date_list[cnt])
            #content_ = re.sub('[^a-zA-Z0-9 ㄱ-ㅣ가-힣]', ' ', content[cnt])
            title_ = title[cnt]
            date_ = date_list[cnt]
            content_ = content[cnt]

            writer.writerow((title_, date_, content_))

    sys.exit()
if __name__ == "__main__":
    main()


