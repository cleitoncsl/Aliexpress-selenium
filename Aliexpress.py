from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = "https://pt.aliexpress.com/category/201054516/tablets.html?spm=a2g0o.category_nav.1.369.3770609dA0wBh7"

option = Options()
option.headless = True
navegador = webdriver.Firefox(options=option)

navegador.get(url)

div_mae = navegador.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[2]")
html_content = div_mae.get_attribute('outerHTML')
soup = BeautifulSoup(html_content, 'html.parser')

#print(soup.prettify())

#_3t7zg _2f4Ho

#lista_produtos = soup.find_all('div', class_='_3GR-w')

lista_produtos = soup.select('h1._18_85')
lista_preco = soup.find('div', class_="mGXnE _37W_B").select('a span')

for produto in lista_produtos:
    nome_produto = produto.getText()
    print(f' Nome -> {nome_produto}')

#preco_produto = lista_preco[0].getText() + lista_preco[1].getText() + lista_preco[2].getText() + lista_preco[3].getText()
#print(preco_produto)