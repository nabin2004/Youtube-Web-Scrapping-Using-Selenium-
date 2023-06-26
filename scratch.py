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

def get_link(i):
    #link of video
    href = video.get_attribute('href')
    print(f'URL of video: {href}')


#Thumbnail link of video
thumbnail_tag = container_elements[0].find_element(By.TAG_NAME, 'img')
thumb = thumbnail_tag.get_attribute('src')
print(f'URL of thumbnail: {thumb}')

print("-----------------------------------Channel Name------------------------")
# Channel name
channel_name = container_elements[0].find_element(By.CSS_SELECTOR, 'a.yt-simple-endpoint.style-scope.yt-formatted-string')
chan_name = channel_name.text 
print(f"Channel Name: {chan_name}")


print('--------------------------Views Number-----------------------')
# Views Number
# views = container_elements[0].find_element(By.CSS_SELECTOR, 'div.span.inline-metadata-item style-scope ytd-video-meta-block')
views = container_elements[0].find_element(By.CSS_SELECTOR, 'span.inline-metadata-item.style-scope.ytd-video-meta-block:nth-of-type(1)')
views_no = views.text
print(f"View Counting: {views_no}")
print('---------------------------------------------------------------')

print('--------------------------UPLOAD DURATION----------------------------')
# Extracting Duration
time_element = container_elements[0].find_element(By.CSS_SELECTOR, 'span.inline-metadata-item.style-scope.ytd-video-meta-block:nth-of-type(2)')
time_text = time_element.text
print(f'Upload duration: {time_text}')
print('----------------------')
print("-------------------Description---------------------------------")
description_text = container_elements[0].find_element(By.ID, 'description-text').text
print(description_text)

print('----------------------------------------------------')