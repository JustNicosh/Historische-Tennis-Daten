#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

import matches_rounds_and_profiles_synchronizer
import os
import unittest
import csv_handler

class TestMatchesRoundsAndProfilesSynchronizer(unittest.TestCase):
	"""Unittests for the class MatchesRoundsAndProfilesSynchronizer.
	"""

	def test_return_csv_data(self):
		"""Do all three csvs return content (known data -> 45032, 3344 and 2199)?
        """
		outputToCheck = matches_rounds_and_profiles_synchronizer.MatchesRoundsAndProfilesSynchronizer().return_csv_data()
		self.assertEqual(len(outputToCheck['matches']), 45032)
		self.assertEqual(len(outputToCheck['profiles']), 3344)
		self.assertEqual(len(outputToCheck['rounds']), 2199)

	def test_return_team_id(self):
		"""Does the function return a team_id (identified by a sourceProfileId and the soureProfileName)?
		"""
		profiles = [['100087','John','Newcombe','R','19440523','AUS','atp','137337'],
					['110066','Allen','Quay','R','','USA','atp','137338'],
					['100023','Ramanathan','Krishnan','R','19370411','IND','atp','137339'],
					['109966','Warren','Jacques','R','19380310','AUS','atp','137340'],
					['109816','E Victor','Seixas','R','19230830','USA','atp','137341'],
					['100127','Tom','Gorman','R','19461219','USA','atp','137342'],
					['109932','Charles','Mckinley','R','19410105','USA','atp','137344']]
		sourceProfileId = '100023'
		soureProfileName = 'Ramanathan Krishnan'
		outputToCheck = matches_rounds_and_profiles_synchronizer.MatchesRoundsAndProfilesSynchronizer().return_team_id(profiles, sourceProfileId, soureProfileName)
		self.assertEqual(outputToCheck, '137339')

	def test_return_round_id(self):
		"""Does the function return a round_id (identified by the sourceYear, the sourceTourneyName and a sourceRoundId)?
		"""
		rounds = [['Australian Open','1969-580','R64','2218','858','20.01.1969-27.01.1969','ATP','1969','1. Runde','25171','78628'],
					['Australian Open','1969-580','R32','2218','858','20.01.1969-27.01.1969','ATP','1969','2. Runde','25171','78629'],
					['Australian Open','1969-580','R16','2218','858','20.01.1969-27.01.1969','ATP','1969','Achtelfinale','25171','78630']]
		sourceYear = '1969-580'
		sourceTourneyName = 'Australian Open'
		sourceRoundId = 'R32'
		outputToCheck = matches_rounds_and_profiles_synchronizer.MatchesRoundsAndProfilesSynchronizer().return_round_id(rounds, sourceYear, sourceTourneyName, sourceRoundId)
		self.assertEqual(outputToCheck, '78629')

	def test_return_matchresult_with_team_ids_and_round_id(self):
		"""dev
		"""
		outputToCheck = matches_rounds_and_profiles_synchronizer.MatchesRoundsAndProfilesSynchronizer().return_matchresult_with_team_ids_and_round_id()
		self.assertEqual(len(outputToCheck[0]), 4)
		self.assertEqual(len(outputToCheck[-1]), 4)

if __name__ == '__main__':
	os.system('radon cc -a matches_rounds_and_profiles_synchronizer.py')
	print('')
	unittest.main()
