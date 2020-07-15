import re
import sys
import urllib
from imgur_downloader import ImgurDownloader
# https://pypi.org/project/imgur-downloader/

albums = ['https://imgur.com/a/h7ZJ2\n', 'https://imgur.com/a/ixPK4\n', 'https://imgur.com/a/h2v5w\n', 'https://imgur.com/a/GWDGS\n',
          'https://imgur.com/a/riD8a\n', 'http://imgur.com/a/vpSiG\n', 'https://imgur.com/a/1dxLi\n', 'https://imgur.com/a/g8bwe\n', 'https://imgur.com/a/tAGDE\n']

hash_db = []

for album in albums:
    # album = urllib.parse.urlparse(album.rstrip())
    downloader = ImgurDownloader(album.rstrip())
    downloader.save_images()
