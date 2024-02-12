with open('C:/Users/AntonioCarlos/Desktop/pyUdemy/text.txt', encoding='utf8') as f:
    contents = f.read()
    print(contents)
lines = []
with open('C:/Users/AntonioCarlos/Desktop/pyUdemy/text.txt', encoding='utf8') as f:
    lines = f.readlines()
count = 0
for line in lines:
    count += 1
    print(f'Line {count}: {line}')
with open('C:/Users/AntonioCarlos/Desktop/pyUdemy/text.txt', encoding='utf8') as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
