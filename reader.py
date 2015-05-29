import base64

class FileReader(object):

	def __init__(self, file_path):

		with open(file_path, 'rb') as filedata:
			self.raw_data = base64.b64encode(filedata.read())
			self.raw_data = self.raw_data.replace("=", "")


	def sanitize(self, char):
		my_ord = ord(char)
		return str(my_ord).zfill(3)

	def read(self, chunk_size):

		for i in xrange(0, len(self.raw_data), chunk_size):
			yield ''.join(map(self.sanitize, self.raw_data[i:i+chunk_size]))