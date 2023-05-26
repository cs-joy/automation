from selenium import webdriver

url = 'https://www.gmail.com'
chrome_driver_location = '/Users/me/Desktop/gmail account login/utilities/chromedriver'
gmail_username = 'your_gmail_address'
gmail_password = 'your_gmail_password'


driver = webdriver.Chrome(executable_path=chrome_driver_location)

driver.get(url)

driver.implicitly_wait(60)
driver.find_element_by_id('identifierId').send_keys(gmail_username)
driver.find_element_by_id('identifierNext').click()

driver.implicitly_wait(60)
driver.find_element_by_name('password').send_keys(gmail_password)
driver.find_element_by_id('passwordNext').click()
