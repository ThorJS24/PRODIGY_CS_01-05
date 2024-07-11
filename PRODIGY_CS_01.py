def caesar_cipher(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if direction == 'encrypt' else -shift
            shift_base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - shift_base + shift_amount) % 26 + shift_base)
        else:
            result += char
    return result

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue
        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))
        direction = 'encrypt' if choice == 'e' else 'decrypt'
        result = caesar_cipher(message, shift, direction)
        print(f"The {direction}ed message is: {result}")
        another = input("Do you want to process another message? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
