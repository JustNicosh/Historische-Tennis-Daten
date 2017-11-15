#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# mechanize only works in python2

import persons_and_teams_creator
import os
import unittest
import csv_handler
import admin_handler

class TestPersonsAndTeamsCreator(unittest.TestCase):
	"""Unittests for the class PersonsAndTeamsCreator.
	"""

	#def test_write_csv(self):
		"""Do we write one csv file with different rounds (known data -> 2193)?
        """
		#path = persons_and_teams_creator.PersonsAndTeamsCreator().write_csv('', '../data/test_allRoundsWithSeasonIds.csv')
		#csvContent = csv_handler.CsvHandler().read_csv(path, 'r', 'latin-1', ',', '|', '2')
		#os.remove('../data/test_allRoundsWithSeasonIds.csv')
		#self.assertEqual(len(csvContent), 2193)
			
if __name__ == '__main__':
	os.system('radon cc -a persons_and_teams_creator.py')
	print('')
	unittest.main()
