import gzip
import json

with gzip.open("data.json.gz", "rb") as f:
    data = json.loads(f.read().decode("ascii"))
#    print (data)
