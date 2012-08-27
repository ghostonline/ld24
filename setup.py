import sys
from cx_Freeze import setup, Executable

import manager

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["pyglet", "planar"] + manager.components, "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Air Fighter",
        version = "1.0",
        description = "Ludum Dare 24 entry",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base)])