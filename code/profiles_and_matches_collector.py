#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import csv_handler

class ProfilesAndMatchesCollector():
	"""Collects all different Grad Slam player profiles and matches.
	"""

	def __init__(self):
		self.dataMainSource = '../data'
		self.dataGenderSources = [{'source': '/tennis_atp-master/', 'id': 'atp'}, {'source': '/tennis_wta-master/', 'id': 'wta'}]
		self.dataMatchesIdentifier = '_matches_'
		self.dataProfilesIdentifier = 'players'
		self.dataGradSlamIdentifiers = ['Australian Open', 'Roland Garros', 'Wimbledon', 'US Open']
		self.firstYear = 1968
		self.lastYear = 2017
		self.dataEnding = '.csv'
		self.tourneyColumn = 1
		self.winnerIdColumn = 7
		self.winnerNameColumn = 10
		self.loserIdColumn = 17
		self.loserNameColumn = 20

	def return_matches_csv_paths_for_single_gender(self, gender):
		"""Returns relative paths to matchresults-csvs for a single gender.
		"""
		csvpaths = []
		for i in range(self.firstYear, self.lastYear + 1):
			csvSource = self.dataMainSource + gender['source'] + gender['id'] + self.dataMatchesIdentifier + str(i) + self.dataEnding
			csvpaths.append(csvSource)
		return csvpaths
			
	def return_matches_csv_paths(self):
		"""Returns relative paths to matchresults-csvs for a both genders.
		"""
		csvpaths = []
		for gender in self.dataGenderSources:
			csvpaths += self.return_matches_csv_paths_for_single_gender(gender)
		return csvpaths

	def return_csv_contents(self):
		"""Returns the contents of several csv files stored in a list.
		"""
		csvcontents = []
		csvpaths = self.return_matches_csv_paths()
		for path in csvpaths:
			csvContent = csv_handler.CsvHandler().read_csv(path, 'r', 'latin-1')
			csvcontents.append(csvContent)
		return csvcontents

	def append_absent_players(self, row, tourneyColumn, playerList, dataGradSlamIdentifiers, winnerIdColumn, winnerNameColumn, loserIdColumn, loserNameColumn):
		"""Appends all absent players to a list of players.
		"""
		if row[tourneyColumn] in dataGradSlamIdentifiers:
			if {'id': row[winnerIdColumn], 'name': row[winnerNameColumn]} not in playerList:
				playerList.append({'id': row[winnerIdColumn], 'name': row[winnerNameColumn]})
			if {'id': row[loserIdColumn], 'name': row[loserNameColumn]} not in playerList:
				playerList.append({'id': row[loserIdColumn], 'name': row[loserNameColumn]})
		return playerList

	def return_all_different_players_and_matches(self):
		"""Returns a list with all Grand Slam players and all Grand Slam matches of our data.
		"""
		csvcontents = self.return_csv_contents()
		playerList = []
		matchesList = []
		for matchList in csvcontents:
			for row in matchList:
				if row[self.tourneyColumn] in self.dataGradSlamIdentifiers:
					matchesList.append(row)
				playerList = self.append_absent_players(row, self.tourneyColumn, playerList, self.dataGradSlamIdentifiers, self.winnerIdColumn, self.winnerNameColumn, self.loserIdColumn, self.loserNameColumn)
		return {'playerList': playerList, 'matchesList': matchesList}

	def append_gender(self, profiles, gender):
		"""Appends gender ids to all items of a list of gender specific profiles.
		"""
		for profile in profiles:
			profile.append(gender['id'])
		return profiles

	def return_all_different_profiles(self):
		"""Returns a list with all Person Profiles (ATP and WTA).
		"""
		allDifferentProfiles = []
		for gender in self.dataGenderSources:
			path = self.dataMainSource + gender['source'] + gender['id'] + '_' + self.dataProfilesIdentifier + self.dataEnding
			csvContent = csv_handler.CsvHandler().read_csv(path, 'r', 'latin-1')
			singleGenderProfiles = self.append_gender(csvContent, gender)
			allDifferentProfiles += singleGenderProfiles
		return allDifferentProfiles
	
	def identify_same_profile(self, allProfiles, gradSlamPlayer):
		"""Matches all players with same id (caution: same id can occur twice, male and female) and name.
		"""
		for profile in allProfiles:
			if gradSlamPlayer['id'] == profile[0] and profile[1] in gradSlamPlayer['name'] and profile[2] in gradSlamPlayer['name']:
				return profile
		return None

	def return_all_grand_slam_profiles_and_matches(self):
		"""Returns a list with all Grand Slam player profiles and all Grand Slam matches.
		"""
		allDifferentPlayersAndMatches = self.return_all_different_players_and_matches()
		differentGradSlamPlayers = allDifferentPlayersAndMatches['playerList']
		allmatches = allDifferentPlayersAndMatches['matchesList']
		allProfiles = self.return_all_different_profiles()
		allGrandSlamProfiles = []
		for gradSlamPlayer in differentGradSlamPlayers:
			profile = self.identify_same_profile(allProfiles, gradSlamPlayer)
			allGrandSlamProfiles.append(profile)
		return {'allGrandSlamProfiles': allGrandSlamProfiles, 'allGrandSlamMatches': allmatches}

	def write_csvs(self, outputPathProfiles, outputPathMatches):
		"""Writes one csv document containing all Grand Slam player profiles and one containing all Grand Slam matches.
		"""
		allGrandSlamProfilesAndMatches = self.return_all_grand_slam_profiles_and_matches()
		allGrandSlamProfiles = allGrandSlamProfilesAndMatches['allGrandSlamProfiles']
		allGrandSlamMatches = allGrandSlamProfilesAndMatches['allGrandSlamMatches']
		csv_handler.CsvHandler().create_csv(allGrandSlamProfiles, outputPathProfiles)
		csv_handler.CsvHandler().create_csv(allGrandSlamMatches, outputPathMatches)
		return {'outputPathProfiles': outputPathProfiles, 'outputPathMatches': outputPathMatches}

if __name__ == '__main__':
	ProfilesAndMatchesCollector().write_csvs('../data/allGrandSlamProfiles.csv', '../data/allGrandSlamMatches.csv')
