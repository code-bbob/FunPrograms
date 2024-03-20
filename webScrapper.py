import requests
from bs4 import BeautifulSoup

url = 'https://youthtech.com.np/index.php?route=information/blog'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Find all the main section headings
main_headings = soup.find_all('div', class_='row')
print(main_headings)
# Extract and print the headings
for heading in main_headings:
    print(heading.text)
