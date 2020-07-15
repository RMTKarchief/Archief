import re
import sys
import urllib
from imgur_downloader import ImgurDownloader
# https://pypi.org/project/imgur-downloader/

albums = ['https://imgur.com/a/YhZPo\n', 'https://imgur.com/a/3uGzo\n', 'https://imgur.com/a/rNIcJ\n', 'https://imgur.com/a/guFj8\n',
          'https://imgur.com/a/sOVaG\n', 'https://imgur.com/a/h97Nk\n', 'https://imgur.com/a/jNS1h\n', 'https://imgur.com/a/MrH8z\n']

hash_db = []

for album in albums:
    # album = urllib.parse.urlparse(album.rstrip())
    downloader = ImgurDownloader(album.rstrip())
    downloader.save_images()
