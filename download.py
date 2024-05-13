from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time


def start():
    global driver
    driver = webdriver.Edge()

    # driver.get("https://www.ultimate-guitar.com/")

    my_tabs_url = 'https://www.ultimate-guitar.com/user/mytabs'
    driver.get(my_tabs_url)

# <a href="https://tabs.ultimate-guitar.com/user/tab/view?h=0iBHGsIFCoYJbL3vrVP22wFt" class="aPPf7 HT3w5 lBssT">Humble And Kind<span data-tip="&quot;Personal tab&quot;" data-for="list-meta-tooltip" data-effect="solid" data-place="right" class="S9GY1" currentitem="false"><span class="S9GY1"><svg viewBox="0 0 16 16" class="is4YP f7_Nl YEJsU P9R6v"><path d="M13.5 13.92c-.013-.32-.022-.5-.026-.542C13.207 10.6 10.908 8.5 8.003 8.5 5.1 8.5 2.8 10.6 2.532 13.375l-.027.235a.525.525 0 0 0 .235.502c.265.173.68.335 1.216.471 1.06.269 2.521.417 4.047.417 1.525 0 2.986-.148 4.047-.417.535-.136.95-.298 1.216-.47.122-.08.2-.144.234-.193zM11 4.25C11 2.438 9.638 1 8 1S5 2.438 5 4.25C5 6.061 6.362 7.5 8 7.5s3-1.439 3-3.25z" fill-rule="nonzero"></path></svg></span></span></a>
#<a href="https://tabs.ultimate-guitar.com/tab/stone-temple-pilots/plush-official-2130323" class="aPPf7 HT3w5 lBssT">Plush</a>



def download(link):
    delay = 15
    print(link)
    driver.get(link)
    
    try:
        e = WebDriverWait(driver, delay).until(EC.any_of(
            EC.element_to_be_clickable((By.XPATH, '//div[text()="Chords"]')),
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Download Pdf"]'))
        ))
        print("text", e.text)
        if 'CHORDS' in e.text.upper():
            e = driver.find_element(By.XPATH, '//div[text()="Chords"]')  
            # e.click()
            driver.execute_script("arguments[0].click()", e)
            try:
                e = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Print"]')))
                e = driver.find_element(By.XPATH, '//span[text()="Print"]')
                # e.click()
                driver.execute_script("arguments[0].click()", e)
            except TimeoutException:
                print("timeout2")
        elif 'DOWNLOAD PDF' in e.text.upper():
            e = driver.find_element(By.XPATH, '//span[text()="Download Pdf"]')  
            # time.sleep(10)
            e.click()
            
    except TimeoutException:
        print("timeout", link)


def get_songlinks():
    global song_links
    song_links = [x.get_attribute('href') for x in driver.find_elements(By.XPATH, "//a[contains(@href, 'https://tabs.ultimate-guitar.com/')]")]


def download_songlinks(offset=0):
    for n, l in enumerate(song_links[offset:]):
        print(n+offset)
        download(l)


# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()