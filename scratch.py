from selenium import webdriver
from selenium.webdriver.common.by import By

trending_url = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'

driver = webdriver.Chrome()
driver.get(trending_url)
print('---------------------------------------------------')
print('Page title:', driver.title) #page title

container_name = "ytd-video-renderer" #name html class
container_elements = driver.find_elements(By.CSS_SELECTOR, container_name) #Class finder
print('Container name:', container_name) #Name of div
print(f'Found {len(container_elements)} videos') # number of videos

def get_name(i):
    #Name of Video
    video = container_elements[i].find_element(By.ID, 'video-title')
    title = video.get_attribute('title')
    print('Title:', title)
