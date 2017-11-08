import gzip
import json
import operator
import os


class TestVFamToJSON:

    def test_valid(self, annotation_path, expected_annotations):
        """
        Test that the collection of vFam text files is correctly translated to JSON.

        """
        result = virtool.virus_hmm.vfam_text_to_json(annotation_path)

        to_check = [{key: r[key] for key in r if key not in ("entries", "genera", "families")} for r in result]

        to_check = sorted(to_check, key=operator.itemgetter("cluster"))
        expected_annotations = sorted(to_check, key=operator.itemgetter("cluster"))

        assert all(x == y for x, y in zip(to_check, expected_annotations))

        assert not os.path.isfile("./annotations.json.gz")

    def test_write_file(self, annotation_path, expected_annotations, tmpdir):
        """
        Test that the JSON data is written to the output path when it is provided.

        """
        path = os.path.join(str(tmpdir), "annotations.json.gz")

        virtool.virus_hmm.vfam_text_to_json(annotation_path, path)

        assert os.path.isfile(path)

        with gzip.open(path, "rt") as json_file:
            output = json.load(json_file)

        to_check = [{key: r[key] for key in r if key not in ["entries", "genera", "families"]} for r in output]

        to_check = sorted(to_check, key=operator.itemgetter("cluster"))
        expected_annotations = sorted(to_check, key=operator.itemgetter("cluster"))

        assert all(x == y for x, y in zip(to_check, expected_annotations))
