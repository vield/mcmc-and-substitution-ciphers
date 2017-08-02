import pprint
import sys


alphabet = "abcdefghijklmnopqrstuvwxyz ?"


def initialize_probabilities():
    # Initialize all counters so that each transition has a tiny initial probability.
    # Well... by probability I mean 'count'
    all_ones = dict([(letter, 1) for letter in alphabet])
    probs = dict([(letter, all_ones.copy()) for letter in alphabet])
    return probs


def update_probabilities(line, probs):
    # Assume line is preceded and followed by a space
    # Get all transition pairs

    line = ' ' + line.lower() + ' '

    for i in range(1, len(line)):
        first = line[i-1] if line[i-1] in alphabet else '?'
        second = line[i] if line[i] in alphabet else '?'

        probs[first][second] += 1


if __name__ == "__main__":

    probs = initialize_probabilities()

    with open(sys.argv[1]) as f:
        for line in f:
            update_probabilities(line, probs)

    pprint.pprint(probs)