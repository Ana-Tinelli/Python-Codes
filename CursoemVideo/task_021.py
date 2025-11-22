import winsound
from pathlib import Path

audio = Path(r"C:\Users\fabri\PycharmProjects\PythonProject\CursoemVideo\podcast.wav")

winsound.PlaySound(str(audio), winsound.SND_FILENAME | winsound.SND_ASYNC)

print("Playing - Podcast Audio File, press enter to stop.")
input()

winsound.PlaySound(None, winsound.SND_PURGE)

