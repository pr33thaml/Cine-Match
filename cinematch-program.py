class MovieRecommendationSystem:
    def __init__(self):
        """
        Initializes an instance of the MovieRecommendationSystem class.
        """
        self.movies = []

    def add_movie(self, title, genre, rating):
        """
        Adds a movie to the recommendation system.

        Parameters:
        title (str): The title of the movie.
        genre (str): The genre of the movie.
        rating (float): The rating of the movie.
        """
        self.movies.append({'title': title, 'genre': genre, 'rating': rating})
        print(f"Added: {title}")

    def delete_movie(self, title):
        """
        Deletes a movie from the recommendation system.

        Parameters:
        title (str): The title of the movie to be deleted.
        """
        updated_movies = []
        for movie in self.movies:
            if movie['title'].lower() != title.lower():
                updated_movies.append(movie)
        self.movies = updated_movies
        print(f"Deleted: {title}")

    def search_movie(self, key, value):
        """
        Searches for movies in the recommendation system based on a given key and value.

        Parameters:
        key (str): The attribute of the movie to search for (e.g., 'title', 'genre', 'rating').
        value (str): The value to search for within the specified key.

        Returns:
        list: A list of movies that match the search criteria.
        """
        results = []
        for movie in self.movies:
            if value.lower() in str(movie[key]).lower():
                results.append(movie)
        return results

    def recommend_top_movies(self, n):
        """
        Recommends the top N movies based on their ratings.

        Parameters:
        n (int): The number of top movies to recommend.

        Returns:
        list: A list of the top N recommended movies.
        """
        sorted_movies = sorted(self.movies, key=lambda x: x['rating'], reverse=True)
        return sorted_movies[:n]

def main():
    """
    Main function to run the Movie Recommendation System.
    """
    cine_match = MovieRecommendationSystem()

    while True:
        print("\n1. Add movie\n2. Delete movie\n3. Search by title\n4. Search by genre\n5. Search by rating\n6. Recommend top movies\n7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Title: ")
            genre = input("Genre: ")
            rating = float(input("Rating: "))
            cine_match.add_movie(title, genre, rating)

        elif choice == '2':
            title = input("Title to delete: ")
            cine_match.delete_movie(title)

        elif choice == '3':
            value = input("Search title: ")
            results = cine_match.search_movie('title', value)
            for movie in results:
                print(f"{movie['title']} - {movie['genre']} - {movie['rating']}")

        elif choice == '4':
            value = input("Search genre: ")
            results = cine_match.search_movie('genre', value)
            for movie in results:
                print(f"{movie['title']} - {movie['genre']} - {movie['rating']}")

        elif choice == '5':
            value = input("Search rating: ")
            results = cine_match.search_movie('rating', value)
            for movie in results:
                print(f"{movie['title']} - {movie['genre']} - {movie['rating']}")

        elif choice == '6':
            n = int(input("Number of movies: "))
            results = cine_match.recommend_top_movies(n)
            for movie in results:
                print(f"{movie['title']} - {movie['genre']} - {movie['rating']}")

        elif choice == '7':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
