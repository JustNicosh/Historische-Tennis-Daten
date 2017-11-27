#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

import csv_handler
import re

class MatchesRoundsAndProfilesSynchronizer():
	"""Synchronizes all different matchresults with round_ids and team_ids.
	"""

	def __init__(self):
		self.matchesPath = '../data/allGrandSlamMatches.csv'
		self.profilesPath = '../data/everyProfileWithTeamId.csv'
		self.roundsPath = '../data/allRoundsWithRoundIds.csv'

	def return_csv_data(self):
		"""Returns all matches, profiles and rounds from given csvs.
		"""
		matches = csv_handler.CsvHandler().read_csv(self.matchesPath, 'r', 'latin-1')
		profiles = csv_handler.CsvHandler().read_csv(self.profilesPath, 'r', 'latin-1')
		rounds = csv_handler.CsvHandler().read_csv(self.roundsPath, 'r', 'latin-1')
		return {'profiles': profiles, 'matches': matches, 'rounds': rounds}

	def return_matchresultSets(self, sourceMatchResult):
		"""Returns a list of sets (identified by the sourceMatchResult).
		"""
		setList = sourceMatchResult.split(' ')
		modifiedSetList = []
		for item in setList:
			if '(' in item:
				modifiedSetList.append(item.split('(')[0])
			elif not re.search('[a-zA-Z]', item) and item != '':
				modifiedSetList.append(item)
			# if a player retired, the depending last set should always be '6-0' (the winner is listed first)
			else:
				modifiedSetList.append('6-0')
		return modifiedSetList

	def return_team_id(self, allProfiles, sourceProfileId, soureProfileName):
		"""Returns a team_id (identified by a sourceProfileId and the soureProfileName).
		"""
		for profile in allProfiles:
			if sourceProfileId == profile[0] and profile[1] in soureProfileName and profile[2] in soureProfileName:
				return profile[7]
		return None

	def return_match_results_without_round_ids(self, sets, teamIdWinner, teamIdLoser):
		"""Returns a dictionary containing match_results (at, team_id, place, result) without round_ids.
		"""
		matchResults = []
		overallWinner = 0
		overallLoser = 0
		for i in range(len(sets)):
			at = str(i + 1)
			winnerPoints = sets[i].split('-')[0]
			loserPoints = sets[i].split('-')[1]
			matchResults.append({'at': at, 'teamId': teamIdWinner, 'place': 'none_home', 'result': winnerPoints})
			matchResults.append({'at': at, 'teamId': teamIdLoser, 'place': 'none_away', 'result': loserPoints})
			# we need a counter for at = 0
			if int(winnerPoints) > int(loserPoints):
				overallWinner += 1
			else:
				overallLoser += 1
		matchResults.append({'at': '0', 'teamId': teamIdWinner, 'place': 'none_home', 'result': str(overallWinner)})
		matchResults.append({'at': '0', 'teamId': teamIdLoser, 'place': 'none_away', 'result': str(overallLoser)})
		return matchResults

	def return_round_id(self, allRounds, sourceYear, sourceTourneyName, sourceRoundId):
		"""Returns a round_id (identified by the sourceYear, the sourceTourneyName and a sourceRoundId).
		"""
		for row in allRounds:
			if row[0] == sourceTourneyName and row[1] == sourceYear and row[2] == sourceRoundId:
				return row[10]
		return None

	def return_match_results_with_round_ids(self, sets, matchCount, roundId):
		"""Returns a list containing match_results (potentialMatch_id, round_id, team_id, result, at, place).
		"""
		matchResultsWithRoundIds = []
		for item in sets:
			matchResultsWithRoundIds.append([str(matchCount), roundId, item['teamId'], item['result'], item['at'], item['place']])
		return {'matchResultsWithRoundIds': matchResultsWithRoundIds}

	def return_matchresult_with_team_ids_and_round_id(self):
		"""dev
		"""
		csvData = self.return_csv_data()
		csvMatchResultRows = []
		csvMatchInfosRows = []
		matchCount = 1
		for match in csvData['matches']:
			sets = self.return_matchresultSets(match[27])
			teamIdWinner = self.return_team_id(csvData['profiles'], match[7], match[10])
			teamIdLoser = self.return_team_id(csvData['profiles'], match[17], match[20])
			matchresultsWithoutRoundIds = self.return_match_results_without_round_ids(sets, teamIdWinner, teamIdLoser)
			roundId = self.return_round_id(csvData['rounds'], match[0], match[1], match[29])
			matchResult = self.return_match_results_with_round_ids(matchresultsWithoutRoundIds, matchCount, roundId)

			for item in matchResult['matchResultsWithRoundIds']:
				csvMatchResultRows.append(item)

			csvMatchInfosRows.append([str(matchCount), teamIdWinner])
			matchCount += 1
		return {'csvMatchResultRows': csvMatchResultRows, 'csvMatchInfosRows': csvMatchInfosRows}

if __name__ == '__main__':
	MatchesRoundsAndProfilesSynchronizer().return_matchresult_with_team_ids_and_round_id()
