import pickle
import streamlit as st

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movie_names = []
    for i in distances[1:6]:  # Get top 5 recommendations
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

st.header('Movie Recommender System Using Machine Learning')

# Load the movie list and similarity matrix
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    
    st.subheader("Recommended Movies:")
    for name in recommended_movie_names:
        st.write("- " + name)
