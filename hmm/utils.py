import os
import subprocess


def prune_annotations(profiles_path, annotations_path, mock=True):
    real_clusters = {int(filename.split(".")[0]) for filename in os.listdir(profiles_path)}

    for filename in os.listdir(annotations_path):
        cluster = int(filename.split("_")[1])

        if cluster not in real_clusters:
            os.remove(os.path.join(annotations_path, filename))


def check_missing(profiles_path, annotations_path):
    profiles = {int(filename.split(".")[0]) for filename in os.listdir(profiles_path)}
    annotations = {int(filename.split("_")[1]) for filename in os.listdir(annotations_path)}

    result = {
        "profiles": [p for p in profiles if p not in annotations],
        "annotations": [a for a in annotations if a not in profiles]
    }

    return result


def split_hmm_file(path):
    buffer = list()

    try:
        os.rmdir("out_split")
    except FileNotFoundError:
        pass

    os.mkdir("out_split")

    with open(path, "r") as f:
        cluster = None

        for line in f:
            if line[0:4] == "NAME":
                cluster = line.split("_")[1].rstrip()

            elif line == "//\n":                
                with open(os.path.join("out_split", cluster + ".hmm"), "w") as o:
                    o.write("".join(buffer))

                buffer = list()
                
                continue

            buffer.append(line)

def hmmstat(path):
    output = subprocess.check_output(["hmmstat", path])

    result = [line.split() for line in output.decode("utf-8").split("\n") if line and line[0] != "#"]

    return [{
        "cluster": int(line[1].replace("vFam_", "")),
        "count": int(line[3]),
        "length": int(line[5])
    } for line in result]
