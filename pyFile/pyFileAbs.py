from pathlib import Path
import os
print(Path.cwd())
print(Path.cwd().is_absolute())
print(Path('temp/python').is_absolute())
print(Path('Desktop/python_antonio'))
print(Path.cwd() / Path('Desktop/python_antonio'))
print(os.path.abspath('.'))
print(os.path.abspath('.\\Scripts'))
print(os.path.isabs('.'))
print(os.path.relpath('c:\\Windows','c:\\'))
print(os.path.relpath('c:\\Windows','c:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python38\\Scripts'))