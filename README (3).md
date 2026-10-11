# 🎬 Movie Recommendation System

A content-based movie recommendation system built with **Python, Pandas, scikit-learn, and Streamlit**. Choose a movie and discover similar titles based on their metadata.

## Project Overview

Finding a movie to watch can be difficult when there are thousands of choices. This project recommends movies with similar metadata to a selected title. It uses movie information such as overview, genres, keywords, cast, and director to build text-based representations and compare movies.

## Features

- Select a movie from a dropdown menu.
- Get up to five similar movie recommendations.
- Optionally view cosine similarity scores.
- Interactive web interface built with Streamlit.
- Precomputed recommendations for quicker retrieval.

## Tech Stack

- **Python** — core programming
- **Pandas and NumPy** — data processing
- **scikit-learn** — text vectorization and cosine similarity
- **NLTK** — text preprocessing/stemming in the notebook
- **Streamlit** — web app
- **GitHub** — source control and project hosting

## Dataset

The project notebook uses the **TMDB 5000 Movies** and **TMDB 5000 Credits** datasets. The workflow combines movie metadata such as:

- Overview
- Genres
- Keywords
- Cast
- Director

Please follow the dataset provider's terms and attribution requirements when redistributing data. Avoid uploading the original CSV files unless you have confirmed redistribution is permitted and they are required for the app.

## How It Works

1. **Load and combine data:** Read the movie and credits datasets and merge them.
2. **Prepare metadata:** Parse genres, keywords, cast, and director information.
3. **Create tags:** Combine selected text fields into one movie profile.
4. **Vectorize text:** Use `CountVectorizer` to convert text into numerical feature vectors.
5. **Calculate similarity:** Use cosine similarity to compare movie vectors.
6. **Recommend movies:** Return the most similar titles while excluding the selected movie.
7. **Serve recommendations:** Streamlit displays the results in a simple web interface.

Cosine similarity is a measure of similarity between feature vectors. It is **not** a probability that a viewer will like a movie.

## Repository Structure

```text
Movie-Recommendation-System/
├── app.py
├── movies.pkl
├── recommendations.pkl
├── requirements.txt
└── README.md
```

- `app.py` — Streamlit interface and recommendation display.
- `movies.pkl` — prepared movie dataframe.
- `recommendations.pkl` — precomputed recommendations.
- `requirements.txt` — Python packages needed to run the app.
- `README.md` — project documentation.

The two pickle files must be generated from the same notebook run and must use the same movie row order. Only load pickle files from sources you trust.

## Run Locally

### 1. Clone the repository

Replace `YOUR_GITHUB_USERNAME` with your GitHub username:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

Ensure `movies.pkl` and `recommendations.pkl` are in the same folder as `app.py`.

### 3. Start the application

```bash
streamlit run app.py
```

Streamlit will print a local URL, usually `http://localhost:8501`.

## Deploy on Streamlit Community Cloud

1. Push `app.py`, `movies.pkl`, `recommendations.pkl`, and `requirements.txt` to your GitHub repository.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Sign in with GitHub and choose **Create app**.
4. Select this repository, the `main` branch, and `app.py` as the main file.
5. Deploy and test the generated app URL.

## Limitations

- Recommendations depend on the available movie metadata.
- The system does not use personal viewing history or user ratings.
- Similar metadata does not guarantee that a user will enjoy a recommendation.
- Duplicate movie titles can make selection ambiguous.
- The current approach uses text features and may not capture deeper semantic meaning.

## Future Improvements

- Display movie posters and release details using a permitted movie metadata API.
- Add filters for genre and release year.
- Use unique movie IDs to distinguish films with duplicate titles.
- Compare CountVectorizer with TF-IDF or semantic embeddings.
- Add tests and evaluate recommendation quality.
- Improve the interface for mobile screens.

## Resume Description

Use these bullets only for features you have actually implemented and tested:

**Movie Recommendation System | Python, Pandas, scikit-learn, NLP, Streamlit**

- Built a content-based movie recommendation pipeline using TMDB metadata, text vectorization, and cosine similarity.
- Combined movie overviews, genres, keywords, cast, and director information to represent movie content.
- Developed a Streamlit interface to let users select a movie and view similar titles.
- Precomputed top recommendations to reduce computation during user interactions.

## Author

**Your Name**  
GitHub: `https://github.com/YOUR_GITHUB_USERNAME`

## Acknowledgements

- TMDB 5000 Movies and Credits dataset providers.
- The Python, scikit-learn, Pandas, and Streamlit open-source communities.
