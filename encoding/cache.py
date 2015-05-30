import sqlite3
import os
class Cache(object):

	def __init__(self, size = 10):

		self.size = size

		self.con = sqlite3.connect('cache.db')

		self.cur = self.con.cursor()

		self.cur.execute("CREATE TABLE IF NOT EXISTS Cache (data TEXT, indx INT, usecount INT) ")

	def read(self, data):

		self.cur.execute("SELECT * FROM Cache WHERE data=?",(data,))
		row = self.cur.fetchone()

		if row == None:
			return False
		else:
			index = row[1]
			usecount = row[2]
			self.cur.execute("UPDATE Cache SET usecount=? WHERE data=?",(usecount+1, data))
			return str(index)

	def write(self, value, index):

		self.cur.execute("INSERT INTO Cache(data, indx, usecount) VALUES  (?, ?, 0)",(value, index))
		self.con.commit()
