import requests


class Auth:

    def __init__(self):
        self.__base_url = 'http://127.0.0.1:8000/api/v1/'
        self.__auth_url = f'{self.__base_url}authentication/token/'

    def get_token(self, username, password):
        auth_payload = {
            'username': username,
            'password': password
        }
        auth_response = requests.post(
            self.__auth_url,
            data=auth_payload
        )
        if auth_response.status_code == 200:
            return auth_response.json()
        return {'error': f'Erro ao autentcar. Status Code: {auth_response.status_code}'}
    

# Este código define uma classe chamada Auth com métodos para lidar com a autenticação. A classe tem um método de inicialização (__init__) que define a URL base e a URL de autenticação para a API.

# O método get_token recebe um username e password como entrada, cria um payload de autenticação, envia uma solicitação POST para a URL de autenticação e processa a resposta. Se o código de status da resposta for 200 (indicando uma solicitação bem-sucedida), ele retorna a resposta JSON. Caso contrário, ele retorna uma mensagem de erro com o código de status.

# Esta classe pode ser usada para autenticar usuários e recuperar seus tokens de autenticação para solicitações subsequentes à API.