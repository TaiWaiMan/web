from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from urllib import parse
import pymysql

# db_config = {
#     'host': 'localhost',     # 127.0.0.1
#     'port': 3306,
#     'user': 'root',
#     'password': '',
#     'db': 'db_chickpt',
#     'chatset': 'utf8'
# }

conn = pymysql.connect(host= 'localhost', user= 'root' ,password= '', port= 3306,   db= 'db_chickpt',)
# conn = pymysql.connect(**db_config)
# try:
#     with conn.cursor() as cursor:
#         command = "SELECT * FROM mission_list"
#         cursor.execute(command)
#         data = cursor.fetchall()
#         # conn.commit()
            
# except Exception as ex:
#     print(ex)


# web_address_keywoud = input('請輸入關鍵字搜尋任務 ')


chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

for pages in range(1, 25):
    web_address = f'https://www.chickpt.com.tw/cases?page={pages}'
    # #web_address = 'https://www.chickpt.com.tw/cases?keyword=Python'
    # web_address = f'https://www.chickpt.com.tw/cases?keyword={web_address_keywoud}'

    driver.get(web_address)

    ul = driver.find_element(By.XPATH, "//ul[@id='job-list']")
    texts = ul.find_elements(By.XPATH, "li")

    #information = [text, people, money, place]
    #words = ['', '', '', '']
    print()
    count = 0
    for text in texts:
        name = text.find_element(By.XPATH, "a/div[@class='is-blk']/h2").text
        person = text.find_element(By.XPATH, "a/div[@class='job-info-company is-blk display-control show-pc show-tablet']/p").text 
        money = text.find_element(By.XPATH, "a/div[@class='is-blk']/p[@class='job_detail']/span[@class='salary']").text
        place = text.find_element(By.XPATH, "a/div[@class='is-blk']/p[@class='job_detail']/span[@class='place']").text
        url = text.find_element(By.XPATH, "a").get_attribute("href")
        cannot = "已徵到"

        # if web_address_keywoud in name:
    #         print(f'符合關鍵字的任務:{name} \n委託人士:{person} \n價錢:{money} \n地方:{place} \n網址:{url} ')
        money=money.replace ('單次$','')
        if cannot not in name:
            print(f'任務:{name} \n委託人士:{person} \n價錢:${money} \n地方:{place} \n網址:{url} ')
            print('-'*60)
            count += 1
        #     else:
        #         print(f'不符合關鍵字的任務:{name}')
        #         print('='*60)

        # if count == 0:
        #     print('没有此項目')
        # conn = pymysql.connect(**db_config)
            try:
                with conn.cursor() as cursor:
                    command = f'INSERT INTO mission_list (name, people, price, location, url) VALUES ("{name}", "{person}", {money}, "{place}" ,"{url}")'
                    cursor.execute(command)
                    conn.commit()
                        
            except Exception as ex:
                print(ex)
   

conn.close()
driver.close()
