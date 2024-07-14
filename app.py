import streamlit as st
import pickle
import pandas as pd
import requests
def recommend(movie):
    movie_index = movieDB[movieDB["title"]== movie].index[0]
    mList = sorted(list(enumerate(similarity[movie_index])),reverse=True,key=lambda x: x[1])[1:11]
    recommended_movies = []
    recommended_movies_posters = []
    for i in mList:
        movie_id = i[0]
        recommended_movies.append(movieDB.iloc[i[0]]["title"])
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

def fetch_poster(movie_id):
    id = movieDB.iloc[movie_id]["movie_id"]
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=134c3e6a124a16a13f7f4a5fa0f3cf76&language=en-US".format(id))
    data = response.json()
    print(data)
    poster_path = data.get("poster_path")               
    return "https://image.tmdb.org/t/p/original"+poster_path
    


movieDB = pickle.load(open('movies.pkl', 'rb'))
movies_list = movieDB["title"].values

similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Movie Recommender System")

selectedMovieName = st.selectbox(
    "Select the Movie Title",
    movies_list)

if st.button("Recommend"):
    names, posters = recommend(selectedMovieName)
    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)

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
    with col6:
        st.text(names[5])
        st.image(posters[5])
    with col7:
        st.text(names[6])
        st.image(posters[6])
    with col8:
        st.text(names[7])
        st.image(posters[7])
    with col9:
        st.text(names[8])
        st.image(posters[8])
    with col10:
        st.text(names[9])
        st.image(posters[9])
   

