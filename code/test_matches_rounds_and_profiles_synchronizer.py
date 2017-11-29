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

	def test_return_matchresultSets(self):
		"""Does the function return a list of sets (identified by the sourceMatchResult)?
		"""
		matchResult_1 = '2-6 7-6(5) 7-6(3)'
		matchResult_2 = '6-1 3-0 RET'
		matchResult_3 = '5-7 6-3 4-6 6-3 13-11'
		matchResult_4 = ' W/O'
		outputToCheck_1 = matches_rounds_and_profiles_synchronizer.MatchesRoundsAndProfilesSynchronizer().return_matchresultSets(matchResult_1)
		outputToCheck_2 = matches_rounds_and_profiles_synchronizer.MatchesRoundsAndProfilesSynchronizer().return_matchresultSets(matchResult_2)
		outputToCheck_3 = matches_rounds_and_profiles_synchronizer.MatchesRoundsAndProfilesSynchronizer().return_matchresultSets(matchResult_3)
		outputToCheck_4 = matches_rounds_and_profiles_synchronizer.MatchesRoundsAndProfilesSynchronizer().return_matchresultSets(matchResult_4)
		self.assertEqual(outputToCheck_1['sets'], ['2-6', '7-6', '7-6'])
		self.assertEqual(outputToCheck_1['incident'], '0')
		self.assertEqual(outputToCheck_2['sets'], ['6-1', '3-0'])
		self.assertEqual(outputToCheck_2['incident'], '12')
		self.assertEqual(outputToCheck_3['sets'], ['5-7', '6-3', '4-6', '6-3', '13-11'])
		self.assertEqual(outputToCheck_3['incident'], '0')
		self.assertEqual(outputToCheck_4['sets'], [])
		self.assertEqual(outputToCheck_4['incident'], '13')

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

	def test_return_match_results_without_round_ids(self):
		"""Does the function return a dictionary containing match_results (at, team_id, place, result) without round_ids?
		"""
		teamIdWinner = '123'
		teamIdLoser = '987'
		sets_1 = ['5-7', '6-3', '13-11']
		outputToCheck_1 = matches_rounds_and_profiles_synchronizer.MatchesRoundsAndProfilesSynchronizer().return_match_results_without_round_ids(sets_1, teamIdWinner, teamIdLoser)
		expectedOutput_1 = [{'teamId': '123', 'result': '5', 'place': 'home', 'at': '1'},
							{'teamId': '987', 'result': '7', 'place': 'away', 'at': '1'},
							{'teamId': '123', 'result': '6', 'place': 'home', 'at': '2'},
							{'teamId': '987', 'result': '3', 'place': 'away', 'at': '2'},
							{'teamId': '123', 'result': '13', 'place': 'home', 'at': '3'},
							{'teamId': '987', 'result': '11', 'place': 'away', 'at': '3'},
							{'teamId': '123', 'result': '2', 'place': 'home', 'at': '0'},
							{'teamId': '987', 'result': '1', 'place': 'away', 'at': '0'}]
		self.assertEqual(outputToCheck_1, expectedOutput_1)
		sets_2 = ['5-7', '1-1']
		outputToCheck_2 = matches_rounds_and_profiles_synchronizer.MatchesRoundsAndProfilesSynchronizer().return_match_results_without_round_ids(sets_2, teamIdWinner, teamIdLoser)
		expectedOutput_2 = [{'teamId': '123', 'result': '5', 'place': 'home', 'at': '1'},
							{'teamId': '987', 'result': '7', 'place': 'away', 'at': '1'},
							{'teamId': '123', 'result': '1', 'place': 'home', 'at': '2'},
							{'teamId': '987', 'result': '1', 'place': 'away', 'at': '2'},
							{'teamId': '123', 'result': '0', 'place': 'home', 'at': '0'},
							{'teamId': '987', 'result': '1', 'place': 'away', 'at': '0'}]
		self.assertEqual(outputToCheck_2, expectedOutput_2)

	def test_return_walkover_matchresults(self):
		"""Does the function return a dictionary containing walkover match_results (at, team_id, place, result) without round_ids?
		"""
		teamIdWinner = '123'
		teamIdLoser = '987'
		outputToCheck = matches_rounds_and_profiles_synchronizer.MatchesRoundsAndProfilesSynchronizer().return_walkover_matchresults(teamIdWinner, teamIdLoser)
		expectedOutput = [{'at': '0', 'teamId': '123', 'place': 'home', 'result': '0'},
						{'at': '0', 'teamId': '987', 'place': 'away', 'result': '0'}]
		self.assertEqual(outputToCheck, expectedOutput)

	def test_return_round_id(self):
		"""Does the function return a round_id (identified by the sourceYear, the sourceTourneyName and a sourceRoundId)?
		"""
		rounds = [['Australian Open','1969-580','R64','2218','858','20.01.1969-27.01.1969','ATP','1969','1. Runde','25171','78628'],
					['Australian Open','1969-580','R32','2218','858','20.01.1969-27.01.1969','ATP','1969','2. Runde','25171','78629'],
					['Australian Open','1969-580','R16','2218','858','20.01.1969-27.01.1969','ATP','1969','Achtelfinale','25171','78630'],]
		sourceYear = '1969-580'
		sourceTourneyName = 'Australian Open'
		sourceRoundId = 'R32'
		outputToCheck = matches_rounds_and_profiles_synchronizer.MatchesRoundsAndProfilesSynchronizer().return_round_id(rounds, sourceYear, sourceTourneyName, sourceRoundId)
		self.assertEqual(outputToCheck, '78629')

	def test_return_match_results_with_round_ids(self):
		"""Does the function return a list containing match_results (potentialMatch_id, round_id, team_id, result, at, place)?
		"""
		sets = [{'teamId': '123', 'result': '5', 'place': 'home', 'at': '1'},
				{'teamId': '987', 'result': '7', 'place': 'away', 'at': '1'},
				{'teamId': '123', 'result': '6', 'place': 'home', 'at': '2'},
				{'teamId': '987', 'result': '3', 'place': 'away', 'at': '2'},
				{'teamId': '123', 'result': '13', 'place': 'home', 'at': '3'},
				{'teamId': '987', 'result': '11', 'place': 'away', 'at': '3'},
				{'teamId': '123', 'result': '2', 'place': 'home', 'at': '0'},
				{'teamId': '987', 'result': '1', 'place': 'away', 'at': '0'}]
		round_id = '7777'
		outputToCheck = matches_rounds_and_profiles_synchronizer.MatchesRoundsAndProfilesSynchronizer().return_match_results_with_round_ids(sets, 99, round_id)
		expectedOutput = [['99', '7777', '123', '5', '1', 'home'],
							['99', '7777', '987', '7', '1', 'away'],
							['99', '7777', '123', '6', '2', 'home'],
							['99', '7777', '987', '3', '2', 'away'],
							['99', '7777', '123', '13', '3', 'home'],
							['99', '7777', '987', '11', '3', 'away'],
							['99', '7777', '123', '2', '0', 'home'],
							['99', '7777', '987', '1', '0', 'away']]
		self.assertEqual(outputToCheck['matchResultsWithRoundIds'], expectedOutput)

	def test_return_matchresult_with_team_ids_and_round_id(self):
		"""Does the function return one list containing match_results (potentialMatch_id, round_id, team_id, result, at, place)
		and another containing match infos  (potentialMatch_id, round_id, winner_team_id, match_incident_id)
		(known data -> >100000 with 6 columns, 36396 with 4 columns)?
		"""
		outputToCheck = matches_rounds_and_profiles_synchronizer.MatchesRoundsAndProfilesSynchronizer().return_matchresult_with_team_ids_and_round_id()
		self.assertGreater(len(outputToCheck['csvMatchResultRows']), 100000)
		self.assertEqual(len(outputToCheck['csvMatchResultRows'][0]), 6)
		self.assertEqual(len(outputToCheck['csvMatchResultRows'][-1]), 6)
		self.assertEqual(len(outputToCheck['csvMatchInfosRows']), 36396)
		self.assertEqual(len(outputToCheck['csvMatchInfosRows'][0]), 4)
		self.assertEqual(len(outputToCheck['csvMatchInfosRows'][-1]), 4)

	def test_write_csvs(self):
		"""Does the function write one csv document containing match_results and another containing match infos (known data -> >100000 and 36396)?
		"""
		paths = matches_rounds_and_profiles_synchronizer.MatchesRoundsAndProfilesSynchronizer().write_csvs('../data/test_tennisGrandSlamMatchResults.csv', '../data/test_tennisGrandSlamMatchInfos.csv')
		csvMatchResults = csv_handler.CsvHandler().read_csv(paths['outputPathMatchResults'], 'r', 'latin-1')
		csvMatchInfos = csv_handler.CsvHandler().read_csv(paths['outputPathMatchInfos'], 'r', 'latin-1')
		os.remove('../data/test_tennisGrandSlamMatchResults.csv')
		os.remove('../data/test_tennisGrandSlamMatchInfos.csv')
		self.assertGreater(len(csvMatchResults), 100000)
		self.assertEqual(len(csvMatchInfos), 36396)

if __name__ == '__main__':
	os.system('radon cc -a matches_rounds_and_profiles_synchronizer.py')
	print('')
	unittest.main()
