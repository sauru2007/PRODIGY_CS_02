from PIL import Image
import os

def encrypt_image(image_path, key):
    """Encrypt the image by modifying pixel values."""
    try:
        image = Image.open(image_path)
        pixels = image.load()

        for x in range(image.width):
            for y in range(image.height):
                r, g, b = pixels[x, y]
                pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

        encrypted_path = os.path.splitext(image_path)[0] + "_encrypted.png"
        image.save(encrypted_path)
        print(f"Image encrypted and saved as {encrypted_path}")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(image_path, key):
    """Decrypt the image by reversing the pixel modification."""
    try:
        image = Image.open(image_path)
        pixels = image.load()

        for x in range(image.width):
            for y in range(image.height):
                r, g, b = pixels[x, y]
                pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

        decrypted_path = os.path.splitext(image_path)[0] + "_decrypted.png"
        image.save(decrypted_path)
        print(f"Image decrypted and saved as {decrypted_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Image Encryption Tool")
    while True:
        print("\nOptions:")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            image_path = input("Enter the path to the image to encrypt: ")
            key = int(input("Enter the encryption key (integer): "))
            encrypt_image(image_path, key)

        elif choice == "2":
            image_path = input("Enter the path to the image to decrypt: ")
            key = int(input("Enter the decryption key (integer): "))
            decrypt_image(image_path, key)

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
