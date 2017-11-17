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

	def test_return_profile_data(self):
		"""Does the function return the expected information?
		"""
		profile = ['110066','Allen','Quay','R','19460616','USA','atp','0','25330']
		outputToCheck = persons_and_teams_creator.PersonsAndTeamsCreator().return_profile_data(profile)
		self.assertEqual(outputToCheck['preName'], 'Allen')
		self.assertEqual(outputToCheck['lastName'], 'Quay')
		self.assertEqual(outputToCheck['country'], 'USA')
		self.assertEqual(outputToCheck['gender'], 'atp')
		self.assertEqual(outputToCheck['birthDay'], '16')
		self.assertEqual(outputToCheck['birthMonth'], '06')
		self.assertEqual(outputToCheck['birthYear'], '1946')

	def test_create_new_person(self):
		"""Does the function create a new person and return the person_id and all depending season_ids?
		"""
		profile = ['110066','Vorname','Nachname','R','19990115','GER','wta','0','25330_99999']
		adminUrl = admin_handler.AdminHandler().return_admin_url('')
		outputToCheck = persons_and_teams_creator.PersonsAndTeamsCreator().create_new_person(profile, adminUrl)
		self.assertGreater(int(outputToCheck['personId']), 0)

	def test_create_new_person_and_team(self):
		"""Does the function create a new team, add the depending person and return the new team_id?
		"""
		profile = ['110066','Neuer','Super Typ','R','19990115','AUT','wta','0','25330_99999']
		adminUrl = admin_handler.AdminHandler().return_admin_url('')
		outputToCheck = persons_and_teams_creator.PersonsAndTeamsCreator().create_new_person_and_team(profile, adminUrl)
		self.assertGreater(int(outputToCheck), 0)

	def test_add_seasons(self):
		"""Does the function add all relevant seasons to one player profile?
		"""
		profile = ['110066','Neuer','Super Typ','R','19990115','AUT','wta','137235','19946_8109_1954']
		adminUrl = admin_handler.AdminHandler().return_admin_url('')
		outputToCheck = persons_and_teams_creator.PersonsAndTeamsCreator().add_seasons(profile, adminUrl)
		self.assertEqual(outputToCheck, profile)

	def test_return_all_profiles_with_team_ids(self):
		"""Does the function return a list containing all modified profiles with team_ids?
		"""
		outputToCheck = persons_and_teams_creator.PersonsAndTeamsCreator().return_all_profiles_with_team_ids('')
		self.assertEqual(len(outputToCheck), 1)
		self.assertNotEqual(outputToCheck[0][7], '0')

	def test_write_csv(self):
		"""Do we write one csv file with all different modified profiles containing team_ids?
        """
		path = persons_and_teams_creator.PersonsAndTeamsCreator().write_csv('', '../data/test_everyProfileWithTeamId.csv')
		csvContent = csv_handler.CsvHandler().read_csv(path, 'r', 'latin-1', ',', '|', '2')
		os.remove('../data/test_everyProfileWithTeamId.csv')
		self.assertEqual(len(csvContent), 1)
		
if __name__ == '__main__':
	os.system('radon cc -a persons_and_teams_creator.py')
	print('')
	unittest.main()
