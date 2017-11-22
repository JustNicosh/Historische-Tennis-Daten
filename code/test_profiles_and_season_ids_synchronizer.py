#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

import profiles_and_season_ids_synchronizer
import os
import unittest
import csv_handler

class TestProfilesAndSeasonIdsSynchronizer(unittest.TestCase):
	"""Unittests for the class ProfilesAndSeasonIdsSynchronizer.
	"""

	def test_return_profiles_and_seasons(self):
		"""Do both csvs return content (known data -> 2199 and 3782)?
		"""
		outputToCheck = profiles_and_season_ids_synchronizer.ProfilesAndSeasonIdsSynchronizer().return_profiles_and_seasons()
		self.assertEqual(len(outputToCheck['profiles']), 3782)
		self.assertEqual(len(outputToCheck['seasons']), 2199)

	def test_return_season_ids(self):
		"""Does the function return a string containing different season_ids?
		"""
		# Test data:
		profileSeasons = ['1968_US Open', '1968_Wimbledon']
		genderMale = 'atp'
		genderFemale = 'wta'
		seasons =  csv_handler.CsvHandler().read_csv('../data/allRoundsWithRoundIds.csv', 'r', 'latin-1')
		outputToCheckMale = profiles_and_season_ids_synchronizer.ProfilesAndSeasonIdsSynchronizer().return_season_ids(profileSeasons, seasons, genderMale)
		outputToCheckFemale = profiles_and_season_ids_synchronizer.ProfilesAndSeasonIdsSynchronizer().return_season_ids(profileSeasons, seasons, genderFemale)
		self.assertEqual(outputToCheckMale, '25330_25412')
		self.assertEqual(outputToCheckFemale, '25371_25453')

	def test_return_profiles_with_season_ids(self):
		"""Does the function return a list containing all profiles with season_ids (known data -> 3782 and 9)?
		"""
		outputToCheck = profiles_and_season_ids_synchronizer.ProfilesAndSeasonIdsSynchronizer().return_profiles_with_season_ids()
		self.assertEqual(len(outputToCheck), 3782)
		self.assertEqual(len(outputToCheck[0]), 9)
		self.assertEqual(len(outputToCheck[1000]), 9)
		self.assertEqual(len(outputToCheck[-1]), 9)

	def test_write_csv(self):
		"""Do we write one csv file with profile rows containing season_ids (known data -> 3782)?
        """
		path = profiles_and_season_ids_synchronizer.ProfilesAndSeasonIdsSynchronizer().write_csv('../data/test_allProfilesWithSeasonIds.csv')
		csvContent = csv_handler.CsvHandler().read_csv(path, 'r', 'latin-1')
		os.remove('../data/test_allProfilesWithSeasonIds.csv')
		self.assertEqual(len(csvContent), 3782)

if __name__ == '__main__':
	os.system('radon cc -a profiles_and_season_ids_synchronizer.py')
	print('')
	unittest.main()
