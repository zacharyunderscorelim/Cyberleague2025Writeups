Find python code in the network bytes of a http response
find a decryption function:
```
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
```
- Notice that theres a lot of packets which just send empty txt files
- export all packets to json
- ctrl F dns.txt.length": "0"
- cycle dns txt length until i find something
- base64 strings found at lengths 4, 8, 12, 20
- last base64 string is cat /root/flag
Hence, the flag must be in a response to this packet
- go back to wireshark and find that packet
- response is right after that packet with result being base64 string ```ECwydiAfdiIyJ3YrIhIRLm8lBVNMVCMqA0cdPVgQKkoKZCUZFT9DOAFEUFw=```
- pass it through the decryption function found earlier
CYBERLEAGUE{baby_warmup_stonks_894ejfhsjeeq}