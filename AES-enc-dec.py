from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

block_size = 16


# ENCRYPT

iv = Random.new().read(block_size)
hashbrown = SHA256.new()
hashbrown.update("terry t-bone")
cipher = AES.new(hashbrown.digest(), AES.MODE_CBC, iv)

contents = ''
with open('test.txt', 'r') as in_file:
	contents = in_file.read()

padded = contents + (block_size - (len(contents) % block_size)) * ' ' 
encrypted = iv + cipher.encrypt(padded)

with open('test.txt.encrypted', 'w') as enc_file:
	enc_file.write(encrypted)


# DECRYPT

iv = encrypted[:block_size]
cipher = AES.new(hashbrown.digest(), AES.MODE_CBC, iv)
decrypted = cipher.decrypt(encrypted[block_size:])

with open('test.txt.decrypted', 'w') as dec_file:
	dec_file.write(decrypted)
