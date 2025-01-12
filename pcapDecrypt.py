import base64


def encrypt_decrypt(data, key="Sup3rS3cur3P@ssW0Rd!!!", encrypt = True):
    key_length = len(key)
    if isinstance(data, str):
        data = data.encode()
    result = bytes(b ^ ord(key[i % key_length]) for i, b in enumerate(data))
    if encrypt:
        return base64.b64encode(result).decode('utf-8')
    else:
        decoded_data = base64.b64decode(data)
        decrypted_result = bytes(
            b ^ ord(key[i % key_length]) for i, b in enumerate(decoded_data))
        return decrypted_result.decode('utf-8', errors='ignore')

print(encrypt_decrypt("ECwydiAfdiIyJ3YrIhIRLm8lBVNMVCMqA0cdPVgQKkoKZCUZFT9DOAFEUFw=", "Sup3rS3cur3P@ssW0Rd!!!", False))
