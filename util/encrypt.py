from cryptography.fernet import Fernet

# 生成密钥
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# 加密密码
original_password = "test"
encrypted_password = cipher_suite.encrypt(original_password.encode())

print(f"Encryption Key: {key.decode()}")
print(f"Encrypted Password: {encrypted_password.decode()}")
print(f"Decrypted Password: {cipher_suite.decrypt(encrypted_password).decode()} ")
