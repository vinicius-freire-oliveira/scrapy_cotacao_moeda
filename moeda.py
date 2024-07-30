import requests
from bs4 import BeautifulSoup
import pandas as pd

def extrair_cotacao_moeda(url):
    # Realiza a requisição para obter o conteúdo da página
    response = requests.get(url)
    site = BeautifulSoup(response.text, 'html.parser')

    # Encontrar a cotação
    cotacao_div = site.find('span', class_='ccOutputTrail')
    cotacao_texto = cotacao_div.previous_sibling.text.strip() if cotacao_div else 'Não disponível'

    return cotacao_texto

# Perguntar ao usuário quais moedas ele deseja consultar
moeda_base = input('Qual moeda você deseja converter? (ex: USD) ').upper()
moeda_destino = input('Para qual moeda você deseja converter? (ex: EUR) ').upper()

# URL da página de resultados
url_base = f'https://www.x-rates.com/calculator/?from={moeda_base}&to={moeda_destino}&amount=1'
print(f'URL da página de resultados: {url_base}')

# Extrair a cotação
cotacao = extrair_cotacao_moeda(url_base)

# Exibir a cotação
print(f'A cotação de {moeda_base} para {moeda_destino} é: {cotacao}')

# Salvar os dados em um arquivo CSV
dados = pd.DataFrame({'Moeda Base': [moeda_base], 'Moeda Destino': [moeda_destino], 'Cotação': [cotacao]})
csv_filename = f'{moeda_base}_para_{moeda_destino}_cotacao.csv'
dados.to_csv(csv_filename, index=False, encoding='utf-8')

# Confirmar que o arquivo foi salvo
print(f'Os dados foram salvos em {csv_filename}')
