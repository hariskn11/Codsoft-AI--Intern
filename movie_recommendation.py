import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Expanded movie data
movies = pd.DataFrame({
    'title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump',
              'The Lord of the Rings: The Fellowship of the Ring', 'Inception', 'The Matrix', "Schindler's List",
              'The Silence of the Lambs', 'The Lion King', 'Jurassic Park', 'Titanic', 'Avatar', 'Gladiator',
              'The Avengers', 'The Social Network', 'The Departed', 'Interstellar', 'The Green Mile',
              'The Terminator', 'The Wizard of Oz', 'Gone with the Wind', 'Braveheart', 'Fight Club',
              'Saving Private Ryan', 'The Godfather Part II', 'The Lord of the Rings: The Return of the King',
              'The Empire Strikes Back', 'Back to the Future', 'Toy Story'],
    'genre': ['Drama', 'Crime', 'Action, Crime, Drama', 'Crime, Drama', 'Drama, Romance',
              'Action, Adventure, Drama', 'Action, Adventure, Sci-Fi', 'Action, Sci-Fi',
              'Biography, Drama, History', 'Crime, Drama, Thriller', 'Animation, Adventure, Drama',
              'Action, Adventure, Sci-Fi', 'Drama, Romance', 'Action, Adventure, Fantasy', 'Action, Drama',
              'Action, Sci-Fi', 'Biography, Drama', 'Crime, Drama, Thriller', 'Adventure, Drama, Sci-Fi',
              'Crime, Drama, Fantasy', 'Action, Sci-Fi', 'Adventure, Family, Fantasy', 'Drama, Romance, War',
              'Biography, Drama, History', 'Drama', 'Drama, War', 'Drama', 'Crime, Drama',
              'Adventure, Drama, Fantasy', 'Action, Adventure, Fantasy', 'Adventure, Comedy, Family']
})

# Preprocess genre data
movies['genre'] = movies['genre'].str.replace(',', ' ')

# Create TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genre'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend movies based on user preferences
def recommend_movies(title, cosine_sim=cosine_sim, movies=movies):
    # Get index of the movie title
    idx = movies.loc[movies['title'] == title].index[0]

    # Get similarity scores with all movies
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top 5 similar movies (excluding the queried movie itself)
    sim_scores = sim_scores[1:6]

    # Get movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return top 5 recommended movie titles
    recommended_movies = movies['title'].iloc[movie_indices].reset_index(drop=True)
    return recommended_movies

# Test the recommendation system
print("Top 5 Recommended Movies for 'The Dark Knight':")
for i, movie in enumerate(recommend_movies('The Dark Knight'), 1):
    print(f"{i}. {movie}")
