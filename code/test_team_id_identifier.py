#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import team_id_identifier
import os
import unittest
import csv_handler

class TestTeamIdIdentifier(unittest.TestCase):
	"""Unittests for the class TeamIdIdentifier.
	"""

	def test_return_profiles_and_teams(self):
		"""Do all csvs return content (known data -> 3781 and at least 4700)?
        """
		outputToCheck = team_id_identifier.TeamIdIdentifier().return_profiles_and_teams()
		self.assertEqual(len(outputToCheck['profiles']), 3781)
		self.assertGreater(len(outputToCheck['hsTeams']), 4700)

	def test_return_sports_specific_teams(self):
		"""Are only columns with the right sport_id and without a double marker returned?
		"""
		# Test data:
		hsTeams = [["456","Team1","","","FC ","club","male","1","217","49","5","yes","no","0","person","2017-07-26 07:54:45"], \
					["456","Team2","","","FC ","club","male","1","217","49","15","yes","no","0","person","2017-07-26 07:54:45"], \
					["456","Team3","","","FC ","club","male","1","217","49","5","yes","no","0","person","2017-07-26 07:54:45"], \
					["456","Team2 / Team3","","","FC ","club","male","1","217","49","5","yes","no","0","person","2017-07-26 07:54:45"]]
		self.assertEqual(len(team_id_identifier.TeamIdIdentifier().return_sports_specific_teams(hsTeams, '5', 1, 10)), 2)

	def test_identify_id(self):
		"""Do we identify the depending team?
		"""
		# Test data:
		teamProfile1 = ['100087','John','Newcombe','R','19440523','AUS','atp','1968_US Open++1968_Wimbledon']
		teamProfile2 = ['100087','Julia','Goerges','R','19440523','AUS','atp','1968_US Open++1968_Wimbledon']
		hsTeams = [["123","'Julia Görges'","","","","club","male","1","47","11","1","yes","no","0","person","2015-05-30 16:57:00"], \
					["456","'John Middlename Newcombe'","","","FC ","club","male","1","217","49","1","yes","no","0","person","2017-07-26 07:54:45"]]
		self.assertEqual(team_id_identifier.TeamIdIdentifier().identify_id(teamProfile1, hsTeams, 1, 0), '456')
		self.assertEqual(team_id_identifier.TeamIdIdentifier().identify_id(teamProfile2, hsTeams, 1, 0), '123')

	def test_return_profiles_with_team_id(self):
		"""Are all profiles returned and many with a team_id (known data -> 3781 and at least 900)?
		"""
		outputToCheck = team_id_identifier.TeamIdIdentifier().return_profiles_with_team_id()
		self.assertEqual(len(outputToCheck), 3781)
		teamIds = 0
		for row in outputToCheck:
			if row[8] != '0':
				teamIds += 1
		self.assertGreater(teamIds, 900)

	def test_write_csv(self):
		"""Do we write one csv file with team_id profile rows (known data -> 3781)?
        """
		path = team_id_identifier.TeamIdIdentifier().write_csv('../data/test_allProfilesWithTeamIds.csv')
		csvContent = csv_handler.CsvHandler().read_csv(path, 'r', 'latin-1')
		os.remove('../data/test_allProfilesWithTeamIds.csv')
		self.assertEqual(len(csvContent), 3781)

if __name__ == '__main__':
	os.system('radon cc -a team_id_identifier.py')
	print('')
	unittest.main()
