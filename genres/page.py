import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from genres.service import GenreService


def show_genres():
    genres_service = GenreService()
    genres = genres_service.get_genres()


    if genres:
        st.write('Lista de Gêneros')
        genres_df = pd.json_normalize(genres)
        AgGrid(
            data=pd.DataFrame(genres),
            reload_data=True,
            key='genres'

        )
    else:
        st.warning('Nenhum Gênero econtrado.')

    st.title('Cadastrar novo gênero')
    name = st.text_input('Nome do Gẽnero')
    if st.button('Cadastrar'):
        new_genre = genres_service.create_genre(
            name=name,
        )
        if new_genre:
            st.rerun()
        else:
            st.error('Erro ao cadastrar gênero. Verifique os campos.')