from encoding.encoder import encode
from encoding.decoder import decode

import sys
import time

def timer(func):

	def wrapper(*arg):
		t = time.clock()
		res = func(*arg)
		print func.func_name, time.clock()-t
		return res

	return wrapper

@timer
def run():
	args = sys.argv
	args.pop(0)

	action = args[0]
	infile = args[1]
	outfile = args[2]

	if action == 'e':
		encode(infile, outfile)

	elif action == 'd':
		decode(infile, outfile)

run()