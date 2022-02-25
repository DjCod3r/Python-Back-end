
from bs4 import BeautifulSoup
import requests

url ='https://pt.stackoverflow.com/questions/tagged/python'


response = requests.get(url)


#print(response.text)

contador = 0
#passando o HTML para o BeautifulSoup
html = BeautifulSoup(response.text, 'html.parser')
for pergunta in html.select('.s-post-summary--content'):
    titulo = pergunta.select_one('.s-post-summary--content-title').text
    data = pergunta.select_one('.relativetime').text
    print(titulo)
    print(data)
    if data == 'ontem':
        contador += 1


print("Perguntas criadas a ontem " + str(contador))


