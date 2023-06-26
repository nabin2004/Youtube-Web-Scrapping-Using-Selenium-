from selenium import webdriver
from selenium.webdriver.common.by import By
import smtplib
import os
trending_url = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'

driver = webdriver.Chrome()
driver.get(trending_url)

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
    # Channel name
    channel_name = container_elements[i].find_element(By.CSS_SELECTOR, 'a.yt-simple-endpoint.style-scope.yt-formatted-string')
    chan_name = channel_name.text 
    print(f"Channel Name: {chan_name}")



def get_views(i):
    views = container_elements[i].find_element(By.CSS_SELECTOR, 'span.inline-metadata-item.style-scope.ytd-video-meta-block:nth-of-type(1)')
    views_no = views.text
    print(f"View Counting: {views_no}")


def get_upload(i):
    # Extracting Duration
    time_element = container_elements[i].find_element(By.CSS_SELECTOR, 'span.inline-metadata-item.style-scope.ytd-video-meta-block:nth-of-type(2)')
    time_text = time_element.text
    print(f'Upload duration: {time_text}')


def get_description(i):
    description_text = container_elements[i].find_element(By.ID, 'description-text').text
    print(description_text)


def main(i):
    get_name(i)
    get_link(i)
    get_thumbnail(i)
    get_channel_name(i)
    get_views(i)
    get_upload(i)
    get_description(i)
    print("============================================================")

for i in range(len(container_elements)):
    main(i)


#######################################3

# print("---------Sending result to Email---------------")

# def send_email():
#     # Email credentials
#     SENDER_EMAIL = 'olinabin801@gmail.com'
#     RECEIVER_EMAILS = ['nabinoli2004@gmail.com', 'olinabin2004@gmail.com']
#     SENDER_PASSWORD = os.environ.get('GMAIL_PASSWORD')

#     if SENDER_PASSWORD:
#         try:
#             server = smtplib.SMTP('smtp.gmail.com', 587)
#             server.ehlo()
#             server.starttls()
#             server.login(SENDER_EMAIL, SENDER_PASSWORD)

#             subject = 'Hello Nabin, How are you?'
#             body = 'Hi MATE!'

#             email_text = f"""\
#             From: {SENDER_EMAIL}
#             To: {', '.join(RECEIVER_EMAILS)}
#             Subject: {subject}

#             {body}
#             """

#             server.sendmail(SENDER_EMAIL, RECEIVER_EMAILS, email_text)
#             server.close()
#             print("Email sent successfully!")
#         except Exception as e:
#             print("An error occurred while sending the email:", str(e))
#     else:
#         print("Email not sent. Please ensure you have set the GMAIL_PASSWORD environment variable.")


# send_email()
