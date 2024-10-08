import requests
from login.service import logout
import streamlit as st

class GenreRepository:
    
    def __init__(self):
        self.__base_url = 'http://127.0.0.1:8000/api/v1/'
        self.__genres_url = f'{self.__base_url}genres/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }
    
    def get_genres(self):
        response = requests.get(
            self.__genres_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados na API. Status Code: {response.status_code}')
    
    def create_genre(self, genre):
        response = requests.post(
            self.__genres_url,
            headers=self.__headers,
            data=genre,
        )

        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados na API. Status Code: {response.status_code}')

    # def delete_genre(self, pk):
    #     response = requests.delete(
    #         f'{self.__genres_url}/{pk}/',
    #         headers=self.__headers
    #     )

    #     if response.status_code == 204:
    #         return True
    #     if requests.status_code == 401:
    #         logout()
    #         return False
    #     raise Exception(f'Erro ao excluir dados na API. Status Code: {response.status_code}')