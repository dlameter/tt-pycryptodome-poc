from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


# KEYGEN

private_key = RSA.generate(2048)
public_key = private_key.publickey()

contents = ""
with open('test.txt', 'r') as in_file:
	contents = in_file.read();


# ENCRYPT

encrypter = PKCS1_OAEP.new(public_key)
encrypted = encrypter.encrypt(contents)

with open('test.txt.encrypted', 'w') as encrypted_file:
	encrypted_file.write(encrypted[0])


# DECRYPT

decrypter = PKCS1_OAEP.new(private_key)
decrypted = decrypter.decrypt(encrypted)

with open('test.txt.decrypted', 'w') as decrypted_file:
	decrypted_file.write(decrypted)


