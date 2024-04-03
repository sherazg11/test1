from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get('https://www.espncricinfo.com/')

score_elements = driver.find_elements(By.XPATH, "//div[@class='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo']")

for element in score_elements:

    team_name_element = element.find_element(By.TAG_NAME, 'p')

    team_name = team_name_element.text

    print("Team Name:", team_name)

    score_element = element.find_element(By.XPATH, "//div[@class='ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap']")

    score = score_element.text

    print("Score:", score)

driver.quit()
