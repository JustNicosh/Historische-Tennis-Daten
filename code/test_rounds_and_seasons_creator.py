#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import rounds_and_seasons_creator
import os
import unittest
import csv_handler

class TestRoundsAndSeasonsCreator(unittest.TestCase):
	"""Unittests for the class RoundsAndSeasonsCreator.
	"""

	def test_returnGsAdminContent(self):
		"""Does the function return the requestet GS-Admin content?
        """
		br = rounds_and_seasons_creator.RoundsAndSeasonsCreator().returnGsAdminContent('http://sport1_admin.app.endstand.de/admin/season.php?sport_id=5&competition_id=858&season_id=&k=2')
		br.form = list(br.forms())[0]
		formToCheck = br.form.find_control('req[competition_id]')
		br.close()
		self.assertGreater(len(formToCheck.value), 0)
		

if __name__ == '__main__':
	os.system('radon cc -a rounds_and_seasons_creator.py')
	print('')
	unittest.main()