from pathlib import Path
import os
Path('Desktop','Python_Antonio')
#WindowsPath('Desktop\Python_Antonio')
print(Path('Desktop','Python_Antonio'))
print('\n')
print(str(Path('Desktop','Python_Antonio')))
print('\n')
print(Path('Desktop') /'Python_Antonio')
print('\n')
HomeFolder = r'C:\Users\admin\Desktop'
subFolder = 'python_Antonio'
print(HomeFolder + '\\' + subFolder)
print('\n')
print(Path.cwd())
os.chdir('c:\\Users\\admin')
print(Path.cwd())
print(Path.home())