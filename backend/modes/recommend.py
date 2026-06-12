from adaptive import get_revision_topics


def recommend_mode():

    topics = get_revision_topics()

    if len(topics) == 0:

        print("\nNo recommendations yet.")
        return

    print("\nRecommended Revision:\n")

    for topic in topics:

        print("-", topic[:60])
