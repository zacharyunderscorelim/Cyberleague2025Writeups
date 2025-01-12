#Challenge: Matroyshka

import os
import gzip
import lzma
import bz2
import magic

output_dir = 'C:/Users/Zachary/Desktop/ctf/cyberleague2025/unzips'
input_path = 'C:/Users/Zachary/Desktop/ctf/cyberleague2025/unzips/matryoshka'


idx = 0
while os.path.exists(input_path):
    with open(input_path, 'rb') as f:
        type = magic.from_file(input_path)
        print(type)
        if "XZ" in type:
            decompressed = lzma.decompress(f.read())
        elif "gzip" in type:
            decompressed = gzip.decompress(f.read())
        else:
            decompressed = bz2.decompress(f.read())

        with open(os.path.join(output_dir, f'matryoshka{idx}'), 'wb') as f:
            f.write(decompressed)
    input_path = os.path.join(output_dir, f'matryoshka{idx}')
    print(input_path)
    if idx > 1000:
        break
    idx += 1
