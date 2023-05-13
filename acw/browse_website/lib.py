from selenium import webdriver

from . import config
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options=ChromeOptions()

options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Safari/537.36"
)

options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--no-sandbox")
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument('--proxy-server='+config.proxy)

driver = webdriver.Chrome('/usr/bin/chromedriver',options=options)

def main(obj):
    if obj['command']=='get':
        driver.get(obj['url'])

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        return ''
    elif obj['command']=='add_header':
        driver.execute_script(obj['header'])
        return ''
    elif obj['command']=='execute_script':
        return driver.execute_script(obj['script'])
    elif obj['command']=='page_source': 
        return driver.page_source

    #driver.quit()
