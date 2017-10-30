#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import profiles_and_competitions_synchronizer
import os
import unittest
import csv_handler

class TestProfilesAndCompetitionsSynchronizer(unittest.TestCase):
	"""Unittests for the class ProfilesAndCompetitionsSynchronizer.
	"""

	def test_return_profiles_and_matches(self):
		"""Do both csvs return content (known data -> 3653 and 39681)?
        """
       	# Known data:
		self.assertEqual(len(profiles_and_competitions_synchronizer.ProfilesAndCompetitionsSynchronizer().return_profiles_and_matches()['profiles']), 3653)
		self.assertEqual(len(profiles_and_competitions_synchronizer.ProfilesAndCompetitionsSynchronizer().return_profiles_and_matches()['matches']), 39681)

	def test_check_if_competition_is_present(self):
		"""Does the function append only different competitions?
		"""
		# Test data set:
		competitions = ['1950_TURNIER-SUPERCOOL']
		match1 = ['1950-Bla', 'TURNIER-SUPERCOOL']
		match2 = ['1950-Bla', 'TURNIER-UNCOOL']
		self.assertEqual(len(profiles_and_competitions_synchronizer.ProfilesAndCompetitionsSynchronizer().check_if_competition_is_present(match1, competitions)), 1)
		self.assertEqual(len(profiles_and_competitions_synchronizer.ProfilesAndCompetitionsSynchronizer().check_if_competition_is_present(match2, competitions)), 2)

	def test_return_all_competitions_for_one_profile(self):
		"""Does the function append all different competitions?
        """
		# Test data set:
		profile = ['id_w_1', '', 'winner']
		matches = [ \
			['1950','TURNIER_SUPERCOOL','2','3','4','5','6','id_w_1','8','9','winner_1','11','12','13','14','15','16','id_l_1','18','19','loser_1'], \
			['1950','TURNIER_SUPERCOOL','2','3','4','5','6','id_w_1','8','9','winner_1','11','12','13','14','15','16','id_l_2','18','19','loser_2'], \
			['1950','TURNIER_UNCOOL','2','3','4','5','6','id_w_1','8','9','winner_1','11','12','13','14','15','16','id_l_3','18','19','loser_3'], \
			['1951','TURNIER_SUPERCOOL','2','3','4','5','6','id_w_1','8','9','winner_1','11','12','13','14','15','16','id_l_1','18','19','loser_1'], \
			['1951','TURNIER_UNCOOL','2','3','4','5','6','id_l_1','8','9','loser_1','11','12','13','14','15','16','id_w_1','18','19','winner_1'], \
			['1951','TURNIER_UNCOOL','2','3','4','5','6','id_w_1','8','9','winner_1','11','12','13','14','15','16','id_l_2','18','19','loser_2'] \
			]
		self.assertEqual(len(profiles_and_competitions_synchronizer.ProfilesAndCompetitionsSynchronizer().return_all_competitions_for_one_profile(profile, matches)), 4)

	def test_return_profiles_with_competitons_list(self):
		"""Do all profiles contain a competition list with at least one item (known data -> 3653)?
        """
		profileWithCompetitionsList = profiles_and_competitions_synchronizer.ProfilesAndCompetitionsSynchronizer().return_profiles_with_competitons_list()
		self.assertEqual(len(profileWithCompetitionsList), 3653)
		for profile in profileWithCompetitionsList:
			self.assertGreater(len(profile[7]), 0)

	def test_write_csv(self):
		"""Do we write one csv file with competition profile rows (known data -> 3653)?
        """
		path = profiles_and_competitions_synchronizer.ProfilesAndCompetitionsSynchronizer().write_csv('../data/test_allProfilesWithCompetitions.csv')
		csvContent = csv_handler.CsvHandler().read_csv(path, 'r', 'latin-1')
		os.remove('../data/test_allProfilesWithCompetitions.csv')
		self.assertEqual(len(csvContent), 3653)

if __name__ == '__main__':
	os.system('radon cc -a profiles_and_competitions_synchronizer.py')
	print('')
	unittest.main()
