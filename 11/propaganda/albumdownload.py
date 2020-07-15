import re
import sys
import urllib
from imgur_downloader import ImgurDownloader
# https://pypi.org/project/imgur-downloader/

albums = ['https://imgur.com/a/AeyUSiX\n', 'https://imgur.com/a/Or3uzAn\n', 'https://imgur.com/a/dNZpNh4\n', 'https://imgur.com/a/XUrI3ds\n', 'https://imgur.com/a/1uBFT43\n', 'https://imgur.com/a/6hzWMIT\n', 'https://imgur.com/a/X6gIevx\n', 'https://imgur.com/a/0x4ctWJ\n', 'https://imgur.com/a/gkYb9Fr\n', 'https://imgur.com/a/1JAVtxQ\n', 'https://imgur.com/a/CSKK3et\n', 'https://imgur.com/a/zxdVwV3\n', 'https://imgur.com/a/Ll5vqPK\n', 'https://imgur.com/a/1pm6EQk\n',
          'https://imgur.com/a/EqY5Dsu\n', 'https://imgur.com/a/uhtFvWh\n', 'https://imgur.com/a/mLaZA5x\n', 'https://imgur.com/a/Sy2I3oS\n', 'https://imgur.com/a/giWVWyp\n', 'https://imgur.com/a/aeraXj2\n', 'https://imgur.com/a/dvJWrQR\n', 'https://imgur.com/a/LFOVcKT\n', 'https://imgur.com/a/xh8qtNt\n', 'https://imgur.com/a/OCIasBU\n', 'https://imgur.com/a/6GEluWV\n', 'https://imgur.com/a/jv4ckxQ\n', 'https://imgur.com/a/Vj6714V\n', 'https://imgur.com/a/XoaflNn\n', 'https://imgur.com/a/fC82Qb6\n']

hash_db = []

for album in albums:
    # album = urllib.parse.urlparse(album.rstrip())
    downloader = ImgurDownloader(album.rstrip())
    downloader.save_images()
