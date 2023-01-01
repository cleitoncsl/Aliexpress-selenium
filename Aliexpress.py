import pandas as pd
import os
import re
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from collections import Counter

velocimento = 0.0039

url = "https://www.aliexpress.com/"

sleep(velocimento) # Time in seconds

os.system("taskkill /f /im chromedriver.exe")
os.system("taskkill /f /im msedge.exe")

def click_button (navegador, name_button, id_delay):
    try:
        delay = id_delay
        # Localizando o Campo Operacao
        _ = WebDriverWait(navegador, delay).until(
            ec.visibility_of_all_elements_located((
                By.XPATH, name_button)))

        navegador.execute_script("window.scrollTo(0,1000,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,1500,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,2000,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,2500,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,3000,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,3500,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,4000,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,4500,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,5000,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,5500,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,6000,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,6500,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,7000,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,7500,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,8000,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,8500,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,9000,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,9500,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,10000,document.body.scrollHeight)")
        sleep(0.5)
        navegador.execute_script("window.scrollTo(0,0, document.body.scrollHeight)")

        print(f'-> Cache da página executado')

    except NoSuchElementException:
        print(f'-> ###Campo não encontrado###')
        navegador.quit()


if __name__ == "__main__":
    delay = 10
    site = "https://www.aliexpress.com/"

    #------------CHROME------------#
    #option = Options()
    #option.add_argument("incognito")
    #option.add_argument("disable-notifications")
    #option.add_argument("disable-infobars")
    #option.add_argument("disable-extensions")
    #option.add_argument("start-minimized")
    #option.add_argument("headless")
    #option.headless = False
    #navegador = webdriver.Chrome(options=option)
    # ------------CHROME------------#

    # ------------EDGE------------#
    option = webdriver.EdgeOptions()
    option.add_argument("start-minimized")
    option.add_argument("disable-notifications")
    option.add_argument("disable-extensions")
    option.add_argument("inprivate")
    #option.add_argument("headless")
    option.headless = False
    navegador = webdriver.Edge(options=option)
    # ------------EDGE------------#

    navegador.get(url)
    sleep(5)
    ######################################## ACEITAR OS COOKIES ########################################
    # cookie_accept = navegador.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[3]/div[2]")
    try:
        cookie_accept = WebDriverWait(navegador, delay).until(ec.element_to_be_clickable((By.CLASS_NAME, "_24EHh"))).click()
        print(f'Cookies Aceitos')
    except Exception as e:
        print(f'Cookies Aceitos')
    sleep(velocimento)
    ######################################## ACEITAR OS COOKIES ########################################

    ######################################## CAMPO PESQUISA ########################################
    # campo_pesquisa = navegador.find_element(By.ID, "search-key")
    try:
        campo_pesquisa = WebDriverWait(navegador, delay).until(ec.element_to_be_clickable((By.ID, "search-key")))
    except Exception as e:
        campo_pesquisa = WebDriverWait(navegador, delay).until(ec.element_to_be_clickable((By.CLASS_NAME, "search-key")))
    ######################################## CAMPO PESQUISA ########################################

    #produto = "XIAOMI MI PAD 5"
    produto = "XIAOMI MI PAD 5"
    #produto = input("Digite o produto desejado: ")
    campo_pesquisa.send_keys(produto)
    botao_lupa = WebDriverWait(navegador, delay).until(ec.element_to_be_clickable((By.CLASS_NAME, "search-button")))
    botao_lupa.click()
    sleep(velocimento)
    print(f'PRODUTO: {produto.upper()}')

    ######################################## CAMPO PESQUISA ########################################

    click_button(navegador, "//div[@id='root']/div/div/div[2]", 15)
    sleep(velocimento)

    ######################################## DIV MAE ########################################

codigo_fonte = navegador.page_source
codigo_fonte = BeautifulSoup(codigo_fonte,'html.parser')
codigo_fonte = str(codigo_fonte)
codigo_fonte = re.findall(r'</path></svg></span></div></div><div class=.{0,100}><a class', codigo_fonte)
codigo_fonte = str(codigo_fonte[0])
codigo_fonte = re.findall(r'=\".{0,50}\" data', codigo_fonte)
codigo_fonte = str(codigo_fonte[0])
codigo_fonte = re.findall(r'\".+\"', codigo_fonte)
codigo_fonte = str(codigo_fonte[0])
codigo_fonte = re.sub(r'"\[', '',codigo_fonte)
codigo_fonte = codigo_fonte.replace('"','')

