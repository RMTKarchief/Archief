import re
import sys
import urllib
from imgur_downloader import ImgurDownloader
# https://pypi.org/project/imgur-downloader/

albums = ['http://imgur.com/a/snwZ7\n', 'http://imgur.com/a/br8RD\n']

hash_db = []

for album in albums:
    # album = urllib.parse.urlparse(album.rstrip())
    downloader = ImgurDownloader(album.rstrip())
    downloader.save_images()
