# Colorful ASCII Art Generator

A Python-based tool that converts static images and real-time webcam feed into vibrant, customizable ASCII art. This application preserves original colors while mapping pixel brightness to ASCII characters, delivering a visually engaging console output.


## Features
- **Dual Input Support**: Convert static images (JPG, PNG, etc.) or process real-time webcam feed.
- **Color Preservation**: Retains the original color of each pixel in the ASCII output.
- **Controlled Frame Rate**: Adjustable delay for webcam mode to prevent fast, unreadable updates.
- **Customizable Parameters**: Modify ASCII character sets, output width, and frame speed.
- **Console Optimization**: Clears old frames automatically to avoid visual clutter.


## Prerequisites
- Python 3.7 or higher (tested on 3.8+)
- Required Python libraries:
  - `opencv-python`: For video capture and frame processing.
  - `pillow`: For image resizing, grayscaling, and pixel color extraction.
  - `rich`: For styled console output (supports RGB colors).
  - `numpy`: For efficient image data handling.

## Changable parameter
- FRAME_DELAY # Frame interval in seconds 
- DEFAULT_ASCII_CHARS # Default ASCII character ramp

# Use instruction/help
## keyword
- You can use the three key words regradless of sequence,and the blank value will be set at default value.

- In other words,if you just use "python main.py", the app will run by default values.

- --char 
    - usage: input a character array is used to replace the pixel,and the replacement method is comparing the brightness of this pixel after convert into gray and replace them by the sequence from left to right(left is smallest). 
    - template:python main.py --char 1234567890(if null,it will use the default array)

- --image
    - usage: input a image path
    - template:python main.py --image yourdir/yourfile.jpeg
    (if input is  invalid ,it will same as python main.py and open camera instead,but if it is null,the app will throw error)
    
- --width 
    - usage: constrain the width of the output picture,and the height will keep same ratio with width
    - template: python main.py --width 100
## end method
- if path is invalid,the mode will turn to camera read.For this mode,you need to press 'q' as the ending signal for the app.
- if path is valid and not null. It will end it life automaticly.