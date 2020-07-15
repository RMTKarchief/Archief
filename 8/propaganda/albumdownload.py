import re
import sys
import urllib
from imgur_downloader import ImgurDownloader
# https://pypi.org/project/imgur-downloader/

albums = ['https://imgur.com/a/my4By7K\n', 'https://imgur.com/a/xRZ5qsF\n', 'https://imgur.com/a/OnTOzMh\n', 'https://imgur.com/a/tZ196WI\n', 'https://imgur.com/a/EMURKEO\n',
          'https://imgur.com/a/kP9XcMG\n', 'https://imgur.com/a/h7gimCA\n', 'https://imgur.com/a/OtQWSaU\n', 'https://imgur.com/a/sv6RKtT\n', 'https://imgur.com/a/N1UqNEu\n', 'https://imgur.com/a/BKWhafN\n']

hash_db = []

for album in albums:
    # album = urllib.parse.urlparse(album.rstrip())
    downloader = ImgurDownloader(album.rstrip())
    downloader.save_images()
