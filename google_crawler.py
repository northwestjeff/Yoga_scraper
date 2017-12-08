import csv
from selenium import webdriver
import time

from yogatest import directory_dict


"""
google_crawler.py imports the directory_dict from yoga_scraper and pulls phone number data
from a google search.
"""

#  TEST DATA DELETE WHEN FINISHED
# directory_dict = {"1": {"name": "Asmi yoga",
#                         "address": "blah1",
#                         "city": "Bend",
#                         "state": "barfoo1"},
#                   "2": {"name": "Lotus Seed",
#                         "address": "blah2",
#                         "city": "Portland",
#                         "state": "barfoo2"}
#                   }



# def crawl():
#     timeout = 10
#     try:
#         WebDriverWait(driver, timeout).until(
#             EC.visibility_of_element_located((By.XPATH, "//input[@class='q']")))
#         print("found Q")
#     except TimeoutException:
#         print("Timed out waiting for page to loan")
#         driver.quit()


# def search_terms():
#     for i in directory_dict.keys():
#         city = directory_dict[i]["city"]
#         name = directory_dict[i]["name"]
#         phone = "phone number"
#         keys_input = "{} {} {}".format(name, city, phone)
#         print("search term".format(keys_input))


def phone_element(driver):
    """
    Pulls phone number from the google search
    """
    time.sleep(7)
    parent_element = driver.find_element_by_xpath("//span[@data-local-attribute='d3ph']")
    child_element = parent_element.find_element_by_tag_name("span")
    phone_number = child_element.text
    print("phone number found: {}".format(phone_number))
    return phone_number


def search(term, driver):
    """
    Scans google for the search box.
    Enters search term (name of studio, city, 'phone number')
    submits the search by clicking submit button
    """
    time.sleep(3)
    input_element = driver.find_element_by_name("q")
    print("found lower case q")
    input_element.send_keys(term)
    print("submitting " + term)
    submit = driver.find_element_by_name("btnK")
    print("found submit")
    submit.click()


def scrape(keys_input, dict):
    """
    Creates and opens web driver to google
    calls "search" function above, passing in the search query and the dictionary
    to add the phone number to.  If no phone number class found, adds "none to the
    dict.
    """
    driver = webdriver.Chrome()
    url = 'https://www.google.com'
    driver.get(url)
    try:
        search(keys_input, driver)
        dict["phone"] = phone_element(driver)
        print("found phone: {}".format(dict["phone"]))
    except:
        print("no phone found")
        dict["phone"] = "none"
    driver.close()


def run():
    """
    Exectures the scrape
    """
    for i in list(directory_dict):
        city = directory_dict[i]["city"]
        name = directory_dict[i]["name"]
        phone = "phone number"
        keys_input = "{} {} {}".format(name, city, phone)
        scrape(keys_input, directory_dict[i])


run()

with open('Yoga/yogaPhone.csv', 'w') as f:
    """
    Writes directory (now with a phone number for each entry) to a CSV file
    """
    w = csv.DictWriter(f, fieldnames=['name', "address", "city", "state", "phone"])
    w.writeheader()
    for i in directory_dict.keys():
        w.writerow(directory_dict[i])
