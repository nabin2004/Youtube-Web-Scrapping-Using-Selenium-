import requests

trending_url = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'

response = requests.get(trending_url)

print("Status Code", response.status_code)
print('Output', response.text[:1000])

with open('trend.html','w') as f:
    f.write(response.text)