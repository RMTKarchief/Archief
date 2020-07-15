import re
import sys
import urllib
import hashlib
from urllib import request

print('Begint met het downloaden van:\n')
hash_db = []
for line in open(sys.argv[1], "r"):
    if not re.search(sys.argv[2], line):
        o = urllib.parse.urlparse(line.rstrip())

        if o.path.split('/')[-1]:
            try:
                with request.urlopen(o.geturl()) as r:
                    data = r.read()

                    print(o.geturl())

                    hash = hashlib.sha1(data).hexdigest()

                    if hash not in hash_db:
                        with open(o.path.split('/')[-1], "wb") as f:
                            f.write(data)
                            f.close()
                        hash_db.append(hash)
                    else:
                        print('Poah! Deze is dubbel!')
            except urllib.error.HTTPError as e:
                continue

print('Klaar!')