######################################## DIV MAE ########################################


# div_mae = navegador.find_element(By.XPATH, "/html[1]/body[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]")
div_mae = WebDriverWait(navegador, delay).until(ec.element_to_be_clickable((By.CLASS_NAME, codigo_fonte)))
sleep(1)
html_content = div_mae.get_attribute('outerHTML')
sleep(1)
soup = BeautifulSoup(html_content, 'html.parser')
sleep(2)
#print(soup.prettify())

# _3t7zg _2f4Ho

# _1kNf9

# _2jcMA

# eXPaM

# _3t7zg _2f4Ho

# a class="_3t7zg _2f4Ho"

#lista_produtos = soup.find_all('div', class_='_3GR-w')
# str_soup = str(soup)
#par_lista_produto = re.findall(r'<a class=.+', str_soup)
#par_lista_produto = str(par_lista_produto)
#par_lista_produto = re.findall(r'a class=.{0,50} href', par_lista_produto)
#par_lista_produto = par_lista_produto[0]
#par_lista_produto = par_lista_produto.replace('a class="','')
#par_lista_produto = par_lista_produto.replace('" href','')

######################################## DIV PRODUTO ########################################

codigo_fonte_produto = str(soup)
codigo_fonte_produto = re.findall(r'</a></span></div></a><a class=.{0,100}\" href', codigo_fonte_produto)
codigo_fonte_produto = str(codigo_fonte_produto[0])
codigo_fonte_produto = re.findall(r'\".{0,100}\"', codigo_fonte_produto)
codigo_fonte_produto = str(codigo_fonte_produto[0])
codigo_fonte_produto = re.findall(r'\".+\"', codigo_fonte_produto)
codigo_fonte_produto = str(codigo_fonte_produto[0])
codigo_fonte_produto = codigo_fonte_produto.replace('"','')
lista_produtos = soup.find_all('a', class_=codigo_fonte_produto)
sleep(1)

######################################## DIV PRODUTO ########################################

contador = 0
contador_page = 5
i = 0
set_lista_contador = []
set_produto = []
set_preco_produto = []
set_qtde_vendas = []
set_tipo_frete = []
set_tipo_devolucao = []
set_avaliacoes = []
set_loja = []
set_link_produto = []
set_link_loja = []
set_promocao = []
set_top_selling = []
botao = WebDriverWait(navegador, delay).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/ul/li[9]')))
sleep(velocimento)

