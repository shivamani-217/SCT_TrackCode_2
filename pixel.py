from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, mode="swap"):
    # Load image and convert to numpy array
    img = Image.open(input_path)
    arr = np.array(img)

    if mode == "swap":
        # Swap pixel values between rows
        arr[::2], arr[1::2] = arr[1::2], arr[::2].copy()
    elif mode == "add":
        # Add a constant to each pixel (mod 256 to keep valid range)
        arr = (arr + 50) % 256
    elif mode == "xor":
        # XOR each pixel with a key
        key = 123
        arr = arr ^ key

    # Save encrypted image
    encrypted_img = Image.fromarray(arr.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Image encrypted using {mode} mode and saved to {output_path}")

def decrypt_image(input_path, output_path, mode="swap"):
    # Load encrypted image
    img = Image.open(input_path)
    arr = np.array(img)

    if mode == "swap":
        # Swap back rows
        arr[::2], arr[1::2] = arr[1::2], arr[::2].copy()
    elif mode == "add":
        # Subtract the constant
        arr = (arr - 50) % 256
    elif mode == "xor":
        # XOR again with the same key
        key = 123
        arr = arr ^ key

    # Save decrypted image
    decrypted_img = Image.fromarray(arr.astype('uint8'))
    decrypted_img.save(output_path)
    print(f"Image decrypted using {mode} mode and saved to {output_path}")

# Example usage
encrypt_image("input1.jpg", "encrypted.jpg", mode="xor")
decrypt_image("encrypted.jpg", "decrypted.jpg", mode="xor")
