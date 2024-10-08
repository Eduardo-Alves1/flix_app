import requests
import streamlit
from login.service import logout


class MoviesRepository:

    def __init__(self):
        self.__base_url = 'http://127.0.0.1:8000/api/v1/'
        self.__movies_url = f'{self.__base_url}movies/'
        self.__headers = {
            'Authorization': f'Bearer {streamlit.session_state.token}'
        }

    def get_movies(self):
        response = requests.get(
            self.__movies_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados na API. Status Code: {response.status_code}')
    
    def create_movie(self, movie):
        response = requests.post(
            self.__movies_url,
            headers=self.__headers,
            data=movie,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao salvar dados na API. Status Code: {response.status_code}')
    
    def get_muvie_stats(self):
        response = requests.get(
            f'{self.__movies_url}statistic/',
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados na API. Status Code: {response.status_code}')