import eyed3
import shutil
import os

PATH = '/Users/linoman/Downloads/music'
INPUT_PATH = os.path.join(PATH, 'mp3')
OUTPUT_PATH = os.path.join(PATH, 'final')

mp3s = os.listdir(INPUT_PATH)
QUERY = '311 - From Chaos'

for mp3 in mp3s:
  mp3_path = os.path.join(INPUT_PATH, mp3)

  if QUERY in mp3:
    song = eyed3.load(mp3_path)
    song.tag.recording_date = '2001'
    song.tag.save()
    print('update', mp3)