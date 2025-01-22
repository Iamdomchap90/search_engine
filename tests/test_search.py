import pytest

from search import SearchEngine


class TestSearchEngine:
    @pytest.fixture
    def search_engine(self, tmp_path):
        # Create temporary test files in the directory
        test_dir = tmp_path / "test_dir"
        test_dir.mkdir()

        # Add test files
        file_1 = test_dir / "file_1.txt"
        file_1.write_text("The quick brown fox jumps over the lazy dog.")

        file_2 = test_dir / "file_2.md"
        file_2.write_text("The quick brown fox jumps over the lazy dog.")

        file_3 = test_dir / "file_3.txt"
        file_3.write_text("The quick brown cat jumps over the humble caterpillar.")

        return SearchEngine(directory=test_dir)

    def test_tokenize_correctly_lists_words_with_spaces_and_punctuation(self, search_engine):
        result = search_engine.tokenize("The quick brown cat jumps over the humble caterpillar.")
        assert result.count("the") == 2
        assert len(result) == 9
        assert "caterpillar" in result

    def test_build_index_only_indexes_text_files(self, search_engine):
        index = search_engine.build_index()
        if any([position[0] == "file_2.md" for position_list in index.values() for position in position_list]):
            assert False
        assert True

    def test_build_index_has_correect_positions(self, search_engine):
        index = search_engine.build_index()
        search_list_one = index["the"]
        assert ("file_3.txt", 0) in search_list_one and ("file_3.txt", 6) in search_list_one
        assert ("file_3.txt", 8) in index["caterpillar"]

    def test_file_rank_works_for_no_matches(self, search_engine):
        search_engine.build_index()
        result = search_engine.file_rank("abcdef", "file_3.txt")
        assert result == ("file_3.txt", 0)
        result_two = search_engine.file_rank("jim beam catastrophic", "file_1.txt")
        assert result_two == ("file_1.txt", 0)

    def test_file_rank_calculates_matches(self, search_engine):
        search_engine.build_index()
        result = search_engine.file_rank("The quick cat", "file_1.txt")
        assert result == ("file_1.txt", 66)
        result_two = search_engine.file_rank("The humble caterpillar", "file_3.txt")
        assert result_two == ("file_3.txt", 100)


