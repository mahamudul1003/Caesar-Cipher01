def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            shifted = (ord(char) - offset + shift) % 26 + offset
            result += chr(shifted) if mode == 'encrypt' else chr((ord(char) - offset - shift) % 26 + offset)
        else:
            result += char
    return result


def main():
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        encrypted_message = caesar_cipher(message, shift, 'encrypt')
        print("Encrypted message:", encrypted_message)
    elif choice == 'd':
        decrypted_message = caesar_cipher(message, shift, 'decrypt')
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")


if __name__ == "__main__":
    main()
