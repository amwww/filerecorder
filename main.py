import os

filename = '/Users/3017079/Desktop/Projects/Python/MahjongBot/main.py'

destination = f'records/mahjongbot'
try:
    os.mkdir(destination)
except Exception:
    print('Folder could not be made, or it already exisits.')

def getlastid():
    lastcheckid = 0
    while True:
        try:
            with open(f'{destination}/{lastcheckid}.txt', 'r') as f:
                pass
        except FileNotFoundError:
            return lastcheckid
        lastcheckid += 1

lastfile = None
while True:
    with open(filename, 'r') as f:
        text = f.read()
    if text == lastfile or text == '':
        continue
    print(f'Change Detected in {filename}')
    print(text)
    lastfile = text
    last = getlastid()
    with open(f'{destination}/{last}.txt', 'w+') as f:
        pass
    with open(f'{destination}/{last}.txt', 'w') as f:
        f.write(text)