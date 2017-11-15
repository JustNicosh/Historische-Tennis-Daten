#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# mechanize only works in python2

from mechanize import Browser
from base64 import b64encode

class AdminHandler():
	"""Handles GS-Admin interaction.
	"""

	def __init__(self):
		self.headers = [('User-agent', 'Firefox')]
		self.gsUsername = 'redaktion'
		self.gsPassword = 'pst2rglr23'
		self.endstandUrl = 'http://sport1_admin.app.endstand.de'
		self.ergebnisDienstUrl = 'http://master.dynamic.ergebnis-dienst.de'

	def return_admin_url(self, target):
		"""Returns GS-Admin url (ergebnis-dienst or endstand).
		"""
		if target == 'ergebnisDienst':
			targetUrl = self.ergebnisDienstUrl
		else:
			targetUrl = self.endstandUrl
		return targetUrl

	def return_gs_admin_content(self, url):
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
