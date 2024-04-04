import urllib.request
import gzip


# with urllib.request.urlopen('https://www.python.org/') as f:
#     print(f.read(300))

with urllib.request.urlopen('https://www.python.org/') as f:
    data = f.read()
    try:
        print(data.decode('utf-8'))
    except UnicodeDecodeError:
        decompressed_data = gzip.decompress(data)
        print(decompressed_data.decode('utf-8')[:3000])