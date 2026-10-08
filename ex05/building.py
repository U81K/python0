import sys


def char_counter(input):
    """
    Counts and prints the number of uppercase, lowercase, punctuation,
    spaces, and digits in a given text.
    """
    total_chars = 0
    upper_chars = 0
    lower_chars = 0
    punct_chars = 0
    spaces_chars = 0
    digits_chars = 0

    for char in input:
        total_chars += 1
        if (char.isupper()):
            upper_chars += 1
        elif (char.islower()):
            lower_chars += 1
        elif (char.isspace()):
            spaces_chars += 1
        elif (char.isdigit()):
            digits_chars += 1
        else:
            punct_chars += 1

    print("The text contains", total_chars, "characters:")
    print(upper_chars, "upper letters")
    print(lower_chars, "lower letters")
    print(punct_chars, "punctuation marks")
    print(spaces_chars, "spaces")
    print(digits_chars, "digits")


def main():
    """
    Main entry point: parses arguments, prompts for text if none is
    provided, and calls char_counter.
    """
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"

        if len(sys.argv) == 1:
            print("What is the text to count?")
            text = sys.stdin.readline()
        else:
            text = sys.argv[1]

        char_counter(text)
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
