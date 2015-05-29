from key import Key
from reader import FileReader

def encode(file_path, out_path):

	print("Generating array from encryption key...")
	encryption_key = Key('data/pi.dat')

	CHUNK_SIZE = 1

	print("Reading file to encrypt...")
	file_reader = FileReader(file_path)

	print("Encrypting file...")
	pointer_array = []
	#  map(encryption_key.get_index, list(file_reader.read(CHUNK_SIZE)))
	counter = 0
	data_list = list(file_reader.read(CHUNK_SIZE))
	max_length = len(data_list)

	for item in data_list:

		pointer_array.append(encryption_key.get_index(item))

		if counter % 10 == 0:
			print("{0}/{1}".format(counter, max_length))
		counter += 1

	print("Dumping encrypted file...")
	with open(out_path, 'a') as outfile:
		outfile.write(','.join(pointer_array))
