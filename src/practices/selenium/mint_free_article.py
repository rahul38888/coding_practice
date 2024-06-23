from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
import sys


chrome_options = Options()
chrome_options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 2})
driver = webdriver.Chrome(options=chrome_options)

url = None
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = input("Type your url\n>>> ")

if not url:
    print("Url is required")
    quit(-1)

id_re = re.search(".*-([0-9]*).html", url)
art_id = id_re.groups()[-1]

driver.get(url)

driver.implicitly_wait(0.5)

# document.getElementsByClassName("FirstEle")[0]
# document.getElementById("paywall_11718943046111").getElementsByClassName("long-hidden")[0]

# driver.implicitly_wait(2)

first_para = driver.find_element(by=By.CLASS_NAME, value="FirstEle")
print(first_para.text)
paywall = driver.find_element(by=By.ID, value=f"paywall_{art_id}")
# other_para = paywall.find_element(by=By.CLASS_NAME, value="long-hidden")
print(paywall.text)

if __name__ == '__main__':
    pass
