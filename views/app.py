import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load the movie data and similarity matrix
df = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = df['title'].values

st.header("Movie Recommender System")

# Dropdown for the movie titles
selected_movie = st.selectbox("Select a movie:", movies_list)

import streamlit.components.v1 as components

def recommend(movie):
    # Check if the movie exists in the dataset
    if movie in df['title'].values:
        index = df[df['title'] == movie].index[0]
        
        # Assuming you already have a similarity matrix (similarity is already loaded)
        # Sort the movies based on similarity scores
        distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
        
        # Get the top 5 most similar movies
        recommended_movies = []
        for i in distance[1:6]:  # Skip the first movie as it will be the same as the selected one
            recommended_movies.append(df.iloc[i[0]]['title'])  # Assuming 'title' column exists in `df`
        
        return recommended_movies
    else:
        return []  # Return an empty list if the movie doesn't exist

if st.button("Recommend"):
    movie_names = recommend(selected_movie)
    
    if movie_names:  # Ensure that recommendations are not empty
        col1, col2, col3, col4, col5 = st.columns(5, gap="medium")
        with col1:
            st.write(movie_names[0])

        with col2:
            st.write(movie_names[1])

        with col3:
            st.write(movie_names[2])

        with col4:
            st.write(movie_names[3])

        with col5:
            st.write(movie_names[4])
    else:
        st.write("No recommendations available.")
