from pathlib import Path
win_dir = Path('c:/Windows')
not_exists_dir = Path('C:/XYZW')
calc_file = Path('C:/Windows/System32/calc.exe')

print(win_dir.exists())
print(win_dir.is_dir())
print(not_exists_dir.exists())
print(not_exists_dir.is_dir())
print(calc_file.exists())
print(calc_file.is_dir())
print(calc_file.is_file())