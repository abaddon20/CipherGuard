from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)


message_original = b"Este es un mensaje secreto."


message_cipher = cipher.encrypt(message_original)
print("message cipher:", message_cipher)


message_decrypted = cipher.decrypt(message_cipher).decode()
print("message decrypted:", message_decrypted)