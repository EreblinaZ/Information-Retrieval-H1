# Homework 1 - Information Retrieval
This code implements a simple GUI application in Python using Tkinter, which allows users to search for words in a text file (index.txt). Here's a brief explanation of the code:

## 1. Inverted Index Construction (build_inverted_index function):
- Reads the index.txt file line by line.
- Splits each line into words and converts them to lowercase.
- Constructs an inverted index where each word points to a list of line numbers where it appears.

## 2. Search Functionality (search_word function):
- Takes a word and looks it up in the inverted index.
- Returns the list of line numbers where the word appears or None if the word is not found.

## 3. Search Button Action (search function):
- Retrieves the word entered by the user.
- Searches the word using the inverted index.
- If the word is found:
- Writes the search results (line numbers and positions within lines) to search_result.txt.
- If the word is not found:
- Adds the word to index.txt.
- Displays a message indicating that the word does not exist in the file.

## 4. GUI Setup:
- Initializes the Tkinter root window and configures its size and position.
- Creates a frame containing a label, an entry box for user input, and a search button.
- When the search button is clicked, it calls the search function.

## 5.Window Closing Protocol (on_closing function):
- Asks for user confirmation before closing the application.

## 6.Main Execution:
- Builds the inverted index by calling build_inverted_index.
- Starts the Tkinter main loop to run the application.

The GUI allows users to enter a word, search for it in the text file, and view the results or update the file if the word is not found.
