# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'FFXIV Emotes',  # Application name
    'macros': [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFF9933, 'Laugh', [Keycode.ENTER, '/laugh\n']),
        (0xFF9933, 'MCH', [Keycode.ALT, Keycode.SHIFT, Keycode.FIVE]),
        (0xFF9933, 'DNC', [Keycode.ALT, Keycode.SHIFT, Keycode.THREE]),
        # 2nd row ----------
        (0xFF3366, 'SMN', [Keycode.CONTROL, Keycode.SHIFT, Keycode.THREE]),
        (0xFF3366, 'BLM', [Keycode.CONTROL, Keycode.SHIFT, Keycode.FOUR]),
        (0xFF3366, 'RDM', [Keycode.CONTROL, Keycode.SHIFT, Keycode.FIVE]),
        # 3rd row ----------
        (0x558B2F, 'WHM', [Keycode.ALT, Keycode.SHIFT, Keycode.SIX]),
        (0x558B2F, 'SCH', [Keycode.ALT, Keycode.SHIFT, Keycode.EIGHT]),
        (0x558B2F, 'AST', [Keycode.ALT, Keycode.SHIFT, Keycode.SEVEN]),
        # 4th row ----------
        (0x3399FF, 'WAR', [Keycode.ALT, Keycode.SHIFT, Keycode.EQUALS]),
        (0x3399FF, 'DRK', [Keycode.ALT, Keycode.SHIFT, Keycode.MINUS]),
        (0x3399FF, 'PLD', [Keycode.ALT, Keycode.SHIFT, Keycode.ZERO]),
    ]
}
