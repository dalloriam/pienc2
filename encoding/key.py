import math
from search import boyermoore
from encoding import cache

class Key(object):

	def __init__(self, filename):
		self.filename = filename
		print self.filename

		with open(self.filename, 'rb') as datafile:
			self.raw_data = datafile.read()

		self.cache = cache.Cache()


	def get_index(self, data):

		db_check = self.cache.read(data)

		if db_check == False:

			index = boyermoore.find(data, ''.join(self.raw_data))

			if  index != False:
				self.cache.write(data, index)
				return str(index)

			return False

		else:
			return db_check

	def get_data(self, index):
		index = int(index)
		return int(self.raw_data[index:index+3])