import streamlit as st
import plotly.express as px
from movies.service import MoviesService

def show_home():
    movie_service = MoviesService()
    movie_stats = movie_service.get_movie_stats()

    st.title('Estatísticas dos Filmes')

    if len(movie_stats['movies_by_genre']) > 0:
        st.subheader('Filmes por Gênero')
        fig = px.pie(
            movie_stats['movies_by_genre'],
            values='count',
            names='genre__name',
            title='Filmes po Gênero'
        )
        st.plotly_chart(fig)
    
    st.subheader('Total de Filmes Cadastrados')
    st.write(movie_stats['total_movies'])

    st.subheader('Total de Filmes por Gêneros')
    for genre in movie_stats['movies_by_genre']:
        st.write(f'{genre["genre__name"]} - {genre["count"]}')

    st.subheader('Total de Avaliações')
    st.write(movie_stats['total_reviews'])

    st.subheader('Média Geral de Estrelas nas Avaliações')
    st.write(movie_stats['avg_stars'])