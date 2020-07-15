import re
import sys
import urllib
from imgur_downloader import ImgurDownloader
# https://pypi.org/project/imgur-downloader/

albums = ['https://imgur.com/a/AeyUSiX\n', 'https://imgur.com/a/Or3uzAn\n']

hash_db = []

for album in albums:
    # album = urllib.parse.urlparse(album.rstrip())
    downloader = ImgurDownloader(album.rstrip())
    downloader.save_images()
