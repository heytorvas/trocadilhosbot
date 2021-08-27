import requests, json
from bs4 import BeautifulSoup

response = requests.get('https://www.dicionariopopular.com/trocadilhos-divertidos-engracados/').text
soup = BeautifulSoup(response, 'html.parser')

article_body = soup.find('div', {'class': 'article--body'})
li_list = article_body.find_all('li')

joke_list = []
for li in li_list:
    if '?' in li.text:
        joke = str(li.text).split('?')
        question = joke[0] + '?'
        answer = joke[1].replace(';', '').strip()
        joke_list.append({
            'question': question,
            'answer': answer
        })

with open('jokes.json', 'w') as f:
    json.dump(joke_list, f, ensure_ascii=False, indent = 4)
