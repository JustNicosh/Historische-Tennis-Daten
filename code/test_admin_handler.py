#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# mechanize only works in python2

import admin_handler
import os
import unittest
import csv_handler

class TestAdminHandler(unittest.TestCase):
	"""Unittests for the class AdminHandler.
	"""

	def test_return_admin_url(self):
		"""Does the function return the right Admin Url?
		"""
		self.assertEqual(admin_handler.AdminHandler().return_admin_url(''), 'http://sport1_admin.app.endstand.de')
		self.assertEqual(admin_handler.AdminHandler().return_admin_url('ergebnisDienst'), 'http://master.dynamic.ergebnis-dienst.de')

	def test_return_gs_admin_content(self):
		"""Does the function return the requestet GS-Admin content?
		"""
		brEndstand = admin_handler.AdminHandler().return_gs_admin_content('http://sport1_admin.app.endstand.de/admin/team.php?sport_id=5&k=2&team_id=')
		brErgebnis = admin_handler.AdminHandler().return_gs_admin_content('http://master.dynamic.ergebnis-dienst.de/admin/team.php?sport_id=5&k=2&team_id=')
		brEndstand.form = list(brEndstand.forms())[0]
		brErgebnis.form = list(brErgebnis.forms())[0]
		formToCheckEndstand = brEndstand.form.find_control('req[country_id]')
		formToCheckErgebnis = brErgebnis.form.find_control('req[country_id]')
		brEndstand.close()
		brErgebnis.close()
		self.assertGreater(len(formToCheckEndstand.value), 0)
		self.assertGreater(len(formToCheckErgebnis.value), 0)
			
if __name__ == '__main__':
	os.system('radon cc -a admin_handler.py')
	print('')
	unittest.main()
