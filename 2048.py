#! python3
# 2048.py game player

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
# Access game webpage
url = 'https://gabrielecirulli.github.io/2048/'
browser = webdriver.Firefox()
browser.get(url)
scores = []

#Game loop
while True:
    main_link = browser.find_element_by_css_selector("html")
    status = browser.find_element_by_css_selector('.game-container p')
    keys=[Keys.RIGHT, Keys.DOWN, Keys.LEFT, Keys.UP]
    while status.text != 'Game over!':
        for i in keys:
            main_link.send_keys(i)
        # Check for game over
        status = browser.find_element_by_css_selector('.game-container p')
    score = browser.find_element_by_css_selector('.score-container').text
    
    #create record of scores
    scores.append(score)
    print(scores)
    # click retry
    retry = browser.find_element_by_css_selector('.retry-button')
    retry.click()
