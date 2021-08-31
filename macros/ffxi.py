# Macro configuration for Final Fantasy XI. Useful for those 
# without a function row on their keyboard.

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Final Fantasy XI',  # Application name
    'macros': [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x6b1a68, 'F1', [Keycode.F1]),
        (0x6b1a68, 'F2', [Keycode.F2]),
        (0x6b1a68, 'F3', [Keycode.F3]),
        # 2nd row ----------
        (0x6b1a68, 'F4', [Keycode.F4]),
        (0x6b1a68, 'F5', [Keycode.F5]),
        (0x6b1a68, 'F6', [Keycode.F6]),
        # 3rd row ----------
        (0x6b1a68, 'Self', [Keycode.F7]),
        (0x6b1a68, 'NPC', [Keycode.F8]),
        (0x6b1a68, 'PC', [Keycode.F9]),
        # 4th row ----------
        (0x4f0b4c, 'Mount', [Keycode.ALT, Keycode.ZERO]),
        (0x6b1a68, 'Trusts', [Keycode.ALT, Keycode.NINE]),
        (0x4f0b4c, 'Refa', [Keycode.ALT, Keycode.EIGHT]),
    ]
}
