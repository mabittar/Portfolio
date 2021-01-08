import requests
from urllib.parse import urlencode
"""
[Observações]
    a intenção em deixar o algorítmo dividido em 3 etapas foi para serapar
    em 3 naturezas distintas: Input, Processamento e Output da API (Clean Architecture).
    Assim o rastreio de erros fica facilitado, como também a manutenção do aplicativo.
    Veja a representação gráfica em: 
    https://blog.cleancoder.com/uncle-bob/images/2012-08-13-the-clean-architecture/CleanArchitecture.jpg

"""


def search(term):
    url = build_url(term)
    data = get_api(url)
    text = abstract(data)
    return text


def get_api(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Response {response.status_code}')
    data = response.json()
    return data


def abstract(data):
    text = data['Abstract']
    if not text:
        raise ValueError('Nao encontrado.')
    return text


def build_url(term):
    url = 'https://api.duckduckgo.com/?'
    qs = {'q': term, 'format': 'json', 'pretty': '1'}
    url += urlencode(qs)
    return url


term = str(input("Entre o termo a ser pesquisado: "))
print(search(term))
