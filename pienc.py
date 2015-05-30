from encoding.encoder import encode
from encoding.decoder import decode

import sys
import time
import os

def timer(func):

	def wrapper(*arg):
		t = time.time()
		res = func(*arg)
		print("--- %s seconds ---" % (time.time() - t))
		return res

	return wrapper

@timer
def run():
	args = sys.argv
	args.pop(0)
	if len(args) < 2 or len(args) > 3:
		print("USAGE: pienc [action] [filename] {output_file}")
	else:
		action = args[0]
		infile = args[1]

		if len(args) == 3:
			outfile = args[2]
		else:
			outfile = ""


		if action == 'e':
			encode(infile, outfile)

		elif action == 'd':
			decode(infile, outfile)

run()