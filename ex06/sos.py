import sys


def main():
    """
    Takes a single string argument and encodes it into Morse Code.
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. "
    }

    try:
        assert len(sys.argv) == 2, "one argument required"
        input = sys.argv[1]

        morse_code = ""
        for char in input:
            char_upper = char.upper()
            if char_upper not in NESTED_MORSE:
                raise AssertionError("the arguments are bad")

            morse_code += NESTED_MORSE[char_upper]
        print(morse_code.strip())

    except AssertionError as e:
        print("AssertionError:", e)
    return 0


if __name__ == "__main__":
    main()
