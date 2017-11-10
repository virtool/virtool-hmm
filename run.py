import hmm.build


if __name__ == "__main__":
    # Make joined HMM file
    clusters = hmm.build.join_profiles(hmm.build.PROFILES_PATH, "gh_build/hmm/profiles.hmm")

    # Make annotations json.gz file
    hmm.build.dir_to_json(hmm.build.ANNOTATIONS_PATH, "gh_build/hmm/annotations.json", include=clusters)

    
