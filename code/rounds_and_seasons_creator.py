#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# mechanize only works in python2

import csv_handler
from mechanize import Browser
from base64 import b64encode

class RoundsAndSeasonsCreator():
	"""Creates Rounds And Seasons.
	"""

	def __init__(self):
		self.headers = [('User-agent', 'Firefox')]
		self.gsUsername = 'redaktion'
		self.gsPassword = 'pst2rglr23'

	def returnGsAdminContent(self, url):
		"""Returns GS-Admin response data.
		"""
		br = Browser()
		br.set_handle_robots(False)
		br.addheaders = self.headers
		b64login = b64encode('%s:%s' % (self.gsUsername, self.gsPassword))
		br.addheaders.append(('Authorization', 'Basic %s' % b64login, ))
		br.open(url)
		try:
			return br
		except:
			print 'Error: Could not open ' + url


if __name__ == '__main__':
	RoundsAndSeasonsCreator().dev()
