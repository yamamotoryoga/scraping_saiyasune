import time
import re
import gspread
import settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from oauth2client.service_account import ServiceAccountCredentials 

# 変数定義
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)
JANcode_price = []

# スプレッドシートに接続するためのテンプレ
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(settings.json_key, scope)
gc = gspread.authorize(credentials)
SPREADSHEET_KEY = settings.spredsheet_key
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

#A列のJANコードを取得
JANcode_list = worksheet.col_values(1)

# 検索対象から、最安値ドットコムの検索ページを指定, 動作がわかるようにJANcodeをprint
JANcode_number = len(JANcode_list)
for JAN_num in range(JANcode_number):
    print(JANcode_list[JAN_num])
    url = 'https://www.saiyasune.com/J' + JANcode_list[JAN_num] + '.html'
    driver.get(url)
    time.sleep(2)

    # 値段取得
    price_info = driver.find_element_by_id('p_dt25')
    price = price_info.text
    JANcode_price.append(re.sub(',|¥', '', price))
    
driver.quit()

# スプレッドシートへの書き込み
print('スプレッドシートへ書き込み中...')
JANcode_price_number = len(JANcode_price)
for JAN_p_num in range(JANcode_price_number):
    worksheet.update_cell(JAN_p_num + 1, 2, JANcode_price[JAN_p_num])
