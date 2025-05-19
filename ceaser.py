from gpa import get_int


def main() -> int:
    shift_value = get_int("Enter the shift value (1-25): ")
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters += letters.lower()
    letters += "0123456789"
    letters += " !@#$%^&*()_+-=[]{}|;:',.<>?/`~ "
    string = input("Enter the string to encrypt: ")
    encrypted_string = ""
    for char in string:
        if char in letters:
            index = (letters.index(char) + shift_value) % len(letters)
            encrypted_string += letters[index]
        else:
            encrypted_string += char
    print("Encrypted string: " + encrypted_string)
    return 0

if __name__ == "__main__":
    main()