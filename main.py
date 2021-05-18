import eyed3
import shutil
import os

PATH = '/Users/linoman/Downloads/music'
INPUT_PATH = os.path.join(PATH, 'mp3')
OUTPUT_PATH = os.path.join(PATH, 'final')

mp3s = os.listdir(INPUT_PATH)
counter = 0
for mp3 in sorted(mp3s):
  counter += 1
  mp3_path = os.path.join(INPUT_PATH, mp3)
  song = eyed3.load(mp3_path)
  t = song.tag
  print(mp3_path)

  if not t.recording_date or not t.album or not t.track_num[0] or not t.title or not t.artist:
    print('recording_date: ', t.recording_date, bool(t.recording_date))
    print(t.album, bool(t.album))
    print(t.track_num[0], bool(t.track_num[0]))
    print(t.title, bool(t.title))
    print(t.artist, bool(t.artist))
    print(mp3_path)
    print(counter, '/', len(mp3s))
    break

  album = f'{t.recording_date} - {t.album}'
  track_name = f'{"%02d" % t.track_num[0]} - {t.title}.mp3'
  final_path = os.path.join(OUTPUT_PATH, t.artist, album)

  if not os.path.exists(final_path):
    os.makedirs(final_path)

  final_song_path = os.path.join(final_path, track_name)

  if not os.path.exists(final_song_path):
    shutil.copyfile(mp3_path, final_song_path)
