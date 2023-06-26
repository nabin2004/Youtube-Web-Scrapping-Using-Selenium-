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
    video = container_elements[i].find_element(By.ID, 'video-title')
    #link of video
    href = video.get_attribute('href')
    print(f'URL of video: {href}')

#Thumbnail link of video
def get_thumbnail(i):
    thumbnail_tag = container_elements[i].find_element(By.TAG_NAME, 'img')
    thumb = thumbnail_tag.get_attribute('src')
    print(f'URL of thumbnail: {thumb}')

def get_channel_name(i):
    print("-----------------------------------Channel Name------------------------")
    # Channel name
    channel_name = container_elements[i].find_element(By.CSS_SELECTOR, 'a.yt-simple-endpoint.style-scope.yt-formatted-string')
    chan_name = channel_name.text 
    print(f"Channel Name: {chan_name}")



def get_views(i):
    print('--------------------------Views Number-----------------------')
    views = container_elements[i].find_element(By.CSS_SELECTOR, 'span.inline-metadata-item.style-scope.ytd-video-meta-block:nth-of-type(1)')
    views_no = views.text
    print(f"View Counting: {views_no}")
    print('---------------------------------------------------------------')

def get_upload(i):
    print('--------------------------UPLOAD DURATION----------------------------')
    # Extracting Duration
    time_element = container_elements[i].find_element(By.CSS_SELECTOR, 'span.inline-metadata-item.style-scope.ytd-video-meta-block:nth-of-type(2)')
    time_text = time_element.text
    print(f'Upload duration: {time_text}')
    print('----------------------')


def get_duration(i):
    print("-------------------Description---------------------------------")
    description_text = container_elements[i].find_element(By.ID, 'description-text').text
    print(description_text)


def main(i):
    print("============================================================")
    get_name(i)
    get_link(i)
    get_thumbnail(i)
    get_channel_name(i)
    get_views(i)
    get_upload(i)
    get_duration(i)
    print("============================================================")

for i in range(len(container_elements)):
    main(i)
