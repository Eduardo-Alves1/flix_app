import streamlit as st
from genres.page import show_genres
from login.page import show_login
from home.page import show_home
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews


def main():
    if 'token' not in st.session_state:
        show_login()
    else:
        st.title('Edu Flix')
        st.divider()

        menu_options = st.sidebar.selectbox(
            'Selecione uma opção',
            ['inicio', 'Gênero', 'Atores/Atrizes', 'Filmes', 'Avaliações']
        )

        if menu_options == 'inicio':
            show_home()

        if menu_options == 'Gênero':
            show_genres()

        if menu_options == 'Atores/Atrizes':
            show_actors()
        
        if menu_options == 'Filmes':
            show_movies()

        if menu_options == 'Avaliações':
            show_reviews()


if __name__ == '__main__':
    main()


