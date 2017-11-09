import filecmp
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

    assert filecmp.cmp(JSON_PATH, output_path)
