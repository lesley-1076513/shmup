import subprocess
import os

entry_point = "src/main.py"

match os.name:
    case "nt":
        python = "pythonw"
    case _:
        python = "python3"

subprocess.call([python, entry_point])
