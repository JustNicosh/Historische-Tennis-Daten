#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

import csv_handler
import re

class MatchesRoundsAndProfilesSynchronizer():
	"""Synchronizes all different matchresults with round_ids and team_ids.
	"""

	def __init__(self):
		self.matchesPath = '../data/competitions/tour-data/atp-500-data/allMatches.csv'
		self.profilesPath = '../data/competitions/tour-data/atp-500-data/everyProfileWithTeamId.csv'
		self.roundsPath = '../data/competitions/tour-data/atp-500-data/allRoundsWithRoundIds.csv'

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
		modifiedSetList = []
		incident = '0'

		if 'W/O' in sourceMatchResult or 'NA' in sourceMatchResult or '&nbsp;' in sourceMatchResult or sourceMatchResult == '':
			incident = '13'
		else:
			setList = sourceMatchResult.split(' ')
			for item in setList:
				if '(' in item:
					modifiedSetList.append(item.split('(')[0])
				elif not re.search('[a-zA-Z]', item):
					modifiedSetList.append(item)
				# if a player retired (RET, ABD or DEF)
				else:
					incident = '12'
		return {'sets': modifiedSetList, 'incident': incident}

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
			matchResults.append({'at': at, 'teamId': teamIdWinner, 'place': 'home', 'result': winnerPoints})
			matchResults.append({'at': at, 'teamId': teamIdLoser, 'place': 'away', 'result': loserPoints})
			# we need a counter for at = 0 (only complete sets, no 'RET' sets)
			if int(winnerPoints) > int(loserPoints) and int(winnerPoints) > 5:
				overallWinner += 1
			elif int(loserPoints) > 5:
				overallLoser += 1
		matchResults.append({'at': '0', 'teamId': teamIdWinner, 'place': 'home', 'result': str(overallWinner)})
		matchResults.append({'at': '0', 'teamId': teamIdLoser, 'place': 'away', 'result': str(overallLoser)})
		return matchResults

	def return_walkover_matchresults(self, teamIdWinner, teamIdLoser):
		"""Returns a dictionary containing walkover match_results (at, team_id, place, result) without round_ids.
		"""
		matchResults = [{'at': '0', 'teamId': teamIdWinner, 'place': 'home', 'result': '0'},
						{'at': '0', 'teamId': teamIdLoser, 'place': 'away', 'result': '0'}]
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
		"""Returns one list containing match_results (potentialMatch_id, round_id, team_id, result, at, place)
		and another containing match infos  (potentialMatch_id, round_id, winner_team_id, match_incident_id).
		"""
		csvData = self.return_csv_data()
		csvMatchResultRows = []
		csvMatchInfosRows = []
		matchCount = 1
		for match in csvData['matches']:
			setInfos = self.return_matchresultSets(match[27])
			sets = setInfos['sets']
			incident = setInfos['incident']
			teamIdWinner = self.return_team_id(csvData['profiles'], match[7], match[10])
			teamIdLoser = self.return_team_id(csvData['profiles'], match[17], match[20])

			# incident 13 (W/O etc.) -> no items in setlist (no match took place)
			if incident != '13':
				matchresultsWithoutRoundIds = self.return_match_results_without_round_ids(sets, teamIdWinner, teamIdLoser)
			else:
				matchresultsWithoutRoundIds = self.return_walkover_matchresults(teamIdWinner, teamIdLoser)

			# no round_id -> tourney after 2008 (we don't want these matches)
			roundId = self.return_round_id(csvData['rounds'], match[0], match[1], match[29])
			if roundId == None:
				continue

			matchResult = self.return_match_results_with_round_ids(matchresultsWithoutRoundIds, matchCount, roundId)
			for item in matchResult['matchResultsWithRoundIds']:
				csvMatchResultRows.append(item)

			csvMatchInfosRows.append([str(matchCount), roundId, teamIdWinner, incident])
			matchCount += 1
		return {'csvMatchResultRows': csvMatchResultRows, 'csvMatchInfosRows': csvMatchInfosRows}

	def write_csvs(self, outputPathMatchResults, outputPathMatchInfos):
		"""Writes one csv document containing match_results and another containing match infos.
		"""
		matchesData = self.return_matchresult_with_team_ids_and_round_id()
		csv_handler.CsvHandler().create_csv(matchesData['csvMatchResultRows'], outputPathMatchResults)
		csv_handler.CsvHandler().create_csv(matchesData['csvMatchInfosRows'], outputPathMatchInfos)
		return {'outputPathMatchResults': outputPathMatchResults, 'outputPathMatchInfos': outputPathMatchInfos}

if __name__ == '__main__':
	MatchesRoundsAndProfilesSynchronizer().write_csvs('../data/competitions/tour-data/atp-500-data/tennisMatchResults.csv', '../data/competitions/tour-data/atp-500-data/tennisMatchInfos.csv')
