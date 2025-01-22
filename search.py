import os
import re
import argparse

from collections import defaultdict


class SearchEngine:
    """Searches contents of all text files within a directory"""

    def __init__(self, directory):
        self.directory = directory

    @staticmethod
    def tokenize(text):
        """Split text into words, remove punctuation, and normalize to lowercase."""
        return re.findall(r'\b\w+\b', text.lower())


    def build_index(self):
        """Build an inverted index for all text files in the given directory."""
        index = defaultdict(list)

        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    text = file.read()
                    words = self.tokenize(text)
                    for position, word in enumerate(words):
                        index[word].append((filename, position))
        print('Index: ', index)
        return dict(index)

    def search(self):
        self.build_index()


if __name__ == "__main__":
    # First get directory as argument to executing the script
    parser = argparse.ArgumentParser(description="Simple search script")
    parser.add_argument("directory", help="The directory to search in")

    args = parser.parse_args()
    directory = args.directory

    search_engine = SearchEngine(directory)
    search_engine.search()
