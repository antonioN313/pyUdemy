from pathlib import Path
import os
print(os.listdir('c:/Users/admin/Desktop/python_Antonio'))
print(os.path.getsize('c:/Users/admin/Desktop/python_Antonio/pyAutomationMoveFiles.py'))
total_size = 0
for root,directories,filename in os.walk('c:/Users/admin/Desktop/python_Antonio'):
    total_size += os.path.getsize(os.path.join(root, filename))

print(total_size)  