#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

import csv_handler

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

	def return_matchresult(self, sourceMatchResults):
		"""dev
		"""
		return [sourceMatchResults]

	def return_team_id(self, allProfiles, sourceProfileId, soureProfileName):
		"""Returns a team_id (identified by a sourceProfileId and the soureProfileName).
		"""
		for profile in allProfiles:
			if sourceProfileId == profile[0] and profile[1] in soureProfileName and profile[2] in soureProfileName:
				return profile[7]
		return None

	def return_round_id(self, allRounds, sourceYear, sourceTourneyName, sourceRoundId):
		"""Returns a round_id (identified by the sourceYear, the sourceTourneyName and a sourceRoundId).
		"""
		for row in allRounds:
			if row[0] == sourceTourneyName and row[1] == sourceYear and row[2] == sourceRoundId:
				return row[10]
		return None

	def return_matchresult_with_team_ids_and_round_id(self):
		"""dev
		"""
		csvData = self.return_csv_data()
		csvOutputRows = []
		for match in csvData['matches']:
			matchResults = self.return_matchresult(match[27])
			teamIdHome = self.return_team_id(csvData['profiles'], match[7], match[10])
			teamIdAway = self.return_team_id(csvData['profiles'], match[17], match[20])
			roundId = self.return_round_id(csvData['rounds'], match[0], match[1], match[29])

			for matchResult in matchResults:
				csvOutputRows.append([roundId, teamIdHome, teamIdAway, matchResult])
		return csvOutputRows

if __name__ == '__main__':
	MatchesRoundsAndProfilesSynchronizer().return_matchresult_with_team_ids_and_round_id()
