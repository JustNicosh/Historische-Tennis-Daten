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
		self.assertEqual(outputToCheck['seasonIds'], '25330')

	def test_create_new_person(self):
		"""Does the function create a new person and return the person_id and all depending season_ids?
		"""
		# CAUTION: NEW DATA WILL BE WRITTEN INTO THE DB (THEREFORE WE NEED AN EXPECTED person_id)!
		profile = ['110066','Vorname','Nachname','R','19990115','GER','wta','0','25330_99999']
		adminUrl = admin_handler.AdminHandler().return_admin_url('')
		outputToCheck = persons_and_teams_creator.PersonsAndTeamsCreator().create_new_person(profile, adminUrl)
		expectedPersonId = '521185'
		self.assertEqual(outputToCheck['personId'], expectedPersonId)
		self.assertEqual(outputToCheck['seasonIds'], '25330_99999')

	def test_return_all_profiles_with_team_ids(self):
		"""Does the function return a list containing all profiles with team_ids?
		"""
		outputToCheck = persons_and_teams_creator.PersonsAndTeamsCreator().return_all_profiles_with_team_ids('')
		self.assertEqual(len(outputToCheck), 3782)
		self.assertNotEqual(outputToCheck[0][7], '0')
		self.assertNotEqual(outputToCheck[1000][7], '0')
		self.assertNotEqual(outputToCheck[-1][7], '0')

			
if __name__ == '__main__':
	os.system('radon cc -a persons_and_teams_creator.py')
	print('')
	unittest.main()
