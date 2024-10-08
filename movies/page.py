import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid
from movies.service import MoviesService
from actors.service import ActorService
from genres.service import GenreService


def show_movies():
    movies_service = MoviesService()
    movies = movies_service.get_movies()

    if movies:
        st.write('Lista de Filmes')
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        AgGrid(
            data=movies_df,
            reload_data=True,
            key='movies'
        )
    else:
        st.warning('Nenhum Filme encontrado.')
        
    st.title('Cadastrar novo filme')
    
    title = st.text_input(label='Titolo do Filme')
    release_date = st.date_input(
        label='Data de Lançamento', 
        value=datetime.today(),
        min_value=datetime(1900, 1, 1).date(),
        max_value=datetime.today(),
        format= 'DD/MM/YYYY',
    )

    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_tipy = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Generos', list(genre_tipy.keys()))
    
    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['name']: actor['id'] for actor in actors}
    selected_actors_name = st.multiselect('Atores/Atrizes', list(actor_names.keys()))
    selected_actors_ids = [actor_names[name] for name in  selected_actors_name]

    resume = st.text_area('Resume')
    
    if st.button('Cadastrar'):
        new_movies = movies_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genre_tipy[selected_genre_name],
            actors=selected_actors_ids,
            resume=resume,
        )
        if new_movies:
            st.rerun()
        else:
            st.error('Erro ao cadastrar filme. Verifique os campos.')