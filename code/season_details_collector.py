#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

import csv_handler

class SeasonDetailsCollector():
	"""Collects Season Details (for DB-table season_detail).
	"""

	def __init__(self):
		self.dataSourcePrePath = '../data/competitions/'

	def modify_price_money(self):
		"""DEV
		"""
		priceMoneyYears = csv_handler.CsvHandler().read_csv('../data/research-data/price_money.csv', 'r', 'latin-1')
		wimbledonFactor = 1.1395
		for i in range(1,len(priceMoneyYears)):
			print(priceMoneyYears[i][0])

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
			if matches[i][0] != matches[i-1][0] and matches[i][0] not in differentSeasonsMarker:
				differentSeasonsMarker.append(matches[i][0])
				differentSeasons.append(matches[i][0:4])

		for season in differentSeasons:
			for roundWithSeasonId in roundsWithSeasonIds:
				if season[0] == roundWithSeasonId[1]:
					season.append(roundWithSeasonId[-1])
					break

		return differentSeasons

	def write_csv(self, matchesSource, roundsWithSeasonIdsSource, outputPath):
		"""Writes one csv containing all season details.
		"""
		seasons = self.return_different_seasons(matchesSource, roundsWithSeasonIdsSource)
		csv_handler.CsvHandler().create_csv(seasons, self.dataSourcePrePath + outputPath)
		return outputPath

		
if __name__ == '__main__':
	SeasonDetailsCollector().write_csv('tour-data/wta-premier-mandatory-and-5-data/allMatches.csv', 'tour-data/wta-premier-mandatory-and-5-data/allRoundsWithSeasonIds.csv', 'tour-data/wta-premier-mandatory-and-5-data/seasonDetails.csv')
	#SeasonDetailsCollector().write_csv('grand-slam-data/allGrandSlamMatches.csv', 'grand-slam-data/allRoundsWithSeasonIds.csv', 'grand-slam-data/seasonDetails.csv')
	#SeasonDetailsCollector().modify_price_money()
