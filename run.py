import hmm.build


if __name__ == "__main__":
    # Make annotations json.gz file
    hmm.build.dir_to_json(hmm.build.ANNOTATIONS_PATH, "annotations.json.gz")

    # Make joined HMM file
    hmm.build.join_profiles(hmm.build.PROFILES_PATH, "profiles.hmm")
