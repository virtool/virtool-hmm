import gzip
import json
import operator
import os
import sys

import hmm.build

JSON_GZ_PATH = os.path.join(sys.path[0], "tests", "annotations.json.gz")
ANNOTATIONS_PATH = os.path.join(sys.path[0], "annotations")


def test_dir_to_json(tmpdir):
    """
    Test that the collection of vFam text files is correctly translated to JSON.

    """
    output_path = os.path.join(str(tmpdir), "test.json.gz")

    hmm.build.dir_to_json(ANNOTATIONS_PATH, output_path)

    assert os.path.isfile(output_path)

    with gzip.open(output_path, "rt") as json_file:
        output = json.load(json_file)

    to_check = [{key: r[key] for key in r if key not in ["entries", "genera", "families"]} for r in output]
    to_check = sorted(to_check, key=operator.itemgetter("cluster"))

    print(to_check)

    expected_annotations = [
        {"length": 133, "mean_entropy": 0.53, "count": 208, "cluster": 5, "total_entropy": 70.49},
        {"length": 356, "mean_entropy": 0.52, "count": 253, "cluster": 2, "total_entropy": 185.12},
        {"length": 96, "mean_entropy": 0.56, "count": 210, "cluster": 4, "total_entropy": 53.76},
        {"length": 505, "mean_entropy": 0.52, "count": 113, "cluster": 10, "total_entropy": 262.6},
        {"length": 612, "mean_entropy": 0.52, "count": 101, "cluster": 8, "total_entropy": 318.24},
        {"length": 136, "mean_entropy": 0.53, "count": 216, "cluster": 3, "total_entropy": 72.08},
        {"length": 500, "mean_entropy": 0.47, "count": 97, "cluster": 9, "total_entropy": 235.0}
    ]

    assert all(x == y for x, y in zip(to_check, expected_annotations))
