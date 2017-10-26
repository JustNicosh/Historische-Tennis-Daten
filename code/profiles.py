#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import csv_handler

class ProfileHandler():
	"""Handle player profile data.
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
		"""Append all absent players to a list of players.
		"""
		if row[tourneyColumn] in dataGradSlamIdentifiers:
			if {'id': row[winnerIdColumn], 'name': row[winnerNameColumn]} not in playerList:
				playerList.append({'id': row[winnerIdColumn], 'name': row[winnerNameColumn]})
			if {'id': row[loserIdColumn], 'name': row[loserNameColumn]} not in playerList:
				playerList.append({'id': row[loserIdColumn], 'name': row[loserNameColumn]})
		return playerList

	def return_all_different_players(self):
		"""Returns a list with all Grand Slam Players of our data.
		"""
		csvcontents = self.return_csv_contents()
		playerList = []
		for matchList in csvcontents:
			for row in matchList:
				playerList = self.append_absent_players(row, self.tourneyColumn, playerList, self.dataGradSlamIdentifiers, self.winnerIdColumn, self.winnerNameColumn, self.loserIdColumn, self.loserNameColumn)
		return playerList
			
	def dev(self):
		print(len(self.return_all_different_players()))

if __name__ == '__main__':
	ProfileHandler().dev()
