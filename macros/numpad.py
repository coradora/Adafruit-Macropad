# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
numlockToggle = True

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros': [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x6b1a68, '7', [Keycode.KEYPAD_SEVEN]),
        (0x6b1a68, '8', [Keycode.KEYPAD_EIGHT]),
        (0x6b1a68, '9', [Keycode.KEYPAD_NINE]),
        # 2nd row ----------
        (0x6b1a68, '4', [Keycode.KEYPAD_FOUR]),
        (0x6b1a68, '5', [Keycode.KEYPAD_FIVE]),
        (0x6b1a68, '6', [Keycode.KEYPAD_SIX]),
        # 3rd row ----------
        (0x6b1a68, '1', [Keycode.KEYPAD_ONE]),
        (0x6b1a68, '2', [Keycode.KEYPAD_TWO]),
        (0x6b1a68, '3', [Keycode.KEYPAD_THREE]),
        # 4th row ----------
        (0x0A0EFE, 'Enter', [Keycode.KEYPAD_ENTER]),
        (0x6b1a68, '0', [Keycode.KEYPAD_ZERO]),
        (0x0A0EFE, '.', [Keycode.KEYPAD_PERIOD]),
        # Encoder button ---
        (0x000000, '', [Keycode.KEYPAD_NUMLOCK])
    ]
}



