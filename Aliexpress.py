from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from collections import Counter


url = "https://pt.aliexpress.com/category/201054516/tablets.html?spm=a2g0o.category_nav.1.369.3770609dA0wBh7"

sleep(1) # Time in seconds

def click_button (navegador, name_button, id_delay):
    try:
        delay = id_delay
        # Localizando o Campo Operacao
        _ = WebDriverWait(navegador, delay).until(
            ec.visibility_of_all_elements_located((
                By.XPATH, name_button)))

        navegador.execute_script("window.scrollTo(0,1000,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,1500,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,2000,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,2500,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,3000,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,3500,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,4000,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,4500,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,5000,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,1000,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,0, document.body.scrollHeight)")

        print(f'-> Cache da página executado')

    except NoSuchElementException:
        print(f'-> ###Campo não encontrado###')
        navegador.quit()


if __name__ == "__main__":
    delay = 5
    site = "https://pt.aliexpress.com"
    option = Options()
    option.headless = False
    navegador = webdriver.Chrome(options=option)

    navegador.get(url)
    click_button(navegador, "//div[@id='root']/div/div/div[2]", 30)


div_mae = navegador.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[2]")

sleep(1)
html_content = div_mae.get_attribute('outerHTML')
sleep(1)
soup = BeautifulSoup(html_content, 'html.parser')


#print(soup.prettify())

# _3t7zg _2f4Ho

# _1kNf9

# _2jcMA

# eXPaM

# _3t7zg _2f4Ho

# a class="_3t7zg _2f4Ho"

#lista_produtos = soup.find_all('div', class_='_3GR-w')
lista_produtos = soup.find_all('a', attrs={'class': '_3t7zg _2f4Ho'})

sleep(1)

contador = 0

for produto in lista_produtos:
    sleep(0.1)
    print(f'----------------------------------------ID-{contador}----------------------------------------------------------------------')
    nome_produto = produto.select('h1._18_85')
    sleep(0.1)
    print(f'Nome -> {nome_produto[0].getText()}')
    preco_produto = produto.find('div', class_="mGXnE _37W_B").select('a span')
    sleep(0.1)
    try:
        print(f'Preço -> {preco_produto[0].getText() + preco_produto[1].getText() + preco_produto[2].getText() + preco_produto[3].getText()}')
    except Exception as e:
        print(f'Preço -> {preco_produto[0].getText() + preco_produto[1].getText()}')

    sleep(0.1)
    qtde_vendas = produto.select("span._1kNf9")
    sleep(0.1)
    try:
        if qtde_vendas is None:
            print('qtde_vendas -> -')
        else:
            print(f'qtde_vendas -> {qtde_vendas[0].getText()}')
    except Exception as e:
        print(f'qtde_vendas -> -')

    tipo_frete = produto.select("span._2jcMA")
    sleep(0.1)
    try:
        if tipo_frete is None:
            print('Frete -> -')
        else:
            print(f'Frete -> {tipo_frete[0].getText()}')
    except Exception as e:
        print(f'Frete -> -')

    tipo_devolucao = produto.select("span._2jcMA")
    sleep(0.1)
    try:
        if tipo_devolucao is None:
            print('Frete -> -')
        else:
            print(f'Devolução -> {tipo_devolucao[1].getText()}')
    except Exception as e:
        print(f'Devolução -> -')

    avaliacoes = produto.select("span.eXPaM")
    sleep(0.1)
    try:
        if avaliacoes is None:
            print('Avaliações -> -')
        else:
            print(f'Avaliações -> {avaliacoes[0].getText()}')
    except Exception as e:
        print(f'Avaliações -> -')

    loja = produto.select("span._7CHGi")
    sleep(0.1)
    try:
        if loja is None:
            print('Loja -> -')
        else:
            print(f'Loja -> {loja[0].getText()}')
    except Exception as e:
        print(f'Loja -> -')

    link_produto = [a['href'] for a in soup.find_all('a', href=True) if a.text]
    if contador == 0:
        x = contador
        link_produto_final = link_produto[x]
    elif (contador % 2) == 0:
        x = contador * 2
        link_produto_final = link_produto[x]
    else:
        x = contador * 2
        link_produto_final = link_produto[x]
    try:
        if link_produto_final is None:
            print('Loja -> -')
        else:
            print(f'Loja -> {site + link_produto_final}')

    except Exception as e:
        print(f'Loja -> -')

    promocao = produto.find_all('img', class_='_1mroo')
    len_promocao = len(promocao)
    texto_promocao = str(promocao)
    sleep(0.1)
    try:
        if texto_promocao.count('https') is None:
            print('Promocao? -> (n)')
        else:
            print(f'Promocao? -> (s)')
    except Exception as e:
        print(f'Loja -> -')

    top_selling  = produto.find_all('img', class_='_1mroo')
    len_top_selling  = len(top_selling )
    texto_top_selling  = str(top_selling )
    sleep(0.1)
    try:
        if top_selling.count('https') is None:
            print('Promocao? -> (n)')
        else:
            print(f'Promocao? -> (s)')
    except Exception as e:
        print(f'Loja -> -')

    contador += 1


navegador.quit()