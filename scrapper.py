import requests
from bs4 import BeautifulSoup

trending_url = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'

response = requests.get(trending_url)

print("Status Code", response.status_code)
# print('Output', response.text[:1000])

try:
    with open('trend.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
        print("File written successfully.")
except Exception as e:
    print("An error occurred while writing to the file:", str(e))

doc = BeautifulSoup(response.text, 'html.parser')
print('Page title:', doc.title.text)

# Container name: style-scope ytd-video-renderer

video_divs = doc.find_all('div',
class_='style-scope ytd-video-renderer')

print(f'Found {len(video_divs)} videos')