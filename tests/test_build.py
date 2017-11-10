import filecmp
import json
import os
import sys

import hmm.build

JSON_PATH = os.path.join("tests", "annotations.json")
ANNOTATIONS_PATH = os.path.join("tests", "annotations")


def test_dir_to_json(tmpdir):
    """
    Test that the collection of vFam text files is correctly translated to JSON.

    """
    output_path = os.path.join(str(tmpdir), "test.json")

    print(JSON_PATH, ANNOTATIONS_PATH)

    hmm.build.dir_to_json(ANNOTATIONS_PATH, output_path)

    assert os.path.isfile(output_path)

    with open(output_path, "r") as f:
        output = json.load(f)

    with open(JSON_PATH, "r") as f:
        expected = json.load(f)

    for i, doc in enumerate(output):
        assert doc == expected[i]
