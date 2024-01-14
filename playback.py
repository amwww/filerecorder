import time

playback = f'records/mahjongbot'

destination = f'playback/playback-mahjongbot.py'

with open(destination, 'w+') as f:
    f.write('')

time.sleep(1)

print('Starting Playback')

id = 0
while True:
    print(id)
    with open(f'{playback}/{id}.txt', 'r') as f:
        text = f.read()
        with open(destination, 'w') as f:
            f.write(text)
    time.sleep(0.03)
    id += 1