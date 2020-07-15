import re
import sys
import urllib
from imgur_downloader import ImgurDownloader
# https://pypi.org/project/imgur-downloader/

albums = ['http://imgur.com/a/LoJuX\n', 'http://imgur.com/a/1N1CV\n', 'http://imgur.com/a/zbB2J\n', 'http://imgur.com/a/WiDC4\n', 'http://imgur.com/a/djDM4\n', 'https://imgur.com/a/fX8Np\n',
          'http://imgur.com/a/TJWBx\n', 'http://imgur.com/a/djDM4\n', 'http://imgur.com/a/ehLAM\n', 'http://imgur.com/a/BycIk\n', 'http://imgur.com/a/FYzPx\n', 'http://imgur.com/a/MfSpm\n', 'http://imgur.com/a/xg7Xi\n']

hash_db = []

for album in albums:
    # album = urllib.parse.urlparse(album.rstrip())
    downloader = ImgurDownloader(album.rstrip())
    downloader.save_images()
