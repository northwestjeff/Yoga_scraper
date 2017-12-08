import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
#
# import requests, html5lib, time

directory_dict = {}

file = open("Yoga/yogafile.csv")
filereader = csv.reader(file, delimiter=",")

yoga_dir = [row for row in filereader]



# remove "map" in the location.  The last five characters pulled in from the scrape
def remove_map():
    """
    Scraper brought in a "map" string. This removes it
    """
    for i in yoga_dir:
        i[1] = i[1][:-5]


def zip_strip():
    """
    Checks for zip code (some have it some dont) and removes it if so
    """
    for i in yoga_dir:
        if i[1][-1].isnumeric():
            i[1] = i[1][:-6]


def usa_normalize():
    """
    Some locations return USA, others United States. Removes both
    """
    for i in yoga_dir:
        key_string = i[1]
        check = "United States"
        if check in key_string:
            i[1] = key_string[:-15]
        else:
            i[1] = key_string[:-5]


def split_city():
    """
    Makes the City its on item on list
    """
    for i in yoga_dir:
        i[1] = i[1].split(" ")
        i.append(i[1][-2])


def split_state():
    """
    Makes the State its on item on list
    """
    for i in yoga_dir:
        i.append(i[1][-1])


def make_dict():
    """
    Converts return to a dict
    """
    for i in yoga_dir:
        directory_dict[i[0]] = {"name": i[0],
                                "address": i[1],
                                'city': i[2],
                                'state': i[3]
                                }


def remove_city_comma():
    """
    Removes a comma
    """
    for i in yoga_dir:
        i[2] = i[2][:-1]


def concat_address():
    """Concatenates the address, which is a list at this point"""
    for i in yoga_dir:
        i[1] = " ".join(i[1])


def clean_data_main():
    """
    Runs the functions
    """
    remove_map()
    usa_normalize()
    zip_strip()
    split_city()
    split_state()
    concat_address()
    remove_city_comma()
    make_dict()


clean_data_main()
