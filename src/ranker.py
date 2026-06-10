def rank_candidates(candidates):

    candidates.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    for i, candidate in enumerate(
            candidates,
            start=1):

        candidate["rank"] = i

    return candidates