from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
import requests
from PIL import Image
import requests
from io import BytesIO
from selenium.webdriver.common.keys import Keys



def move_right(driver,source):
	action = ActionChains(driver)
	action.send_keys(Keys.ARROW_RIGHT).perform()

def move_left(driver,source):
	action = ActionChains(driver)
	# target = driver.find_element_by_xpath('//*[@id="matchListNoMessages"]')
	# action.drag_and_drop(source, target).perform()
	action.send_keys(Keys.ARROW_LEFT).perform()
	# action.drag_and_drop_by_offset(source,150,250).perform()


option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})
           
           
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = option)
# driver = webdriver.PhantomJS()
driver.get('https://tinder.com/app/recs')


time.sleep(2)
driver.find_element_by_xpath('//span[text()="Log in"]').click()
time.sleep(2)
driver.find_element_by_xpath('//span[text()="Log in with Facebook"]').click()
time.sleep(2)
driver.switch_to_window(driver.window_handles[1])
# driver.find_element_by_name('email').click()
time.sleep(2)
driver.find_element_by_name('email').send_keys('')
driver.find_element_by_name('pass').send_keys('')
driver.find_element_by_name('login').click()
time.sleep(2)
driver.switch_to_window(driver.window_handles[0])
time.sleep(8)
# driver.find_element_by_xpath('//span[text()="Allow"]').click()
# time.sleep(1)
# driver.find_element_by_xpath('//span[text()="Enable"]').click()
url_links = []


webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
def attractiveness(url):
	attractive = 0
	try:
		api = 'https://api.haystack.ai/api/image/analyze?apikey=bcc555e7f0a8f53f04f3f2abeae71611&output=json&model=attractiveness'
		response = requests.get(url)
		img = Image.open(BytesIO(response.content))
		buf = BytesIO()
		img.save(buf, format='PNG')
		buf.seek(0)
		print("OK we here")
		files = {'image':( 'Mustafa.jpeg', buf,'image/*')}
		post = requests.post(api,files = files)
		print("Score")
		attractive = (int(post.json()['people'][0]['attractiveness']))
		print("OK we here")
	except Exception as e:
		print(e)
	finally:
		return attractive


while True:
	webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
	soup = BeautifulSoup(driver.page_source,'lxml')
	# print(soup)
	urls = soup.find_all("span",{"class":"keen-slider__slide Wc($transform) Fxg(1)"})
	url_links.append(urls)
	# print(urls[len(urls)-5])
	elem = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/span[1]/div')
	# print(elem)
	url = elem.value_of_css_property("background-image")[5:-2]

	# print(url)
	#Continue the Api Calling later ... 
	#Onto the swiping

	# action = ActionChains(driver)
	source = elem
	attractive = 10
	print("Score "+ str(attractive))
	if(attractive>5):
		move_right(driver,source)
		print("moving right")
		webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
		time.sleep(2)
	else:
		print("moving left")
		move_left(driver,source)
		webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
		time.sleep(2)
		# print(driver.window_handles)

	
	# print(source)
	# right_move = action.drag_and_drop_by_offset(source,300,250).perform()
	# left_move = action.drag_and_drop_by_offset(source,150,250).perform()
	# move_left(driver,source)
	# move_right(driver,source)














