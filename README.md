# SearchEngine

Utilises an index to optimise the look up process. Each word can simply be checked as the key of a dictionary instead of searching through lines of text after reading each file.

Please note this is only a basic implementation of search. Therefore it will NOT consider the following:
+ Excluding small words (such as 'a', 'of', 'the' etc.)
+ Matching work stems (if entering 'quickly' will not match 'quickness' or other words with this stem).
+ Will not match subtrings in the text files.

## How to Use

+ Open your local terminal window & navigate to directory containing the search.py script.
+ Enter:
    `python3 search.py <relative_file_path_to_searchable_directory>`

## Testing 

if you want to run the test suite for this file:
+ cd into the search_engine directory.
+ run `poetry shell`
+ run `poetry install`
+ run `pytest .`

## Dependencies

This project is lightweight and only uses poetry to manage its testing dependencies.
