# Word Count

Coded by [samuelfarrus](https://github.com/samuelfarrus).

## Description

The folder contains two files. First, the 'wordCount.py', a interactive process coded in Python which, when called, will count the amount of appearances of each word in a text (.txt) file. Second, there is a text file to be used as an example, named 'sherlock.txt'. The file is actually a book, 'The Adventures of Sherlock Holmes' by Arthur Conan Doyle, and can be found in the [Project Gutenberg](https://www.gutenberg.org/ebooks/1661).

The program will generate a CSV file in the end, named 'word_count_result.csv', containing the relation of each word and its respective amount ou appearances. The repository already contains one file, giving the result of the analysis for the 'sherlock.txt' example file.

### Usage

The word count can be called via console terminal (or Git Bash) by typing `py wordCount.py`, replacing 'wordCount.py' by the file's path if necessary.

Once running, the program will simulate a terminal by itself, and will ask for two entries:

1. *The text file to be analysed*: type the name of the file to be analysed (to have its words counted). **Note**: it is not necessary to add the '.txt' extension, the program will automatically add if it is not provided.
2. *The sorting method*: once the analysis is complete, the program will ask for the *sorting method*. Suppose the following word list and their respective amount of appearances as an example: *avocado (5), genesis (2), bite (1), omega (4)*. The sorting methods are:
	* Order of appearance (default): leave the entry empty to sort by order of appearance = *avocado (5), genesis (2), bite (1), omega (4)*.
	* **wa** for Words (ascending) = *avocado (5), bite (1), genesis (2), omega (4)*.
	* **wd** for Words (descending) = *omega (4), genesis (2), bite (1), avocado (5)*.
	* **aa** for Amount (ascending) = *bite (1), genesis (2), omega (4), avocado (5)*.
	* **ad** for Amount (descending) = *avocado (5), omega (4), genesis (2), bite (1)*.