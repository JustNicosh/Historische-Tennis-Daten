#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

import csv_handler

class SeasonDetailsCollector():
	"""
	"""

	def __init__(self):
		self.dataSourcePrePath = '../data/competitions/'

	def return_all_different_matches(self, matchesSource, roundsWithSeasonIdsSource):
		"""Returns all different matches.
		"""
		csvPathMatches = self.dataSourcePrePath + matchesSource
		csvContentMatches = csv_handler.CsvHandler().read_csv(csvPathMatches, 'r', 'latin-1')
		csvPathRoundsWithSeasonIds = self.dataSourcePrePath + roundsWithSeasonIdsSource
		csvContentRoundsWithSeasonIds = csv_handler.CsvHandler().read_csv(csvPathRoundsWithSeasonIds, 'r', 'latin-1')
		return {'matches': csvContentMatches, 'roundsWithSeasonIds': csvContentRoundsWithSeasonIds}

	def return_different_seasons(self, matchesSource, roundsWithSeasonIdsSource):
		"""Returns all different seasons.
		"""
		data = self.return_all_different_matches(matchesSource, roundsWithSeasonIdsSource)
		matches = data['matches']
		roundsWithSeasonIds = data['roundsWithSeasonIds']
		differentSeasonsMarker = []
		differentSeasons = []
		for i in range(len(matches)):
			if matches[i][0] != matches[i-1][0] and matches[i][0] not in differentSeasons:
				differentSeasonsMarker.append(matches[i][0])
				differentSeasons.append(matches[i][0:4])

		for season in differentSeasons:
			for roundWithSeasonId in roundsWithSeasonIds:
				if season[0] == roundWithSeasonId[1]:
					season.append(roundWithSeasonId[-1])
					break

		print(differentSeasons)
		return differentSeasons

	def dev(self, matchesSource, roundsWithSeasonIdsSource):
		seasons = self.return_different_seasons(matchesSource, roundsWithSeasonIdsSource)
		print(len(seasons))

	def write_csv(self, matchesSource, roundsWithSeasonIdsSource):
		"""
		"""
		details = self.dev(matchesSource, roundsWithSeasonIdsSource)

		
if __name__ == '__main__':
	SeasonDetailsCollector().write_csv('tour-data/atp-1000-data/allMatches.csv', 'tour-data/atp-1000-data/allRoundsWithSeasonIds.csv')
	#SeasonDetailsCollector().write_csv('grand-slam-data/allGrandSlamMatches.csv', 'grand-slam-data/allRoundsWithSeasonIds.csv')
