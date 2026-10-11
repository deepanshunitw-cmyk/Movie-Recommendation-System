
import pickle
import streamlit as st

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

@st.cache_resource
def load_data():
    with open("movies.pkl", "rb") as f:
        movies = pickle.load(f)

    with open("recommendations.pkl", "rb") as f:
        recommendations = pickle.load(f)

    return movies, recommendations


st.title("🎬 Movie Recommendation System")
st.write(
    "Select a movie and discover five similar movies "
    "using content-based filtering."
)

try:
    movies, recommendations = load_data()

    selected_movie = st.selectbox(
        "Choose your favorite movie",
        movies["title"].tolist()
    )

    if st.button("Recommend Movies", type="primary"):
        movie_index = movies.index[
            movies["title"] == selected_movie
        ][0]

        st.subheader(f"Movies similar to {selected_movie}")

        results = recommendations.get(movie_index, [])

        if not results:
            st.info("No recommendations available.")
        else:
            columns = st.columns(len(results))

            for column, (idx, score) in zip(columns, results):
                with column:
                    st.markdown(f"**{movies.iloc[idx]['title']}**")
                    st.caption(
                        f"Similarity: {score:.2f}"
                    )

except FileNotFoundError as e:
    st.error(
        f"Required file not found: {e.filename}. "
        "Please check your deployment files."
    )
