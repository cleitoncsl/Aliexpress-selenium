import pandas as pd
import os
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from collections import Counter

# url = "https://pt.aliexpress.com/w/wholesale-xiaomi-mi-pad-5.html?catId=0&initiative_id=SB_20221224181351&SearchText=xiaomi%2Bmi%2Bpad%2B5&spm=a2g0o.home.1000002.0&dida=y"
url = "https://pt.aliexpress.com/"

sleep(1) # Time in seconds

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
        navegador.execute_script("window.scrollTo(0,5500,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,6000,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,6500,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,7000,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,7500,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,8000,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,8500,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,9000,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,9500,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,10000,document.body.scrollHeight)")
        sleep(1)
        navegador.execute_script("window.scrollTo(0,0, document.body.scrollHeight)")

        print(f'-> Cache da página executado')

    except NoSuchElementException:
        print(f'-> ###Campo não encontrado###')
        navegador.quit()


if __name__ == "__main__":
    delay = 10
    site = "https://pt.aliexpress.com"

    #------------CHROME------------#
    option = Options()
    option.add_argument("--incognito")
    option.headless = False
    navegador = webdriver.Chrome(options=option)
    # ------------CHROME------------#

    #option = webdriver.EdgeOptions()
    # option.add_argument("start-minimized")
    # option.add_argument("inprivate")
    # option.add_argument("headless")
    # option.headless = False
    # navegador = webdriver.Edge(options=option)

    navegador.get(url)
    sleep(5)
    ######################################## ACEITAR OS COOKIES ########################################
    # cookie_accept = navegador.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[3]/div[2]")
    cookie_accept = WebDriverWait(navegador, delay).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div[3]/div[2]"))).click()
    # sleep(1)
    ######################################## ACEITAR OS COOKIES ########################################

    ######################################## CAMPO PESQUISA ########################################
    # campo_pesquisa = navegador.find_element(By.ID, "search-key")
    campo_pesquisa = WebDriverWait(navegador, delay).until(ec.element_to_be_clickable((By.ID, "search-key")))
    produto = "XIAOMI MI PAD"
    #produto = input("Digite o produto desejado: ")
    campo_pesquisa.send_keys(produto)
    botao_lupa = WebDriverWait(navegador, delay).until(ec.element_to_be_clickable((By.CLASS_NAME, "search-button")))
    botao_lupa.click()
    sleep(10)
    print(f'PRODUTO: {produto.upper()}')

    ######################################## CAMPO PESQUISA ########################################

    click_button(navegador, "//div[@id='root']/div/div/div[2]", 30)


# div_mae = navegador.find_element(By.XPATH, "/html[1]/body[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]")
div_mae = div_mae = WebDriverWait(navegador, delay).until(ec.element_to_be_clickable((By.CLASS_NAME, "list--gallery--34TropR")))
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
lista_produtos = soup.find_all('a', class_='manhattan--container--1lP57Ag cards--gallery--2o6yJVt')

sleep(1)

velocimento = 0
contador = 0
contador_page = 2
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
botao = navegador.find_element(By.CSS_SELECTOR,"#root > div.root--container--2gVZ5S0 > div > div.right--container--1WU9aL4.right--hasPadding--52H__oG > div > div.content--container--2dDeH1y > div.pagination--paginationList--2qhuJId > div.pagination--left--3ZLy8Mu > ul > li:nth-child(" + str(contador_page) + ")")

