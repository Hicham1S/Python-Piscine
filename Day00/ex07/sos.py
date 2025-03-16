import sys

NESTED_MORSE = {" ": "/",
                "A": ".-",
                "B": "-...",
                "C": "-.-.",
                "D": "-..",
                "E": ".",
                "F": "..-.",
                "G": "--.",
                "H": "....",
                "I": "..",
                "J": ".---",
                "K": "-.-",
                "L": ".-..",
                "M": "--",
                "N": "-.",
                "O": "---",
                "P": ".--.",
                "Q": "--.-",
                "R": ".-.",
                "S": "...",
                "T": "-",
                "U": "..-",
                "V": "...-",
                "W": ".--",
                "X": "-..-",
                "Y": "-.--",
                "Z": "--..",
                "1": ".----",
                "2": "..---",
                "3": "...--",
                "4": "....-",
                "5": ".....",
                "6": "-....",
                "7": "--...",
                "8": "---..",
                "9": "----.",
                "0": "-----"}


def convert_to_morse(user_arg: str) -> str:
    """Transform the text to Morse code"""
    morse_code = []
    for char in user_arg:
        if char.upper() in NESTED_MORSE:
            morse_code.append(NESTED_MORSE[char.upper()])
        else:
            raise AssertionError("The arguments are bad")
    return ' '.join(morse_code)


def main():
    """Main function to encode the input string to Morse code."""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("The arguments are bad")
        user_input = sys.argv[1]
        result = convert_to_morse(user_input)
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
