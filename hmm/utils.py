import os
import subprocess


def prune_annotations(profiles_path, annotations_path, mock=True):
    clusters = [int(f.split("_")[1]) for f in os.listdir(annotations_path)]

    return clusters


def hmmstat(path):
    output = subprocess.check_output(["hmmstat", path])

    result = [line.split() for line in output.decode("utf-8").split("\n") if line and line[0] != "#"]

    return [{
        "cluster": int(line[1].replace("vFam_", "")),
        "count": int(line[3]),
        "length": int(line[5])
    } for line in result]
