#! python3
# flickr.py - automatically download images from flickr
from selenium import webdriver
import requests, os

# User inputs what theme to download
search_item = input()

# Access flickr
browser = webdriver.Firefox()
browser.get("https://www.flickr.com/search/?text=" + str(search_item))
main_links = browser.find_elements_by_class_name("overlay")

# Get links to all images on the first page
links = []
for i in main_links:
    links.append(i.get_attribute("href"))
    links
# access each link and find source image

for z in links:
    browser.get(z)
    userElem = browser.find_element_by_class_name("main-photo")
    attr = userElem.get_attribute("src")
    res = requests.get(attr)
    res.raise_for_status()

    # save pictures in direcotry
    imageFile = open(os.path.join("flickr", os.path.basename(attr)), "wb")
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
