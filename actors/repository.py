import requests
import streamlit as st
from login.service import logout

class ActorsRepository:

    def __init__(self):
        self.__base_url = 'http://127.0.0.1:8000/api/v1/'
        self.__actors_url = f'{self.__base_url}actors/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_actors(self):
        response = requests.get(
            self.__actors_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados na API. Status Code: {response.status_code}')
    
    def create_actor(self, actor):
        response = requests.post(
            self.__actors_url,
            headers=self.__headers,
            data=actor,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao salvar dados na API. Status Code: {response.status_code}')