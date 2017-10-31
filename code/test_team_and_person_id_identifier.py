#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import team_and_person_id_identifier
import os
import unittest
import csv_handler

class TestTeamAndPersonIdIdentifier(unittest.TestCase):
	"""Unittests for the class TestTeamAndPersonIdIdentifier.
	"""

	def test_return_profiles_teams_and_persons(self):
		"""Do all csvs return content (case known data -> 3653)?
        """
		outputToCheck = team_and_person_id_identifier.TeamAndPersonIdIdentifier().return_profiles_teams_and_persons()
		self.assertEqual(len(outputToCheck['profiles']), 3653)
		self.assertGreater(len(outputToCheck['hsTeams']), 10000)
		self.assertGreater(len(outputToCheck['hsPersons']), 10000)

	def test_identify_team_id(self):
		"""Do we identify the depending team?
		"""
		# Test data:

		# ACHTUNG -> team-Tabelle (hs-db) wurde zwar im utf-8-Format exportiert, aber
		# UMLAUTE stellen ein Problem dar (201504,Julia,Goerges VS "39494","Julia","Görges","Julia Görges")

		profile1 = ['100087','John','Newcombe','R','19440523','AUS','atp','1968_US Open++1968_Wimbledon']
		profile2 = ['100087','Julia','Goerges','R','19440523','AUS','atp','1968_US Open++1968_Wimbledon']
		hsTeams = [["123","Julia Görges","","","","club","male","1","47","11","1","yes","no","0","person","2015-05-30 16:57:00"], \
					["456","John Middlename Newcombe","","","FC ","club","male","1","217","49","1","yes","no","0","person","2017-07-26 07:54:45"]]
		self.assertEqual(team_and_person_id_identifier.TeamAndPersonIdIdentifier().identify_team_id(profile1, hsTeams), '456')
		self.assertEqual(team_and_person_id_identifier.TeamAndPersonIdIdentifier().identify_team_id(profile2, hsTeams), '123')

	def test_identify_person_id(self):
		"""Do we identify the depending person?
		"""
		# Test data:

		# ACHTUNG -> team-Tabelle (hs-db) wurde zwar im utf-8-Format exportiert, aber
		# UMLAUTE stellen ein Problem dar (201504,Julia,Goerges VS "39494","Julia","Görges","Julia Görges")

		profile1 = ['100087','John','Newcombe','R','19440523','AUS','atp','1968_US Open++1968_Wimbledon']
		profile2 = ['100087','Julia','Goerges','R','19440523','AUS','atp','1968_US Open++1968_Wimbledon']
		hsPersons = [["12","Julia","Görges","Julia Görges","male","1978-09-27","187","87","2013-06-10 14:39:10"], \
					["34","John","Newcombe","John Newcombe","male","1978-09-27","187","87","2013-06-10 14:39:10"]]
		self.assertEqual(team_and_person_id_identifier.TeamAndPersonIdIdentifier().identify_person_id(profile1, hsPersons), '34')
		self.assertEqual(team_and_person_id_identifier.TeamAndPersonIdIdentifier().identify_person_id(profile2, hsPersons), '12')

if __name__ == '__main__':
	os.system('radon cc -a team_and_person_id_identifier.py')
	print('')
	unittest.main()
