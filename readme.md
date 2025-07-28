# 🎬 Movie Recommendation System

This project is a **Content-Based Movie Recommendation System** built using the **TMDB dataset**. It uses **TF-IDF vectorization** and **Cosine Similarity** to recommend similar movies based on user input.

## 📌 Features

- Content-based filtering using movie overviews, genres, and tags
- TF-IDF vectorization to extract important features
- Cosine similarity to find similar movies
- Data preprocessing to improve recommendation quality
- Simple and interactive user input system

## 🧰 Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn (TF-IDF, Cosine Similarity)
- TMDB Dataset (Kaggle)

## 📂 Project Structure

movie-recommendation/
├── data/
│ └── movies.csv
├── movie_recommender.py
├── requirements.txt
└── README.md

markdown
Copy
Edit

## 🚀 How It Works

1. Loads and preprocesses movie data.
2. Converts text data to numerical vectors using **TF-IDF**.
3. Calculates **Cosine Similarity** between movies.
4. Recommends top N similar movies for a given input movie title.

## 🧪 Example

Input: `Inception`  
Output:  
- Interstellar  
- The Prestige  
- The Matrix  
- Memento  
- Shutter Island
