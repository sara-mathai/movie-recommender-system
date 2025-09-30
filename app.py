#8f4ca076663a859a20435989a958199


import streamlit as st
import pickle
import pandas as pd
import requests



def fetch_poster(movie_id):
    #8f4ca076663a859a20435989a9581990- from tmdb profile settings->api
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8f4ca076663a859a20435989a9581990&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names=[]
    recommended_movie_posters=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id

        recommended_movie_names.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movie_posters.append(fetch_poster(movie_id))


    return recommended_movie_names,recommended_movie_posters

movie_dict=pickle.load(open('movies_dict.pkl','rb'))

movies=pd.DataFrame(movie_dict)


similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)


if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
