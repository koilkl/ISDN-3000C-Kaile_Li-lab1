import sys
from PIL import Image

# TODO: Define your character ramp
ASCII_CHARS = "..." 

def resize_and_grayscale(image, new_width=100):
    # TODO: Implement with AI's help
    pass

def map_pixel_to_char(pixel_value):
    # TODO: Implement with AI's help
    pass

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv} <image_path>")
        return

    image_path = sys.argv
    
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: File not found at '{image_path}'")
        return

    # --- Your main logic will go here ---
    # 1. Resize and convert the image
    # 2. Get the pixel data
    # 3. Build the ASCII string
    # 4. Print the final art
    
    print("ASCII Art generation is ready to be built!")


if __name__ == "__main__":
    main()