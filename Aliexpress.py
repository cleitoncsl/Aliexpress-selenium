from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

url = "https://pt.aliexpress.com/category/201054516/tablets.html?spm=a2g0o.category_nav.1.369.3770609dA0wBh7"

delay = 5
option = Options()
option.headless = False
navegador = webdriver.Chrome(options=option)

navegador.get(url)

sleep(5) # Time in seconds

div_mae = navegador.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[2]")
html_content = div_mae.get_attribute('outerHTML')
soup = BeautifulSoup(html_content, 'html.parser')

#print(soup.prettify())

#_3t7zg _2f4Ho

lista_produtos = soup.find('div', class_='_3GR-w')

#lista_produtos = soup.select('h1._18_85')
#lista_preco = soup.find('div', class_="mGXnE _37W_B").select('a span')

for produto in lista_produtos:
    nome_produto = produto.select('h1._18_85')
    print(f'Nome -> {nome_produto[0].getText()}')
    preco_produto = produto.find('div', class_="mGXnE _37W_B").select('a span')
    print(f'Preço -> {preco_produto[0].getText() + preco_produto[1].getText()+ preco_produto[2].getText() + preco_produto[3].getText()}')