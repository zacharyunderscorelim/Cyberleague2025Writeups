#Challenge: Matroyshka 2

import pyzipper
import os

output_dir = 'C:/Users/Zachary/Desktop/ctf/cyberleague2025/unzips2/'
input_root = 'C:/Users/Zachary/Desktop/ctf/cyberleague2025/unzips2'
input_path = input_root + '/maxime'

'''
zip_ref = pyzipper.AESZipFile(input_path)
pwdlist = zip_ref.namelist()
zip_ref.extractall(output_dir, pwd=bytes(pwdlist[0], 'utf-8'))
'''

idx = 0

while True:
    with pyzipper.AESZipFile(input_path) as zf:
        pwdlist = zf.namelist()
        zf.extractall(output_dir, pwd=bytes(pwdlist[0], 'utf-8'))
    os.rename(os.path.join(output_dir, pwdlist[0]), os.path.join(output_dir, f'{idx}'))
    input_path = os.path.join(output_dir, f'{idx}')
    print(input_path)
    if idx > 1000:
        break
    idx += 1