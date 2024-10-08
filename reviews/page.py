import streamlit as st
from st_aggrid import AgGrid
from movies.service import MoviesService
from reviews.service import ReviewService
import pandas as pd

def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    if reviews:
        st.write('Reviews dos Filmes')
        reviews_df = pd.json_normalize(reviews)
        AgGrid(
            data=reviews_df,
            reload_data=True,
            key='reviews'
        )
    else:
        st.warning('Nenhuma Avaliação encontrada.')

    st.title('Cadastrar Nova Avsliação')

    movie_service = MoviesService()
    movies = movie_service.get_movies()
    movie_title = {movie['title']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Filme', list(movie_title.keys()))


    stars = st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1,
    )

    coment = st.text_area(
        label='Comentário',
        max_chars=200,
    )

    if st.button('Cadastrar'):
        new_review = review_service.create_review(
            movie=movie_title[selected_movie_title],
            stars=stars,
            comment=coment,
        )
        if new_review:
            st.rerun()
        else:
            st.error('Erro ao cadastrar avaliação. Verifique os campos.')