while i  <= contador_page:

    for produto in lista_produtos:
        #--REGEX NOME PRODUTO

        codigo_nome_produto = str(produto)
        codigo_nome_produto = re.findall(r'<h1 class=.{0,250} </h1', codigo_nome_produto)
        codigo_nome_produto = str(codigo_nome_produto)
        codigo_nome_produto = re.findall(r'\".{0,250}\">', codigo_nome_produto)
        codigo_nome_produto = str(codigo_nome_produto)
        codigo_nome_produto = re.sub(r"\[|\]|>|\\|\"|'",'', codigo_nome_produto)
        codigo_nome_produto = str(codigo_nome_produto)

        #--REGEX NOME PRODUTO

        sleep(velocimento)
        print(f'----------------------------------------ID-{contador}----------------------------------------------------------------------')
        ######################################## NOME PRODUTO ########################################
        #
        nome_produto = produto.select('h1', class_=codigo_nome_produto)
        sleep(velocimento)
        print(f'NOME -> {nome_produto[0].getText()}')
        vNome_produto = nome_produto[0].text
        set_produto.append(vNome_produto)
        sleep(velocimento)
        #
        ######################################## NOME PRODUTO ################################################################################ PRODUTO ########################################

        ######################################## PRECO PRODUTO ########################################
        #--REGEX PREÇO PRODUTO

        codigo_preco_produto = str(produto)
        codigo_preco_produto = re.findall(r'\"><div class=\".{0,50}\"><span style=', codigo_preco_produto)
        codigo_preco_produto = str(codigo_preco_produto)
        codigo_preco_produto = re.findall(r'\".{0,250}\">', codigo_preco_produto)
        codigo_preco_produto = str(codigo_preco_produto)
        codigo_preco_produto = re.sub(r"><div class=|\[|\']|>|\\|\"|'\"|'|=",'', codigo_preco_produto)
        codigo_preco_produto = str(codigo_preco_produto)
        sleep(velocimento)

        #--REGEX PREÇO PRODUTO
        preco_produto = produto.find('div', class_=codigo_preco_produto).select('a span')
        tam_preco = len(preco_produto)
        sleep(velocimento)
        try:
            if tam_preco == 6:
                print(f'PRECO -> {preco_produto[0].getText() + preco_produto[1].getText() + preco_produto[2].getText() + preco_produto[3].getText() + preco_produto[4].getText() + preco_produto[5].getText()}')
                vPreco_produto = {preco_produto[0].getText() + preco_produto[1].getText() + preco_produto[2].getText() + preco_produto[3].getText() + preco_produto[4].getText() + preco_produto[5].getText()}
                vPreco_produto = str(vPreco_produto)
                vPreco_produto = re.sub(r"{|}|\'|R\$",'', vPreco_produto)
                set_preco_produto.append(vPreco_produto)

            elif tam_preco == 5:
                print(f'PRECO -> {preco_produto[0].getText() + preco_produto[1].getText() + preco_produto[2].getText() + preco_produto[3].getText() + preco_produto[4].getText()}')
                vPreco_produto = {preco_produto[0].getText() + preco_produto[1].getText() + preco_produto[2].getText() + preco_produto[3].getText() + preco_produto[4].getText()}
                vPreco_produto = str(vPreco_produto)
                vPreco_produto = re.sub(r"{|}|\'|R\$",'', vPreco_produto)
                set_preco_produto.append(vPreco_produto)



            elif tam_preco == 4:
                print(f'PRECO -> {preco_produto[0].getText() + preco_produto[1].getText() + preco_produto[2].getText() + preco_produto[3].getText()}')
                vPreco_produto = {preco_produto[0].getText() + preco_produto[1].getText() + preco_produto[2].getText() + preco_produto[3].getText()}
                vPreco_produto = str(vPreco_produto)
                vPreco_produto = re.sub(r"{|}|\'|R\$",'', vPreco_produto)
                set_preco_produto.append(vPreco_produto)

            elif tam_preco == 3:
                print(f'PRECO -> {preco_produto[0].getText() + preco_produto[1].getText() + preco_produto[2].getText() }')
                vPreco_produto = {preco_produto[0].getText() + preco_produto[1].getText() + preco_produto[2].getText() }
                vPreco_produto = str(vPreco_produto)
                vPreco_produto = re.sub(r"{|}|\'|R\$",'', vPreco_produto)
                set_preco_produto.append(vPreco_produto)

            elif tam_preco == 2:
                print(f'PRECO -> {preco_produto[0].getText() + preco_produto[1].getText() }')
                vPreco_produto = {preco_produto[0].getText() + preco_produto[1].getText() }
                vPreco_produto = str(vPreco_produto)
                vPreco_produto = re.sub(r"{|}|\'|R\$",'', vPreco_produto)
                set_preco_produto.append(vPreco_produto)

            elif tam_preco == 1:
                print(f'PRECO -> {preco_produto[0].getText()}')
                vPreco_produto = {preco_produto[0].getText()}
                vPreco_produto = str(vPreco_produto)
                vPreco_produto = re.sub(r"{|}|\'|R\$",'', vPreco_produto)
                set_preco_produto.append(vPreco_produto)

        except Exception as e:
            print(f'PRECO -> 0')
            vPreco_produto = 0
            sleep(velocimento)
        # set_preco_produto.append(vPreco_produto) <-deletar
        ######################################## PRECO PRODUTO ########################################

        ######################################## QTDE PRODUTO ########################################
        qtde_vendas = produto.select("span.manhattan--trade--2PeJIEB")
        sleep(velocimento)
        try:
            if qtde_vendas is None or len(qtde_vendas) == 0:
                print('QTDE VENDAS -> 0')
                vQtde_Vendas = 0
                set_qtde_vendas.append(vQtde_Vendas)

            else:
                print(f'QTDE VENDAS -> {qtde_vendas[0].getText()}')
                vQtde_Vendas = qtde_vendas[0].getText()
                vQtde_Vendas = str(vQtde_Vendas)
                vQtde_Vendas = re.sub(r"  vendido\(s\)",'', vQtde_Vendas)
                set_qtde_vendas.append(vQtde_Vendas)

        except Exception as e:
            print(f'QTDE VENDAS -> -')
            set_qtde_vendas.append(0)
        ######################################## QTDE PRODUTO ########################################


        ######################################## TIPO FRETE ########################################
        tipo_frete = produto.select("span.tag--textStyle--vcAi3Rh")
        sleep(velocimento)
        try:

            tam_campo_frete = len(tipo_frete)
            if tam_campo_frete == 2:
                print(f'TIPO FRETE -> {tipo_frete[1].getText()}')
                vTipo_Frete = {tipo_frete[1].getText()}
                set_tipo_frete.append(vTipo_Frete)

            elif tam_campo_frete == 1:
                print(f'TIPO FRETE -> {tipo_frete[0].getText()}')
                vTipo_Frete = {tipo_frete[0].getText()}
                set_tipo_frete.append(vTipo_Frete)

            else:
                print('TIPO FRETE -> 0')
                set_tipo_frete.append(0)

        except Exception as e:
            print(f'Erro')


        sleep(velocimento)
        ######################################## TIPO FRETE ########################################

        ######################################## TIPO DEVOLUCAO ########################################
        tipo_devolucao = produto.select("span._2jcMA")
        sleep(velocimento)
        try:
            if tipo_devolucao is None:
                print('DEVOLUCAO -> -')
                vTipo_Devolucao = tipo_devolucao[0].getText()

            else:
                print(f'DEVOLUCAO -> {tipo_devolucao[1].getText()}')
                vTipo_Devolucao = tipo_devolucao[0].getText()

        except Exception as e:
            print(f'DEVOLUCAO -> -')
            vTipo_Devolucao = "-"
        set_tipo_devolucao.append(vTipo_Devolucao)

        ######################################## TIPO DEVOLUCAO ########################################

        ######################################## AVALICAOES ########################################
        avaliacoes = produto.select("span.manhattan--evaluation--3cSMntr")
        sleep(velocimento)
        try:
            if avaliacoes is None: #avaliacoes
                print('AVALIACOES -> -')
                vAvaliacoes = "-"
            else:
                print(f'AVALIACOES -> {avaliacoes[0].getText()}')
                vAvaliacoes = avaliacoes[0].getText()

        except Exception as e:
            print(f'AVALIACOES -> -')
            vAvaliacoes = "-"

        set_avaliacoes.append(vAvaliacoes)
        ######################################## AVALICAOES ########################################

        ######################################## LOJA ########################################
        loja = produto.select("a.cards--storeLink--1_xx4cD")
        sleep(velocimento)
        try:
            if loja is None:
                print('LOJA -> -')
                vLoja = "-"

            else:
                print(f'LOJA -> {loja[0].getText()}')
                vLoja = loja[0].getText()

        except Exception as e:
            print(f'LOJA -> -')
            vLoja = "-"

        set_loja.append(vLoja)
        sleep(velocimento)
        ######################################## LOJA ########################################

        ######################################## LINK PRODUTO ########################################
        link_produto = [a['href'] for a in soup.find_all('a', href=True) if a.text]
        try:
            if contador == 0:
                x = contador
                link_produto_final = link_produto[x]
                vLinkProdutoFinal = "https:" + link_produto_final
                set_link_produto.append(vLinkProdutoFinal)
                print(f'LINK PRODUTO -> {"https:" + link_produto_final}')

            elif (contador % 2) == 0:
                contador
                x = contador
                link_produto_final = link_produto[x]
                set_link_produto.append(vLinkProdutoFinal)
                print(f'LINK PRODUTO -> {"https:" + link_produto_final}')

            elif link_produto_final is None:
                print('LINK PRODUTO -> -')
                vLinkProdutoFinal = "-"
                set_link_produto.append(vLinkProdutoFinal)

            else:
                x = contador + 1
                link_produto_final = link_produto_final
                set_link_produto.append(vLinkProdutoFinal)
                print(f'LINK PRODUTO -> {"https:" + link_produto_final}')

        except Exception as e:
            link_produto_final
            set_link_produto.append(vLinkProdutoFinal)
            print(f'LINK PRODUTO -> {"https:" + link_produto_final}')

        sleep(velocimento)
        ######################################## LINK PRODUTO ########################################

        ######################################## LINK LOJA ########################################
        try:
            link_loja = link_produto[x + 1]
            tam_link_loja = len(link_loja)

            if tam_link_loja is None:
                vLinkLojaFinal = 0
                set_link_loja.append(vLinkLojaFinal)
                print(f'LINK LOJA - > -')

            else:
                vLinkLojaFinal = "https:" + link_loja
                set_link_loja.append(vLinkLojaFinal)
                print(f'LINK LOJA - >{"https:" + vLinkLojaFinal}')


        except Exception as e:
                    vLinkLojaFinal
                    set_link_loja.append(vLinkLojaFinal)
                    print(f'LINK LOJA - > {"https:" + link_loja}')

        sleep(velocimento)
        ######################################## LINK LOJA ########################################

        ######################################## PROMOCAO ########################################
        promocao = produto.select("span.tag--textStyle--vcAi3Rh")

        try:
            len_promocao = len(promocao)
            if len_promocao == 2:
                print(f'PROMOCAO -> {promocao[0].getText()}')
                vTipo_Frete = {promocao[0].getText()}
                set_promocao.append(vTipo_Frete)

            else:
                print(f'PROMOCAO -> (n)')
                set_promocao.append("(n)")

        except Exception as e:
            print(f'PROMOCAO -> -')
            vPromocao = "(n)"
            sleep(velocimento)

        ######################################## PROMOCAO ########################################

        ######################################## TOP SELLING ########################################
        top_selling = produto.find_all('img', class_='tag--imgStyle--1hJHaAY')
        sleep(velocimento)
        try:
            top_selling = len(top_selling[0].get('src'))
            if top_selling is None:
                print('TOP SELLING? -> (n)')
                v_top_selling = "(n)"
                set_top_selling.append(v_top_selling)

            else:
                    print(f'TOP SELLING? -> (s)')
                    v_top_selling = "(s)"
                    set_top_selling.append(v_top_selling)

        except Exception as e:
            print(f'TOP SELLING -> (n)')
            v_top_selling = "(n)"
            set_top_selling.append(v_top_selling)

        sleep(velocimento)
        ######################################## TOP SELLING ########################################

        set_lista_contador.append(contador)
        contador += 1
        x = contador
        sleep(velocimento)

    contador += 1
    i += 1
    if len(botao.text) > 0:
        try:
            botao.click()
            sleep(5)
            click_button(navegador, "//div[@id='root']/div/div/div[2]", 30)
            sleep(1)
            div_mae = navegador.find_element(By.CLASS_NAME, "list--gallery--34TropR")
            sleep(1)
            print(f'#PAGINA -> {contador_page}')
            print(f'#QTDE LINHAS -> {len(set_produto)}')
            print(f'#PARSING DOCUMENT#')
            html_content = div_mae.get_attribute('outerHTML')
            sleep(1)
            print(f'#SOUP PARSER#')
            soup = BeautifulSoup(html_content, 'html.parser')
            print(f'#PARSE NEXT PAGE#')
            lista_produtos = soup.find_all('a', class_='manhattan--container--1lP57Ag cards--gallery--2o6yJVt')

        except Exception as e:
            print(f'Erro')

df = pd.DataFrame(data=(set_lista_contador), columns=["ID"])
df = df.set_index('ID')
df['NOME PRODUTO'] = set_produto
df['PRECO'] = set_preco_produto
df['QTDE VENDAS'] = set_qtde_vendas
df['TIPO FRETE'] = set_tipo_frete
df['DEVOLUCAO'] = set_tipo_devolucao
df['AVALIACOES'] = set_avaliacoes
df['LOJA'] = set_loja
df['LINK PRODUTO'] = set_link_produto
df['LINK LOJA'] = set_link_loja
df['PROMOCAO'] = set_promocao
df['TOP SELLING'] = set_top_selling
data_frame = df
print(df)

with pd.ExcelWriter(r"E:\Users\cleit\Documents\CURSO PYTHON\Aliexpress-selenium\teste.xlsx",
                    engine="xlsxwriter") as writer:
    data_frame.to_excel(writer)

navegador.quit()