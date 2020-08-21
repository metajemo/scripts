#!/usr/bin/env python3

import os
import sys
import shutil

AUDIO_FORMAT = 'mp3'
YOUTUBE_LIBRARY_LOCATION = '/home/pie/downloads/music/youtube_songs'
YOUTUBE_DL_COMMAND = 'youtube-dl -x -f mp4 {}'
M4A_TO_MP3_COMMAND = 'ffmpeg -i {}.m4a -b:a 192K -vn {}.{}'
TMP_FOLDER = '/tmp'

args = sys.argv[1:]
print('args: {}'.format(args))
if args:
    os.system(YOUTUBE_DL_COMMAND.format(args[0]))
res = [f for f in os.listdir('.') if '.m4' in f]
print('the result is {}'.format(res))
for item in res:
    tmp_item = item.split('.')[0]
    print('tmp item is: {}'.format(tmp_item))
    os.system(M4A_TO_MP3_COMMAND.format(tmp_item, tmp_item, AUDIO_FORMAT))
    mp3_file = '{}.{}'.format(tmp_item, AUDIO_FORMAT)
    destination_of_mp3_file = os.path.join(YOUTUBE_LIBRARY_LOCATION, mp3_file)
    if os.path.isfile(destination_of_mp3_file):
        print(('WARNING! File with name: {} already exists at: {}.'
              ' Original file is moved to {}. Overwriting...'
              '').format(mp3_name, YOUTUBE_LIBRARY_LOCATION, TMP_FOLDER))
        shutil.move(mp3_file, TMP_FOLDER)
    shutil.move(mp3_file,
                YOUTUBE_LIBRARY_LOCATION)
    os.remove(item)


