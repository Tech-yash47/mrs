import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=75a88a6807a3ff2326bcef85a31bde3c"
    )
    data = response.json()
    poster_path = data.get('poster_path')
    if not poster_path:
        return "https://via.placeholder.com/500x750?text=No+Poster"
    return "https://image.tmdb.org/t/p/original" + poster_path

def recommend(movie):
    movie_index = new_df[new_df["title"] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[movie_index])),key= lambda x:x[1],reverse=True)[1:6]
    recommended_movie = []
    recommended_movie_poster = []
    for i in movie_list:
        recommended_movie.append(new_df.iloc[i[0]]['title'])
        recommended_movie_poster.append(fetch_poster(i[0]))
    return recommended_movie,recommended_movie_poster

movies_dict = pickle.load(open('movie_dic.pkl', 'rb'))
new_df = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Movie name', new_df['title'])

if st.button('Recommendation') == True:
    st.write(recommend(selected_movie_name))
    movies,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(movies[0])
        st.image(posters[0])
    with col2:
        st.header(movies[1])
        st.image(posters[1])
    with col3:
        st.header(movies[2])
        st.image(posters[2])
    with col4:
        st.header(movies[3])
        st.image(posters[3])
    with col5:
        st.header(movies[4])
        st.image(posters[4])

