import sys


def count_char(text):
    """ This function takes a text str and counts the number of upper,
    lower letters, digits, spaces, and punctuation marks in the text. """

    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    digit_count = sum(1 for char in text if char.isdigit())
    space_count = sum(1 for char in text if char.isspace())
    punctuation_count = sum(
        1 for char in text if not char.isalnum() and not char.isspace()
    )

    print(f"The text contains {len(text)} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    """Main function that handles the input argument and calls the
    count_char to display the output of counting."""
    try:
        assert len(sys.argv) <= 2, \
            "AssertionError: more than one argument provided"

        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("What is the text to count?\n")
            text = sys.stdin.readline().rstrip("\n")

        if not text:
            raise ValueError("Error: Empty input provided")

        count_char(text)

    except Exception as e:
        sys.exit(f"\n{str(e)}")


if __name__ == "__main__":
    main()
