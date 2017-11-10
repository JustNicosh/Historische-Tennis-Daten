#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# mechanize only works in python2

import seasons_creator
import os
import unittest
import csv_handler

class TestSeasonsCreator(unittest.TestCase):
	"""Unittests for the class SeasonsCreator.
	"""

	def test_return_gs_admin_content(self):
		"""Does the function return the requestet GS-Admin content?
        """
		br = seasons_creator.SeasonsCreator().return_gs_admin_content('http://sport1_admin.app.endstand.de/admin/season.php?sport_id=5&competition_id=858&season_id=&k=2')
		br.form = list(br.forms())[0]
		formToCheck = br.form.find_control('req[competition_id]')
		br.close()
		self.assertGreater(len(formToCheck.value), 0)

	def test_return_admin_url(self):
		"""Does the function return the right Admin Url?
        """
		self.assertEqual(seasons_creator.SeasonsCreator().return_admin_url(''), 'http://sport1_admin.app.endstand.de')
		self.assertEqual(seasons_creator.SeasonsCreator().return_admin_url('ergebnisDienst'), 'http://master.dynamic.ergebnis-dienst.de')

	def test_return_new_season_id(self):
		"""Does the function identify the season_id by year?
        """
		br = seasons_creator.SeasonsCreator().return_gs_admin_content('http://sport1_admin.app.endstand.de/admin/season.php?sport_id=5&competition_id=858&season_id=936')
		self.assertEqual(seasons_creator.SeasonsCreator().return_new_season_id(br, '2009'), '936')
		br.close()

	def test_import_season(self):
		"""Does the function import the season and return the season_id?
        """
		# Test data:
		row = ['Australian Open','2010-580','R64','119','858','20.01.2010-27.01.2010','ATP','2010','2. Runde']
		adminUrl = 'http://sport1_admin.app.endstand.de'
		self.assertEqual(seasons_creator.SeasonsCreator().import_season(row, adminUrl), '1931')

	def test_import_seasons(self):
		"""Does the function import all seasons and return a list containig season_ids  (known data -> 2193 and 10)?
		"""
		self.assertEqual(len(seasons_creator.SeasonsCreator().import_seasons('')), 2193)
		self.assertEqual(len(seasons_creator.SeasonsCreator().import_seasons('')[0]), 10)
		self.assertEqual(len(seasons_creator.SeasonsCreator().import_seasons('')[1000]), 10)

	def test_write_csv(self):
		"""Do we write one csv file with different rounds (known data -> 2193)?
        """
		path = seasons_creator.SeasonsCreator().write_csv('', '../data/test_allRoundsWithSeasonIds.csv')
		csvContent = csv_handler.CsvHandler().read_csv(path, 'r', 'latin-1', ',', '|', '2')
		os.remove('../data/test_allRoundsWithSeasonIds.csv')
		self.assertEqual(len(csvContent), 2193)
			
if __name__ == '__main__':
	os.system('radon cc -a seasons_creator.py')
	print('')
	unittest.main()
