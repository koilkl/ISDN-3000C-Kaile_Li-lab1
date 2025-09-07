import cv2
from PIL import Image
from rich.console import Console
from rich.text import Text
import numpy as np
import argparse
import msvcrt  # For capturing keyboard input on Windows
import time  # For controlling frame rate

# Default ASCII character ramp
DEFAULT_ASCII_CHARS = '.:-=+*#%@'
FRAME_DELAY = 0.1  # Frame interval in seconds (controls refresh speed; larger values = slower)


def resize_and_grayscale(image, target_width):
    """Resize the image to the target width and convert it to grayscale."""
    original_width, original_height = image.size
    aspect_ratio = original_height / original_width
    new_height = int(target_width * aspect_ratio)
    resized_image = image.resize((target_width, new_height))
    grayscale_image = resized_image.convert('L')
    return resized_image, grayscale_image  # Return resized color image and grayscale image (matching dimensions)


def map_pixel_to_char(pixel_value, char_ramp=DEFAULT_ASCII_CHARS):
    """Map a grayscale pixel value to a character in the character ramp."""
    ramp_length = len(char_ramp)
    index = int((pixel_value / 255) * (ramp_length - 1))
    return char_ramp[index]


def process_image_for_ascii(image, width,char_ramp=DEFAULT_ASCII_CHARS):
    """Convert an image to ASCII art and print it with color."""
    # Get resized color image and grayscale image (same dimensions for coordinate matching)
    resized_color_img, grayscale_image = resize_and_grayscale(image,width)
    console = Console()
    console.clear()  # Clear the screen to avoid frame overlapping
    for y in range(grayscale_image.height):
        line = Text()  # Accumulate colored characters with rich.Text
        for x in range(grayscale_image.width):
            # Get color from resized color image (matching coordinates)
            r, g, b = resized_color_img.getpixel((x, y))[:3]
            # Map grayscale pixel value to ASCII character
            ascii_char = map_pixel_to_char(grayscale_image.getpixel((x, y)), char_ramp)
            line.append(ascii_char, style=f"rgb({r},{g},{b})")
        console.print(line)  # Print a line of colored ASCII


def process_frame_for_ascii(frame,width, char_ramp=DEFAULT_ASCII_CHARS):
    """Process a video frame and print it as colored ASCII art with controlled speed."""
    pillow_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    process_image_for_ascii(pillow_img, width,char_ramp)
    time.sleep(FRAME_DELAY)  # Add delay between frames to control refresh rate


def main():
    parser = argparse.ArgumentParser(description="Generate ASCII art from an image or webcam.")
    parser.add_argument('--image', type=str, help="Path to the image file.", default="")
    parser.add_argument('--chars', type=str, default=DEFAULT_ASCII_CHARS,
                        help="Custom ASCII character ramp for mapping.")
    parser.add_argument('--width', type=int, default=100,
                        help="Target width of the ASCII art (smaller = faster/simpler).")
    args = parser.parse_args()

    char_ramp = args.chars
    if args.image:
        try:
            with Image.open(args.image) as img:
                print("Processing image...")
                process_image_for_ascii(img, args.width,char_ramp)
        except FileNotFoundError:
            print(f"Error: File not found at '{args.image}'. Defaulting to webcam.")
            args.image = ""
        except IOError:
            print(f"Unable to open image. Please check the path: '{args.image}'. Defaulting to webcam.")
            args.image = ""

    # Default to webcam if no image provided or on error
    if not args.image:
        print("Processing webcam feed. Press 'q' to quit.")
        video_capture = cv2.VideoCapture(0)
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            process_frame_for_ascii(frame, args.width,char_ramp)

            # Check for 'q' key press to quit
            if msvcrt.kbhit() and msvcrt.getch().decode('utf-8').lower() == 'q':
                break

        video_capture.release()


if __name__ == "__main__":
    main()