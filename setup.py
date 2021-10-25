import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

options = {"build_exe": {"includes": "atexit"}}

executables = [Executable("ToolRemote.py", base=base)]

setup(
    name="ToolRemote",
    version="0.1",
    description="ToolRemote",
    options=options,
    executables=executables,
)