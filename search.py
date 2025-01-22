import os
import re
import argparse

from collections import defaultdict


class SearchEngine:
    """Searches contents of all text files within a directory"""

    def __init__(self, directory):
        self.directory = directory
        self._index = defaultdict(list)
        self._file_count = 0
        self.text_files = []

    @staticmethod
    def tokenize(text: str) -> [str]:
        """Split text into words, remove punctuation, and normalize to lowercase."""

        return re.findall(r"\b\w+\b", text.lower())


    def build_index(self) -> dict:
        """Build an inverted index for all text files in the given directory."""

        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):
                self._file_count += 1
                self.text_files.append(filename)
                filepath = os.path.join(self.directory, filename)
                with open(filepath, "r", encoding="utf-8") as file:
                    text = file.read()
                    words = self.tokenize(text)
                    for position, word in enumerate(words):
                        self._index[word].append((filename, position))
        return dict(self._index)

    def file_rank(self, search_term: str, filename: str) -> (str, tuple):
        """"""
        rank_count = 0
        search_term_set = set(self.tokenize(search_term))

        for term in search_term_set:
            if term not in self._index.keys():
                continue
            rank_count += 1 if any([True for file_tuple in self._index[term] if file_tuple[0] == filename]) else 0

        return filename, int(rank_count / len(search_term_set) * 100)


    def search_flow(self):
        """Multiple searches can be executed sequentially until user quits"""

        self._index = self.build_index()

        while True:
            ranks = []
            search = input("Enter search term (or 'quit' to exit): ")
            if search == "quit":
                break
            if not search:
                continue

            for filename in self.text_files:
                ranks.append(self.file_rank(search, filename))

            if not any([rank[1] for rank in ranks]):
                print("No matches found.")
            else:
                ranks = sorted(ranks, key=lambda x: -x[1])

                for rank in ranks:
                    print(f"{rank[0]}: {rank[1]}%")
                print("\n") # Establishes end of results for search


if __name__ == "__main__":
    # First get directory as argument to executing the script
    parser = argparse.ArgumentParser(description="Simple search script")
    parser.add_argument("directory", help="The directory to search in")

    args = parser.parse_args()
    directory_path = args.directory

    search_engine = SearchEngine(directory_path)
    search_engine.search_flow()
