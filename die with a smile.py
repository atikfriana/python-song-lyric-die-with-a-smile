import time
from threading import Thread
import sys

lyrics = [
    ("So I'ma love you every night like it's the last night", 0.05),
    ("Like it's the last night", 0.06),
    ("If the world was ending", 0.06),
    ("I'd wanna be next to you", 0.08),
    ("If the party was over", 0.05),
    ("And our time on Earth was through", 0.12),
    ("I'd wanna hold you just for a while", 0.12),
]
delays = [0, 4.0, 7.0, 10.0, 16.0, 18.0, 25.0]

def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def play_lyric(lyric, delay_time, char_delay):
    time.sleep(delay_time)  # Waits for the delay time
    animate_text(lyric, char_delay)

threads = []
for i in range(len(lyrics)):
    lyric, char_delay = lyrics[i]
    delay_time = delays[i]
    thread = Thread(target=play_lyric, args=(lyric, delay_time, char_delay))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
