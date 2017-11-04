#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import team_and_person_id_identifier
import os
import unittest
import csv_handler

class TestTeamAndPersonIdIdentifier(unittest.TestCase):
	"""Unittests for the class TestTeamAndPersonIdIdentifier.
	"""

	def test_return_profiles_and_teams(self):
		"""Do all csvs return content (case known data -> 3653)?
        """
		outputToCheck = team_and_person_id_identifier.TeamAndPersonIdIdentifier().return_profiles_and_teams()
		self.assertEqual(len(outputToCheck['profiles']), 3653)
		self.assertGreater(len(outputToCheck['hsTeams']), 5000)

	def test_return_sports_specific_teams(self):
		"""Are only columns with the right sport_id and without a double marker returned?
		"""
		# Test data:
		hsTeams = [["456","Team1","","","FC ","club","male","1","217","49","'5'","yes","no","0","person","2017-07-26 07:54:45"], \
					["456","Team2","","","FC ","club","male","1","217","49","'15'","yes","no","0","person","2017-07-26 07:54:45"], \
					["456","Team3","","","FC ","club","male","1","217","49","'5'","yes","no","0","person","2017-07-26 07:54:45"], \
					["456","Team2 / Team3","","","FC ","club","male","1","217","49","'5'","yes","no","0","person","2017-07-26 07:54:45"], \
					]
		self.assertEqual(len(team_and_person_id_identifier.TeamAndPersonIdIdentifier().return_sports_specific_teams(hsTeams, '5')), 2)

	def test_identify_id(self):
		"""Do we identify the depending team?
		"""
		# Test data:
		teamProfile1 = ['100087','John','Newcombe','R','19440523','AUS','atp','1968_US Open++1968_Wimbledon']
		teamProfile2 = ['100087','Julia','Goerges','R','19440523','AUS','atp','1968_US Open++1968_Wimbledon']
		hsTeams = [["123","Julia Görges","","","","club","male","1","47","11","1","yes","no","0","person","2015-05-30 16:57:00"], \
					["456","John Middlename Newcombe","","","FC ","club","male","1","217","49","1","yes","no","0","person","2017-07-26 07:54:45"]]
		self.assertEqual(team_and_person_id_identifier.TeamAndPersonIdIdentifier().identify_id(teamProfile1, hsTeams, 1), '456')
		self.assertEqual(team_and_person_id_identifier.TeamAndPersonIdIdentifier().identify_id(teamProfile2, hsTeams, 1), '123')

if __name__ == '__main__':
	os.system('radon cc -a team_and_person_id_identifier.py')
	print('')
	unittest.main()
