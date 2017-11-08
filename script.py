def vfam_text_to_json(annotation_path, output_path=None):
    paths = os.listdir(annotation_path)

    annotations = list()

    for path in paths:
        document = {"entries": []}

        with open(os.path.join(annotation_path, path), "r") as vfam_file:
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

    if output_path:
        with gzip.open(output_path, "wt") as output:
            json.dump(annotations, output)

    return annotations
