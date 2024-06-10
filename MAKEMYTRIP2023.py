# MAKE MY TRIP PRICE COLLECTOR



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
url = 'https://www.makemytrip.com/flight/search?itinerary=-BLR-24/12/2023_BLR-DEL-27/12/2023&tripType=R&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng'
driver.get(url)

# Wait for the dynamic content to load
element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/span'))
)

# Click the element to trigger the dynamic content loading
element.click()

# Wait for a moment to ensure the dynamic content is loaded
sleep(20)

# Get the updated page source
content = driver.page_source

# Close the browser
driver.quit()

# Now, you can use BeautifulSoup to extract the price
soup = BeautifulSoup(content, 'html.parser')
all_data=[]
all_ele=soup.find_all('div',class_="makeFlex spaceBetween appendBottom15")
for i in all_ele:
    print(i.text)
# span,class="boldFont blackText"   name

# price = soup.find_all('p', class_="blackText fontSize16 blackFont")
