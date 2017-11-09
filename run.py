import hmm.build


if __name__ == "__main__":
    # Make annotations json.gz file
    hmm.build.dir_to_json(hmm.build.ANNOTATIONS_PATH, "gh_build/hmm/annotations.json")

    # Make joined HMM file
    hmm.build.join_profiles(hmm.build.PROFILES_PATH, "gh_build/hmm/profiles.hmm")
