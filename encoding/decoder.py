from key import Key
import base64
import os

def decode(file_path, out_path):

	if out_path == "":
		out_path = file_path.replace('.pi', '')

	print("Generating array from encryption key...")
	encryption_key = Key('data/pi.dat')

	CHUNK_SIZE = 1

	print("Reading file to decrypt...")
	with open(file_path, 'rb') as infile:
		indexes = infile.read().split(',')

	print("Decrypting file...")
	pointer_array =  map(encryption_key.get_data, indexes)

	print("Dumping decrypted file...")
	with open(out_path, 'a') as outfile:

		b64string = ''.join(map(chr, pointer_array))

		missing_padding = 4 - len(b64string) % 4
		if missing_padding:
			b64string += b'='* missing_padding

		outfile.write(base64.decodestring(b64string))

	os.remove('cache.db')