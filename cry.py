import six, base64

def decode(key, string):
    string = base64.urlsafe_b64decode(string + b'===')
    string = string.decode('latin') if six.PY3 else string
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string

def get(passphrase):
  return decode(passphrase, 's9jIlqVlZGdR'.encode('ASCII'))

if __name__ == "__main__":
    p = input("Clave?\n\n>> ")
    print(get(p))