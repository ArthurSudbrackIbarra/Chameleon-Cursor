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


# Function that returns an absolute path based on a relative path.
def from_relative_path(file_name):
    directory = os.path.dirname(__file__)
    return os.path.join(directory, file_name)


# Variable to check whether the program audio is on or off.
is_audio_on = True


# Function that will determine whether the audio
# should be on or off when the program is started.
def init_audio_settings():
    global is_audio_on
    settings_file = open(from_relative_path("settings.txt"), "r")
    first_line = settings_file.readlines()[0]
    if first_line.find("on") == -1:
        is_audio_on = False


# Function to toggle the program audio (on -> off / off -> on).
def toggle_audio_on_off():
    global is_audio_on
    settings_file = open(from_relative_path("settings.txt"), "w")
    settings_file.seek(0)
    if is_audio_on:
        settings_file.write("audio=off")
        is_audio_on = False
    else:
        settings_file.write("audio=on")
        is_audio_on = True
    settings_file.truncate()
    settings_file.close()
    return not is_audio_on


# Function to play a wav file in the same path as this program.
def play_audio(audio_name):
    wave_obj = simpleaudio.WaveObject.from_wave_file(from_relative_path(audio_name))
    wave_obj.play()


# Function that will be triggered whenever the user presses a key.
def on_press(key):
    global is_audio_on
    if key == Key.shift_r:
        current_cursor_coordinates = pyautogui.position()
        rgb_tuple = get_pixel_color(current_cursor_coordinates)
        hex_value = rgb_to_hex(rgb_tuple)
        print(f"\nHexadecimal Color Value: {hex_value}")
        copy_to_clipboard(hex_value)
        if is_audio_on:
            play_audio("color_copied.wav")
    elif key == Key.up:
        was_audio_on = toggle_audio_on_off()
        if was_audio_on:
            print("\nProgram audio set to: OFF")
        else:
            print("\nProgram audio set to: ON")


# Main function.
def main():
    init_audio_settings()
    print("\nChameleon Cursor ™\n")
    print("Press [RIGHT SHIFT] to copy a color")
    print("Press [ARROW UP] to turn audio on/off\n")
    with Listener(on_press=on_press) as listener:
        print("Now listening to keyboard input!")
        listener.join()


if __name__ == '__main__':
    main()
