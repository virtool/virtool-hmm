import filecmp
import json
import operator
import os
import sys

import hmm.build

JSON_PATH = os.path.join(sys.path[0], "tests", "annotations.json")
ANNOTATIONS_PATH = os.path.join(sys.path[0], "tests", "annotations")


def test_dir_to_json(tmpdir):
    """
    Test that the collection of vFam text files is correctly translated to JSON.

    """
    output_path = os.path.join(str(tmpdir), "test.json")

    hmm.build.dir_to_json(ANNOTATIONS_PATH, output_path)

    assert os.path.isfile(output_path)

    with open(output_path) as f:
        output = json.load(f)

    with open(JSON_PATH) as f:
        expected = json.load(f)

    for data in (output, expected):
        data = sorted(data, key=operator.itemgetter("cluster"))

    for x, y in zip(output, expected):
        assert x == y
