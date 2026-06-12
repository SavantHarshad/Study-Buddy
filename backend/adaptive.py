from memory import get_weak_topics


def get_revision_topics():

    weak = get_weak_topics()

    return [x[0] for x in weak]
