import pytest
from library_item import LibraryItem  

# Tests for the LibraryItem class
class TestLibraryItem:
    # Test initialization
    def test_initialization(self):
        item = LibraryItem("Inception", "Christopher Nolan", 5)
        assert item.name == "Inception"
        assert item.director == "Christopher Nolan"
        assert item.rating == 5
        assert item.play_count == 0

        # Test initialization with default rating
        default_item = LibraryItem("Interstellar", "Christopher Nolan")
        assert default_item.rating == 0

    # Test the info method
    def test_info(self):
        item = LibraryItem("Inception", "Christopher Nolan", 3)
        expected_info = "Inception - Christopher Nolan ***"
        assert item.info() == expected_info

        # Test info with different ratings
        item.rating = 5
        expected_info_updated = "Inception - Christopher Nolan *****"
        assert item.info() == expected_info_updated

    # Test the stars method
    def test_stars(self):
        item = LibraryItem("Inception", "Christopher Nolan", 3)
        assert item.stars() == "***"

        # Test stars with different ratings
        item.rating = 5
        assert item.stars() == "*****"

        # Test stars with no stars
        item.rating = 0
        assert item.stars() == ""
