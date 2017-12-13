import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time

#  Search URL from website.  To use a new URL, take the URL from yogaalliance.org after searching a city or state
url = 'https://www.yogaalliance.org/Directory-Registrants?type=School&location=OR,%20United%20States'

# create new instance of chrome
driver = webdriver.Chrome()

# Direct driver to site of interest
driver.get(url)

list_directory = []

def crawl():
    timeout = 10
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='ya_school-name']")))
    except TimeoutException:
        driver.quit()


def get_names():
    address_parent = driver.find_elements_by_xpath("//div[@class='ya_school-address']")
    addresses = [x.text for x in address_parent]
    addresses = [str(i) for i in addresses]
    addresses = [each.replace("\n", " ") for each in addresses]

    # Creates list of yoga names on the page
    link_parent = driver.find_elements_by_xpath("//h3[@class='ya_school-location-name']//a")
    link_name = [x.text for x in link_parent]
    make_list(zip(link_name, addresses))

    with open("yogafile.csv", "w") as f:
        wr = csv.writer(f)
        for row in list_directory:
            wr.writerow(row)

def next_page():
    try:
        next_not_disabled = driver.find_element_by_xpath(
            "//a[@title='Go to the next page'][not(contains(@class, 'k-state-disabled'))]")  # Not used but serves as a test for the driver
        next_button = driver.find_element_by_xpath("//span[contains(@class, 'k-i-arrow-e')]")
        next_button.click()
        return True
    except NoSuchElementException:
        return False
    except StaleElementReferenceException:
        return False


def make_list(zipped):
    """
    Called in get_names()
    """
    for x in zipped:
        list_directory.append(list(x))


# LOOP through pages
next_enabled = True
while next_enabled == True:
    crawl()
    get_names()
    time.sleep(5)
    next_enabled = next_page()
    time.sleep(7)
driver.quit()
