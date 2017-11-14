#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# mechanize only works in python2

import rounds_creator
import os
import unittest
import csv_handler

class TestRoundsCreator(unittest.TestCase):
	"""Unittests for the class RoundsCreator.
	"""

	def test_return_gs_admin_content(self):
		"""Does the function return the requestet GS-Admin content?
        """
		br = rounds_creator.RoundsCreator().return_gs_admin_content('http://sport1_admin.app.endstand.de/admin/round.php?sport_id=5&competition_id=858&season_id=6618&round_id=&k=2')
		#br = rounds_creator.RoundsCreator().return_gs_admin_content('http://master.dynamic.ergebnis-dienst.de/admin/round.php?sport_id=5&competition_id=858&season_id=6618&round_id=&k=2')
		br.form = list(br.forms())[0]
		formToCheck = br.form.find_control('req[round_mode_id]')
		br.close()
		self.assertGreater(len(formToCheck.value), 0)

	def test_return_admin_url(self):
		"""Does the function return the right Admin Url?
        """
		self.assertEqual(rounds_creator.RoundsCreator().return_admin_url(''), 'http://sport1_admin.app.endstand.de')
		self.assertEqual(rounds_creator.RoundsCreator().return_admin_url('ergebnisDienst'), 'http://master.dynamic.ergebnis-dienst.de')

	def test_return_new_round_id(self):
		"""Does the function identify the round_id by year?
        """
		br = rounds_creator.RoundsCreator().return_gs_admin_content('http://sport1_admin.app.endstand.de/admin/round.php?sport_id=5&competition_id=858&season_id=7950')
		self.assertEqual(rounds_creator.RoundsCreator().return_new_round_id(br, '1. Runde'), '26398')
		br.close()

	def test_import_round(self):
		"""Does the function import the round and return the round_id?
        """
        # CAUTION: NEW DATA WILL BE WRITTEN INTO THE DB (THEREFORE WE NEED AN EXPECTED round_id)!
		# Test data:
		row = ['Australian Open','','','','858','','','','unbekannt','25172']
		adminUrl = 'http://sport1_admin.app.endstand.de'
		expectedRoundId = '78625'
		self.assertEqual(rounds_creator.RoundsCreator().import_round(row, adminUrl), expectedRoundId)

	def test_import_rounds(self):
		"""Does the function import all seasons and return a list containig season_ids  (known data -> 2193 and 11)?
		"""
		# CAUTION: A LOT OF NEW DATA WOULD BE WRITTEN INTO THE DB, THEREFORE test_write_csv REPLACES test_import_rounds!

	def test_write_csv(self):
		"""Do we write one csv file with different rounds (known data -> 2193 and 11)?
        """
        # CAUTION: NEW DATA WILL BE WRITTEN INTO THE DB!
		path = rounds_creator.RoundsCreator().write_csv('', '../data/test_allRoundsWithRoundIds.csv')
		csvContent = csv_handler.CsvHandler().read_csv(path, 'r', 'latin-1', ',', '|', '2')
		os.remove('../data/test_allRoundsWithRoundIds.csv')
		self.assertEqual(len(csvContent), 2193)
		self.assertEqual(len(csvContent[0]), 11)
		self.assertEqual(len(csvContent[1000]), 11)
			
if __name__ == '__main__':
	os.system('radon cc -a rounds_creator.py')
	print('')
	unittest.main()
