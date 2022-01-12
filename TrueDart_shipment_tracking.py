import time
import sys
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
warnings.filterwarnings("ignore", category=DeprecationWarning)

link = 'https://www.bluedart.com/web/guest/trackdartresultthirdparty?trackFor=0&trackNo='
trackno="50894961924"

options = webdriver.ChromeOptions() 
options.add_argument('log-level=3')
options.add_argument('disable-gpu')
options.add_argument('disable-infobars')
options.add_argument('disable-extensions')
options.add_argument('headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
w = webdriver.Chrome(options=options)

xpath = '//*[@id="50894961924-rdrmv"]/div/div/div[1]/div[2]/ul/li[2]/p'
data_table_xpath ='//*[@id="SCAN50894961924"]/div/table/tbody'
status_xpath = "//*[contains(text(), ' Status and Scan ')]"

def check():
    count=0
    url = link+trackno
    while True:
        w.get(url)
        WebDriverWait(w, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
        w.find_element_by_xpath(status_xpath).click()
        data_l = w.find_element_by_xpath(data_table_xpath).text
        c_data=data_l.split('\n', 1)[0]
        count += 1
        sys.stdout.write("\r")
        sys.stdout.write("\t{}".format(c_data)+'\t'+"{:2d} times checked.".format(count))
        sys.stdout.flush()
        time.sleep(100)
check()
