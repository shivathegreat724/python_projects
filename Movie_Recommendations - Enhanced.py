import time
import pandas as pd

from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

movies = pd.read_csv("imdb_top_1000.csv")

print(Fore.LIGHTGREEN_EX + "🎬 Welcome to the AI Movie Recommendation!🎬")
name = input(Fore.LIGHTBLUE_EX+ "\n🦈What's your name?").strip()
print(Fore.LIGHTYELLOW_EX + f"\n🐙Great to meet you, {name}!")

unique_genres = set()

for genres in movies["Genre"].dropna():
    for genre in genres.split(","):
        unique_genres.add(genre.strip())

unique_genres = sorted(unique_genres)

print(Fore.CYAN + "\n🦖Available Genres:")
for i, genre in enumerate(unique_genres, 1):
    print(Fore.LIGHTCYAN_EX + f"{i}. {genre}")


choice = input(Fore.LIGHTRED_EX + "\n🐉Enter genre number or name: ").strip()

if choice.isdigit():
    number = int(choice)
    selected_genre = unique_genres[number - 1]
else:
    selected_genre = choice

print(selected_genre)

mood = input(Fore.LIGHTYELLOW_EX + "\n⛈️What kind of mood are you looking for?\n> ")

mood_blob = TextBlob(mood)
mood_polarity = mood_blob.sentiment.polarity

if mood_polarity > 0.1:
    mood_type = "Positive 🔥"
    print("Positive 🔥")

elif mood_polarity < -0.1:
    mood_type = "Negative 🥀"
    print("Negative 🥀")
else:
    mood_type = "Neutral ⚖️"
    print("Neutral ⚖️")


min_rating = float(input("\n🌚Enter minimum rating (0-10): "))
max_rating = float(input("🚀Enter maximum rating (0-10): "))


filtered_movies = movies[
    movies["Genre"].str.contains(selected_genre, case=False, na=False) &
    (movies["IMDB_Rating"] >= min_rating) &
    (movies["IMDB_Rating"] <= max_rating)
].copy()


def get_movie_polarity(description):
    if pd.isna(description):
        return 0
    return TextBlob(str(description)).sentiment.polarity


filtered_movies["polarity"] = (
    filtered_movies["Overview"]
    .apply(get_movie_polarity)
)

filtered_movies["mood_difference"] = abs(
    filtered_movies["polarity"] - mood_polarity
)

recommendations = filtered_movies.sort_values(by="mood_difference")


for i, (_, movie) in enumerate(recommendations.head(5).iterrows(), 1):
    print(f"{i}.{movie['Series_Title']}",
        Fore.LIGHTMAGENTA_EX + f"(🌋Rating: {movie['IMDB_Rating']:.1f}/10)"
    )




