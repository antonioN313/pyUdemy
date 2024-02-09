from pathlib import Path
import os

p = Path('c:/Users/admin/Desktop/python_Antonio/pyRegex.py')
print(p.anchor)
print(p.drive)
print(p.parent)
print(p.stem)
print(p.suffix)
print(p.parents)
print(p.parents[0])
print(p.parents[1])
print(p.parents[2])
print(p.parents[3])
print(p.parents[4])
print('\n')
arquivo = 'c:/Users/admin/Desktop/python_Antonio/pyRegex.py'
print(os.path.basename(arquivo))
print(os.path.dirname(arquivo))
print(os.path.split(arquivo))