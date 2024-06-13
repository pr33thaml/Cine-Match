Cine-Match
Cine-Match is a simple movie recommendation system implemented in Python, designed using object-oriented programming principles. This program enables users to manage movies by adding them with details like title, genre, and rating. It also provides functionalities to delete movies, search for movies by various criteria, and recommend top-rated movies.

Features
Add Movie: Users can add new movies to the system by providing details such as title, genre, and rating.
Delete Movie: Movies can be removed from the system based on the specified title.
Search Movies: Users can search for movies using different criteria:
By Title: Find movies containing a specific keyword in their title.
By Genre: Filter movies by specifying a genre.
By Rating: Locate movies based on a specific rating.
Recommend Top Movies: The system recommends the top N movies based on their ratings.
Implementation Details
Data Storage: The movie data is stored internally using Python lists and dictionaries, making it efficient for insertion, deletion, and search operations.
Sorting Algorithm: Sorting algorithms are used to recommend top-rated movies efficiently. The system sorts movies based on their ratings in descending order to extract the top-rated ones.
Requirements
Python 3.x: Ensure Python 3.x is installed on your system.
No External Libraries: The project does not require any external libraries, leveraging Python's built-in functionalities for implementation.
