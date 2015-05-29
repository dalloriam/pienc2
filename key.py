import math
from search import boyermoore

class Key(object):

	def __init__(self, filename):
		self.filename = filename
		print self.filename
		with open(self.filename, 'rb') as datafile:
			self.raw_data = datafile.read()

		counter = 0


	def get_index(self, data):

		index = boyermoore.find(data, ''.join(self.raw_data))

		if  index != False:
			return str(index)

		return False

	def get_data(self, index):
		index = int(index)
		print index
		return int(self.raw_data[index:index+3])