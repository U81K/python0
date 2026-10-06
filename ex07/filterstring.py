import sys


def main():
    """
    Accepts a string S and an integer N.
    Outputs a list of words from S that have a length greater than N.
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        s = sys.argv[1]
    except AssertionError as e:
        print("AssertionError:", e)
        return 1

    filtered_words = [word for word in filter(lambda w: len(w) > n, s.split())]
    print(filtered_words)

    return 0


if __name__ == "__main__":
    main()
