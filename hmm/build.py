import collections
import gzip
import json
import os
import sys

ANNOTATIONS_PATH = os.path.join(sys.path[0], "annotations")


def guess_definition(annotation):
    names = [entry["name"] for entry in annotation["entries"]]
    top_three = collections.Counter(names).most_common(3)
    top_names = [entry[0] for entry in top_three]
    return ", ".join(top_names)


def dir_to_json(dir_path, output_path):
    paths = os.listdir(dir_path)

    annotations = list()

    for path in paths:
        document = {"entries": []}

        with open(os.path.join(dir_path, path), "r") as vfam_file:
            for line in vfam_file:

                line = line.rstrip()
                data = " ".join(line.split()[1:])

                if line.startswith("CLUSTER"):
                    document["cluster"] = int(data)

                if line.startswith("NUM_SEQ"):
                    document["count"] = int(data)

                if line.startswith("LENGTH"):
                    document["length"] = int(data)

                if line.startswith("RELATIVE_ENTROPY"):
                    document["mean_entropy"] = float(data)

                if line.startswith("TOTAL_RELATIVE"):
                    document["total_entropy"] = float(data)

                if line.startswith("FAMILIES"):
                    document["families"] = json.loads(data.replace("'", '"'))

                if line.startswith("GENERA"):
                    document["genera"] = json.loads(data.replace("'", '"'))

                if line.startswith("FASTA"):
                    continue

                if "|" in line:
                    line = line.split("|")
                    name_field = line[5].split("[")

                    document["entries"].append({
                        "gi": line[1],
                        "accession": line[3],
                        "name": name_field[0].strip(),
                        "organism": name_field[1].replace("]", "").strip()
                    })

        annotations.append(document)

    with gzip.open(output_path, "wt") as f:
        json.dump(annotations, f)


def join_profiles(dir_path, target_path):
    with open(target_path, "w") as o:
        for filename in os.listdir(dir_path):
            path = os.path.join(dir_path, filename)

            with open(path, "r") as f:
                o.write(f.read())
                o.write("\\")