while len(botao.text) > 0:
    for produto in lista_produtos:
        sleep(0.1)
        print(f'----------------------------------------ID-{contador}----------------------------------------------------------------------')
        ######################################## NOME PRODUTO ########################################
        #
        nome_produto = produto.select('h1', class_="manhattan--titleText--WccSjUS")
        sleep(velocimento)
        print(f'Nome -> {nome_produto[0].getText()}')
        vNome_produto = nome_produto[0].text
        set_produto.append(vNome_produto)
        #
        ######################################## NOME PRODUTO ################################################################################ PRODUTO ########################################

        ######################################## PRECO PRODUTO ########################################
        preco_produto = produto.find('div', class_="manhattan--price-sale--1CCSZfK").select('a span')
        tam_preco = len(preco_produto)
        sleep(velocimento)
        try:
            if tam_preco == 6:
                print(f'Preço -> {preco_produto[0].getText() + preco_produto[1].getText() + preco_produto[2].getText() + preco_produto[3].getText() + preco_produto[4].getText() + preco_produto[5].getText()}')
                vPreco_produto = {preco_produto[0].getText() + preco_produto[1].getText() + preco_produto[2].getText() + preco_produto[3].getText() + preco_produto[4].getText() + preco_produto[5].getText()}
                set_preco_produto.append(vPreco_produto)

            elif tam_preco == 5:
                print(f'Preço -> {preco_produto[0].getText() + preco_produto[1].getText() + preco_produto[2].getText() + preco_produto[3].getText() + preco_produto[4].getText()}')
                vPreco_produto = {preco_produto[0].getText() + preco_produto[1].getText() + preco_produto[2].getText() + preco_produto[3].getText() + preco_produto[4].getText()}
                set_preco_produto.append(vPreco_produto)



            elif tam_preco == 4:
                print(f'Preço -> {preco_produto[0].getText() + preco_produto[1].getText() + preco_produto[2].getText() + preco_produto[3].getText()}')
                vPreco_produto = {preco_produto[0].getText() + preco_produto[1].getText() + preco_produto[2].getText() + preco_produto[3].getText()}
                set_preco_produto.append(vPreco_produto)

            elif tam_preco == 3:
                print(f'Preço -> {preco_produto[0].getText() + preco_produto[1].getText() + preco_produto[2].getText() }')
                vPreco_produto = {preco_produto[0].getText() + preco_produto[1].getText() + preco_produto[2].getText() }
                set_preco_produto.append(vPreco_produto)

            elif tam_preco == 2:
                print(f'Preço -> {preco_produto[0].getText() + preco_produto[1].getText() }')
                vPreco_produto = {preco_produto[0].getText() + preco_produto[1].getText() }
                set_preco_produto.append(vPreco_produto)

            elif tam_preco == 1:
                print(f'Preço -> {preco_produto[0].getText()}')
                vPreco_produto = {preco_produto[0].getText()}
                set_preco_produto.append(vPreco_produto)

        except Exception as e:
            print(f'Preço -> 0')
            vPreco_produto = 0
        # set_preco_produto.append(vPreco_produto) <-deletar
        ######################################## PRECO PRODUTO ########################################

        ######################################## QTDE PRODUTO ########################################
        qtde_vendas = produto.select("span.manhattan--trade--2PeJIEB")
        sleep(velocimento)
        try:
            if qtde_vendas is None or len(qtde_vendas) == 0:
                print('qtde_vendas -> 0')
                vQtde_Vendas = 0

            else:
                print(f'qtde_vendas -> {qtde_vendas[0].getText()}')
                vQtde_Vendas = qtde_vendas[0].getText()

        except Exception as e:
            print(f'qtde_vendas -> -')
        set_qtde_vendas.append(vQtde_Vendas)
        ######################################## QTDE PRODUTO ########################################


        ######################################## TIPO FRETE ########################################
        tipo_frete = produto.select("span.tag--textStyle--vcAi3Rh")
        sleep(velocimento)
        try:

            tam_campo_frete = len(tipo_frete)
            if tam_campo_frete == 2:
                print(f'Preço -> {tipo_frete[1].getText()}')
                vTipo_Frete = {tipo_frete[1].getText()}
                set_tipo_frete.append(vTipo_Frete)

            elif tam_campo_frete == 1:
                print(f'Preço -> {tipo_frete[0].getText()}')
                vTipo_Frete = {tipo_frete[0].getText()}
                set_tipo_frete.append(vTipo_Frete)

            else:
                print('fPreco -> 0')
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
                print('Frete -> -')
                vTipo_Devolucao = tipo_devolucao[0].getText()

            else:
                print(f'Devolução -> {tipo_devolucao[1].getText()}')
                vTipo_Devolucao = tipo_devolucao[0].getText()

        except Exception as e:
            print(f'Devolução -> -')
            vTipo_Devolucao = "-"
        set_tipo_devolucao.append(vTipo_Devolucao)

        ######################################## TIPO DEVOLUCAO ########################################

        ######################################## AVALICAOES ########################################
        avaliacoes = produto.select("span.manhattan--evaluation--3cSMntr")
        sleep(velocimento)
        try:
            if avaliacoes is None: #avaliacoes
                print('Avaliações -> -')
                vAvaliacoes = "-"
            else:
                print(f'Avaliações -> {avaliacoes[0].getText()}')
                vAvaliacoes = avaliacoes[0].getText()

        except Exception as e:
            print(f'Avaliações -> -')
            vAvaliacoes = "-"

        set_avaliacoes.append(vAvaliacoes)
        ######################################## AVALICAOES ########################################

        ######################################## LOJA ########################################
        loja = produto.select("a.cards--storeLink--1_xx4cD")
        sleep(velocimento)
        try:
            if loja is None:
                print('Loja -> -')
                vLoja = "-"

            else:
                print(f'Loja -> {loja[0].getText()}')
                vLoja = loja[0].getText()

        except Exception as e:
            print(f'Loja -> -')
            vLoja = "-"

        set_loja.append(vLoja)
        ######################################## LOJA ########################################

        ######################################## LINK PRODUTO ########################################
        link_produto = [a['href'] for a in soup.find_all('a', href=True) if a.text]
        if contador == 0:
            x = contador
        elif (contador % 2) == 0:
            contador
        else:
            x = contador + 1

        link_produto_final = link_produto[x]
        try:
            if link_produto_final is None:
                print('Loja -> -')
                vLinkProdutoFinal = "-"

            else:
                print(f'Link Produto -> {"https:" + link_produto_final}')
                vLinkProdutoFinal = "https:" + link_produto_final

        except Exception as e:
            print(f'Link Produto -> -')
            vLinkProdutoFinal = "-"

        set_link_produto.append(vLinkProdutoFinal)
        sleep(velocimento)
        ######################################## LINK PRODUTO ########################################

        ######################################## LINK LOJA ########################################
        link_loja = link_produto[x + 1]
        try:
            if link_loja is None:
                print(f'Link Loja -> -')
            else:
                print(f'Link Loja - >{"https:" + link_loja}')
                vLinkLojaFinal = "https:" + link_loja


        except Exception as e:
            print('Link Loja -> -')
            vLinkLojaFinal = 0

        set_link_loja.append(vLinkLojaFinal)
        sleep(velocimento)
        ######################################## LINK LOJA ########################################

        ######################################## PROMOCAO ########################################
        promocao = produto.select("span.tag--textStyle--vcAi3Rh")

        try:
            len_promocao = len(promocao)
            if len_promocao == 2:
                print(f'Promoção -> {promocao[0].getText()}')
                vTipo_Frete = {promocao[0].getText()}
                set_promocao.append(vTipo_Frete)

            else:
                print(f'Promoção -> (n)')
                set_promocao.append("(n)")

        except Exception as e:
            print(f'Promoção -> -')
            vPromocao = "(n)"

        ######################################## PROMOCAO ########################################

        ######################################## TOP SELLING ########################################
        top_selling = produto.find_all('img', class_='tag--imgStyle--1hJHaAY')
        sleep(velocimento)
        try:
            top_selling = len(top_selling[0].get('src'))
            if top_selling is None:
                print('top_selling? -> (n)')
                v_top_selling = "(n)"

            else:
                    print(f'top_selling? -> (s)')
                    v_top_selling = "(s)"

        except Exception as e:
            print(f'top_selling -> (n)')
            v_top_selling = "(n)"


        set_top_selling.append(v_top_selling)
        sleep(velocimento)
        ######################################## TOP SELLING ########################################

        contador += 1
        x = contador
        lista = list(zip(
            set_produto, set_preco_produto, set_qtde_vendas, set_tipo_frete, set_tipo_devolucao,
            set_avaliacoes, set_loja, set_link_produto, set_link_loja, set_promocao, set_top_selling)) ##resultado
        data_frame = pd.DataFrame(lista,
            columns=['Nome.Produto', 'Prc.Produto', 'Qtd.Vendas', 'Tipo.Frete', 'Tipo.Devolucao', 'Avaliacaoes',
                     'Nome Loja', 'Link.Produto', 'Link.Loja', 'Promocao', 'Top.Selling'])


        with pd.ExcelWriter(r"E:\Users\cleit\Documents\CURSO PYTHON\Aliexpress-selenium\teste.xlsx", engine="xlsxwriter") as writer:
            data_frame.to_excel(writer)



    contador_page += 1
    contador = 1
    if len(botao.text) > 0:
        try:
            botao = navegador.find_element(By.CSS_SELECTOR,"#root > div.root--container--2gVZ5S0 > div > div.right--container--1WU9aL4.right--hasPadding--52H__oG > div > div.content--container--2dDeH1y > div.pagination--paginationList--2qhuJId > div.pagination--left--3ZLy8Mu > ul > li:nth-child(" + str(contador_page) + ")")
            botao.click()
            sleep(10)
            click_button(navegador, "//div[@id='root']/div/div/div[2]", 30)
            sleep(1)
            div_mae = navegador.find_element(By.CLASS_NAME, "list--gallery--34TropR")
            sleep(1)
            print(f'#PARSING DOCUMENT#')
            html_content = div_mae.get_attribute('outerHTML')
            sleep(1)
            print(f'#SOUP PARSER#')
            soup = BeautifulSoup(html_content, 'html.parser')
            print(f'#PARSE NEXT PAGE#')
            lista_produtos = soup.find_all('a', class_='manhattan--container--1lP57Ag cards--gallery--2o6yJVt')



        except Exception as e:
            print(f'Erro')


navegador.quit()