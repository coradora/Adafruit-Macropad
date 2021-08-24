from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "HOME",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQTEAM
        # 1st row ----------
        (0x193375, "< Back", [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x193375, "Fwd >", [Keycode.ALT, Keycode.RIGHT_ARROW]),
        (0x193375, "Up", [Keycode.SHIFT, " "]),  # Scroll up
        # 2nd row ----------
        (0x193375, "Vol -", [Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, Keycode.MINUS]),
        (0x193375, "Vol +", [Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, Keycode.EQUALS]),
        (0x193375, "Down", " "),  # Scroll down
        # 3rd row ----------
        (0x5B1975, "Taskmgr", [Keycode.CONTROL, Keycode.SHIFT, Keycode.ESCAPE]),
        (0x5B1975, "Term", [Keycode.WINDOWS, "2"]),  # For opening personal programs they must be pinned to taskbar.
        # The bind number is tied to the order on the task bar (1 indexed)
        (0x5B1975, "Chrome", [Keycode.WINDOWS, "1"]),
        # 4th row ----------
        (0xE07516, "Copy", [Keycode.CONTROL, "c"]),
        (0xE07516, "Paste", [Keycode.CONTROL, "v"]),
        (0xE07516, "Snip", [Keycode.WINDOWS, Keycode.SHIFT, Keycode.S]), 
        # Encoder button ---
        (0x000000, "", [Keycode.CONTROL, "w"]),  # Close tab
    ],
}
# Write your code here :-)
