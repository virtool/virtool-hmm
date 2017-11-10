"""
Tests for the actual data in the repository, rather than the code used for data generation.

"""
import hmm.utils

ANNOTATIONS_PATH = "data/annotations"
PROFILES_PATH = "data/profiles"


def test_missing():
    result = hmm.utils.check_missing(PROFILES_PATH, ANNOTATIONS_PATH)

    assert result["profiles"] == list()
    assert result["annotations"] == list()
