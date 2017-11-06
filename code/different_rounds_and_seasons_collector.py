#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import csv_handler

class DifferentRoundsAndSeasonsCollector():
	"""Collects all different rounds (depending on seasons and competitions).
	"""

	def __init__(self):
		self.matchesPath = '../data/allGrandSlamMatches.csv'
		self.yearRow = 0
		self.toureyNameRow = 1
		self.roundMarkerRow = 29

	def append_round_season_competition(self, roundSeasonCompetitions, match, yearRow, toureyNameRow, roundMarkerRow):
		"""Appends all different rounds (depending on seasons and competitions).
		"""
		itemsToCheck = [match[toureyNameRow], match[yearRow], match[roundMarkerRow]]
		if itemsToCheck not in roundSeasonCompetitions:
			roundSeasonCompetitions.append(itemsToCheck)
		return roundSeasonCompetitions

	def write_csv(self, outputPath):
		"""Writes one csv document containing all different rounds (depending on seasons and competitions).
		"""
		roundSeasonCompetitions = []
		matches = csv_handler.CsvHandler().read_csv(self.matchesPath, 'r', 'latin-1')
		for match in matches:
			roundSeasonCompetitions = self.append_round_season_competition(roundSeasonCompetitions, match, self.yearRow, self.toureyNameRow, self.roundMarkerRow)
		roundSeasonCompetitions.sort(key = lambda round: round[0])
		csv_handler.CsvHandler().create_csv(roundSeasonCompetitions, outputPath)
		return outputPath

if __name__ == '__main__':
	DifferentRoundsAndSeasonsCollector().write_csv('../data/allDifferentGrandSlamRounds.csv')
