import streamlit as st
import pickle
import pandas as pd
import requests

# Add a background image using CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1524985069026-dd778a71c7b4");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    .block-container {
        background-color: rgba(0, 0, 0, 0.6); /* Optional: Dark overlay for readability */
        padding: 2rem;
        border-radius: 1rem;
    }

    h1, .stSelectbox label,.stText{
        color: white !important;
    }
    .stButton button{
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to fetch movie poster using the movie ID
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={st.secrets['TMDB_API_KEY']}&language=en-US"
        data = requests.get(url).json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750?text=Error+Loading"

# Function to recommend movies based on the selected movie
def recommend(movie):
    matching_movies = movies[movies['title'] == movie]
    if matching_movies.empty:
        st.error("Selected movie not found in the dataset.")
        return [], []

    movie_index = matching_movies.index[0]

    if movie_index >= len(similarity):
        st.error("Selected movie index is out of range in the similarity matrix.")
        return [], []

    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie_names = []
    recommended_movies_posters = []

    for i in movies_list:
        index = i[0]
        if index < len(movies):
            movie_id = movies.iloc[index].movie_id
            recommended_movie_names.append(movies.iloc[index].title)
            recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movies_posters

# Streamlit App Title
st.title('🎬 Movie Recommender System')

# Load movie data and similarity matrix
try:
    movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
except Exception as e:
    st.error(f"Failed to load data files: {e}")
    st.stop()

# Dropdown to select a movie
selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

# Show recommendations on button click
if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie_name)
    if names and posters:
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.text(names[i])
                st.image(posters[i])
