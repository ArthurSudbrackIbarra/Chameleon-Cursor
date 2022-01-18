# Imports.
import os
from pynput.keyboard import Listener, Key
import pyautogui
import PIL.ImageGrab
import pyperclip
import simpleaudio


# Function to get the color of the pixel in a (x,y) coordinate.
# Returns a tuple of size 3 containing the RGB values.
def get_pixel_color(coordinates):
    return PIL.ImageGrab.grab().load()[coordinates[0], coordinates[1]]


# Function to convert an RGB tuple to a hexadecimal string.
def rgb_to_hex(rgb_tuple):
    return "#%02x%02x%02x" % rgb_tuple


# Function to copy a text to the user's clipboard.
def copy_to_clipboard(text):
    pyperclip.copy(text)


# Function to play a wav file in the same path as this program.
def play_audio(audio_name):
    directory = os.path.dirname(__file__)
    file = os.path.join(directory, audio_name)
    wave_obj = simpleaudio.WaveObject.from_wave_file(file)
    wave_obj.play()


# Function that will be triggered whenever the user presses a key.
def on_press(key):
    if key == Key.shift_r:
        current_cursor_coordinates = pyautogui.position()
        rgb_tuple = get_pixel_color(current_cursor_coordinates)
        hex_value = rgb_to_hex(rgb_tuple)
        print(f"Hexadecimal Color Value: {hex_value}")
        copy_to_clipboard(hex_value)
        play_audio("color_copied.wav")


# Main function.
def main():
    with Listener(on_press=on_press) as listener:
        print("\nNow listening to keyboard input!\n")
        listener.join()


if __name__ == '__main__':
    main()
