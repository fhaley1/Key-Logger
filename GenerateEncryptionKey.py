from cryptography.fernet import Fernet

# Generates an ecryption key and saves it to encryption_key.txt
key = Fernet.generate_key()
file = open("encryption_key.txt", 'wb')
file.write(key)
file.close()
