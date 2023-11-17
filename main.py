import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def extract_data(carro, pages):

    # Criar uma lista para armazenar os títulos
    title = []

    # Criar uma lista para armazenar os anos
    subjects = []

    # Criar uma lista para armazenar os preços
    price = []

    for i in range(1, pages + 1):

        # Construir a URL da página
        url = "https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-es?ps=1&q=" + carro + "&rs=70&o=" + str(i)

        # Adicionar um cabeçalho User-Agent para simular um navegador
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        # Fazer a solicitação com o cabeçalho User-Agent
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extrair os dados do HTML
            subject_matches = subject_pattern.findall(str(soup))
            price_matches = price_pattern.findall(str(soup))
            title_matches = title_pattern.findall(str(soup))

            # Adicionar os dados às listas
            title.extend(title_matches)
            subjects.extend(subject_matches)
            price.extend(price_matches)

            time.sleep(3)

    # Criar um dicionário com os dados
    data = {"ano": subjects, "title": title, "price": price}

    # Criar um DataFrame a partir do dicionário
    df = pd.DataFrame(data)

    return df

# Input dos dados

print('Bem vindo ao busca carro! \n Você coloca o nome do carro e o número de páginas e ele te retorna todos os anúncios do OLX com essa busca. \n ')
print('\n Só buscamos carros seminovos (após o ano de 2020) \n')

print('Ao final da busca você recebe um arquivo Excel com o nome do carro')

print('Digite o modelo do carro: (ex: corolla xei)')
carro = input()

# Chamar a função
df = extract_data(carro, 5)

# Imprimir o DataFrame
print(df)

# Nomeia o arquivo
filename = carro + ".xlsx"

# Exportar o DataFrame para um arquivo Excel
df.to_excel(filename, index=False)
