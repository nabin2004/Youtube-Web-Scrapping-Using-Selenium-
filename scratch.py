from selenium import webdriver
from selenium.webdriver.common.by import By

trending_url = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'

driver = webdriver.Chrome()
driver.get(trending_url)
print('Page title:', driver.title)

container_name = "ytd-video-renderer"
container_elements = driver.find_elements(By.CSS_SELECTOR, container_name)
print('Container name:', container_name)
print(f'Found {len(container_elements)} videos')

title_element = container_elements[0].find_element(By.ID, 'video-title')
title = title_element.get_attribute('title')
print('Title:', title)

