import requests
from bs4 import BeautifulSoup

#criçaõ de estrura para raspagem
link = 'https://www.bing.com/search?q=cota%C3%A7%C3%A3o+dolar'
#site escolhido para raspagem
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'}
requisicao = requests.get(link, headers=headers)

print(requisicao.text)
print(requisicao)

site = BeautifulSoup(requisicao.text, "html.parser")
print(site.prettify())

print('--------------------------------------')

titulo = site.find('title')
print(titulo)

print('--------------------------------------')

pesquisa = site.find_all('input')
print(pesquisa)
print(pesquisa[1])

print('--------------------------------------')

pesquisa2 = site.find_all ('div', class_='text')
print(pesquisa2)

print('--------------------------------------')

pesquisa3 = site.find_all ('div', class_='b_focusTextSmall curr_totxt')
print(pesquisa3)

print('--------------------------------------')

pesquisa4 = site.find ('div', class_='b_focusTextSmall curr_totxt')
print('O preço do dólar é:', pesquisa4.get_text())

print('--------------------------------------')

pesquisa4 = site.find ('div', class_='b_focusTextSmall curr_totxt')
print('O preço do dólar é:', pesquisa4.get_text())
print(pesquisa4['data-value'])

print('--------------------------------------')
#User-Agent:
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183
