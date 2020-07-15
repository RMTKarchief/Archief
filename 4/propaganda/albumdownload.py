import re
import sys
import urllib
from imgur_downloader import ImgurDownloader
# https://pypi.org/project/imgur-downloader/

albums = ['http://imgur.com/a/rY4Bx\n', 'http://imgur.com/a/dyD5p\n', 'http://imgur.com/a/5kO8r\n', 'http://imgur.com/a/8Keqm\n',
          'https://imgur.com/a/ArQwm\n', 'http://imgur.com/a/LFJnA\n', 'http://imgur.com/a/ieCMP\n', 'http://imgur.com/a/yIgN7\n']

hash_db = []

for album in albums:
    # album = urllib.parse.urlparse(album.rstrip())
    downloader = ImgurDownloader(album.rstrip())
    downloader.save_images()
