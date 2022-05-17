from pydub import AudioSegment
from pydub.playback import play
import sys
import os

song = sys.argv[1]
extension = os.path.basename(song)


def playsong(song):
    if extension.endswith('.wav'):
        song = AudioSegment.from_wav(song)
        play(song)
    elif extension.endswith('.mp3'):
        song = AudioSegment.from_mp3(song)
        play(song)
    elif extension.endswith('.ogg'):
        song = AudioSegment.from_ogg(song)
        play(song)


if __name__ == '__main__':
    playsong(r'C:\Users\Arina\files\1.ogg')
