import re
import sys
import urllib
from imgur_downloader import ImgurDownloader
# https://pypi.org/project/imgur-downloader/

albums = ['https://imgur.com/a/qiQ7Dg8\n', 'https://imgur.com/a/VsH5hIv\n', 'https://imgur.com/a/1sVNZEM\n', 'https://imgur.com/a/Shjhkcq\n', 'https://imgur.com/a/1TagtLS\n', 'https://imgur.com/a/I8keYeh\n', 'https://imgur.com/a/KeAY0jh\n', 'https://imgur.com/a/I8keYeh\n'
          ]

hash_db = []

for album in albums:
    # album = urllib.parse.urlparse(album.rstrip())
    downloader = ImgurDownloader(album.rstrip())
    downloader.save_images()
