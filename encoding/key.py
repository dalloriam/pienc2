import math
from search import boyermoore
from encoding import cache
import pi

class Key(object):

	def __init__(self, filename):
		self.filename = filename
		self.raw_data = pi.key

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