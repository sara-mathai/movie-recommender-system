Movie Recommendation System 🎬

A content-based movie recommendation system built with Python and deployed using Streamlit. It recommends movies based on metadata such as overview, genres, keywords, cast, and crew, and displays movie posters fetched from the TMDB API.

Features

Suggests top 5 similar movies for a selected movie.

Fetches movie posters dynamically using the TMDB API.

Preprocessing includes text normalization, stemming, and Bag-of-Words feature extraction.

Computes similarity using cosine similarity.

Optimized for performance with Pickle serialization of processed data and similarity matrix.

Technologies & Libraries

Python | Pandas | NumPy | NLTK | scikit-learn | Streamlit | Requests | Pickle

How It Works

Preprocess movie metadata: combine overview, genres, keywords, cast, and crew into a single tags column.

Convert text to numerical vectors using CountVectorizer.

Compute cosine similarity between movie vectors.

Build a Streamlit web app where users can select a movie and see top recommendations with posters.
