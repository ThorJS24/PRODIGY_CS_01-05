from PIL import Image

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    encrypted_image = Image.new("RGB", image.size)
    pixels = image.load()
    encrypted_pixels = encrypted_image.load()
    
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            encrypted_pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    decrypted_image = Image.new("RGB", image.size)
    pixels = image.load()
    decrypted_pixels = decrypted_image.load()
    
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            decrypted_pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print("Image Encryption Tool")
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue
        image_path = input("Enter the path to the image file: ")
        output_path = input("Enter the path for the output file: ")
        key = int(input("Enter the encryption/decryption key (integer): "))
        
        if choice == 'e':
            encrypt_image(image_path, output_path, key)
        else:
            decrypt_image(image_path, output_path, key)
        
        another = input("Do you want to process another image? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
