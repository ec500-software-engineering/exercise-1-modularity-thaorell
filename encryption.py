from cryptography.fernet import Fernet

def generate_key(p_id):
    filename = str(p_id) + ".key"
    # A function to generate random keys for users 
    key = Fernet.generate_key()
    file = open(filename, 'wb')
    file.write(key) # The key is type bytes still
    file.close()
    return key


def encrypt(data, key):
    # Encrypt anything
    print(data)
    message = str(data).encode()
    f = Fernet(key)
    encrypted = f.encrypt(message)
    # file = open('private.dat', 'wb')
    # file.write(encrypted) # The key is type bytes still
    # file.close()
    return encrypted
