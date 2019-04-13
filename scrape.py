import parameters
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parsel import Selector

def google_search(query):
    driver.get('https://www.google.com')
    sleep(1)

    search_query = driver.find_element_by_name('q')
    search_query.send_keys(query)
    sleep(0.5)

    search_query.send_keys(Keys.RETURN)
    sleep(1)

    linkedin_urls = driver.find_elements_by_class_name('iUh30')
    linkedin_urls = [url.text for url in linkedin_urls]
    sleep(0.5)

    return linkedin_urls


def login_driver():
    #driver = webdriver.Chrome('~/Downloads/chromedriver/chromedriver')
    driver = webdriver.Chrome()
    driver.get('https://www.linkedin.com')

    username = driver.find_element_by_class_name('login-email')
    username.send_keys(parameters.linkedin_username)
    sleep(0.5)

    password = driver.find_element_by_class_name('login-password')
    password.send_keys(parameters.linkedin_password)
    sleep(0.5)

    sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
    sign_in_button.click()
    sleep(0.5)
    return driver


def get_relevant_people(profile_id):
    url = 'https://www.linkedin.com/in/'+profile_id
    driver.get(url)

    # add a 5 second pause loading each URL
    sleep(2)

    # assigning the source code for the webpage to variable sel
    sel = Selector(text=driver.page_source) 
    #name = driver.find_element_by_css_selector('.topcard__name')
    name = sel.xpath('//*[starts-with(@class, "pv-top-card-section__name")]/text()').extract_first().strip()
    headline = sel.xpath('//*[starts-with(@class, "pv-top-card-section__headline")]/text()').extract_first().strip()
    location = sel.xpath('//*[starts-with(@class, "pv-top-card-section__location")]/text()').extract_first().strip()
    print(name, headline, location)
    #also_viewed = sel.xpath('//*[starts-with(@class, "pv-browsemap-section__member-detail--has-hover")]/text()')
    names = sel.xpath('//*[starts-with(@class, "name")]/text()')
    extracted_names = [name.strip() for name in names.getall()]
    extracted_names = [name for name in filter(None, extracted_names)]
    print(extracted_names)
    #return sel
    return (name, headline, location, extracted_names)


def logout_driver():
    driver.quit()

driver = login_driver()