#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

import csv_handler

class CompetitionsSynchronizer():
	"""Synchronizes all different competitions.
	"""

	def __init__(self):
		self.atp1000InfosPath = '../data/competitions/atp-1000-data/tennisMatchInfos.csv'
		self.atp1000MatchResultsPath = '../data/competitions/atp-1000-data/tennisMatchResults.csv'
		self.atp500GermanyInfosPath = '../data/competitions/atp-500-germany-data/tennisMatchInfos.csv'
		self.atp500GermanyMatchResultsPath = '../data/competitions/atp-500-germany-data/tennisMatchResults.csv'
		self.tourFinalsInfosPath = '../data/competitions/tour-finals-data/tennisMatchInfos.csv'
		self.tourFinalsMatchResultsPath = '../data/competitions/tour-finals-data/tennisMatchResults.csv'
		self.wtaPremierGermanyInfosPath = '../data/competitions/wta-premier-germany-data/tennisMatchInfos.csv'
		self.wtaPremierGermanyMatchResultsPath = '../data/competitions/wta-premier-germany-data/tennisMatchResults.csv'
		self.wtaPremierMandatoryAnd5InfosPath = '../data/competitions/wta-premier-mandatory-and-5-data/tennisMatchInfos.csv'
		self.wtaPremierMandatoryAnd5MatchResultsPath = '../data/competitions/wta-premier-mandatory-and-5-data/tennisMatchResults.csv'

		self.wtaPremierInfosPath = '../data/competitions/tour-data/wta-premier-data/tennisMatchInfos.csv'
		self.wtaPremierMatchResultsPath = '../data/competitions/tour-data/wta-premier-data/tennisMatchResults.csv'
		self.atp500InfosPath = '../data/competitions/tour-data/atp-500-data/tennisMatchInfos.csv'
		self.atp500MatchResultsPath = '../data/competitions/tour-data/atp-500-data/tennisMatchResults.csv'

	def return_csv_data(self):
		"""Returns all Match Infos and Match Results from given csvs.
		"""
		matchInfos = [
		#csv_handler.CsvHandler().read_csv(self.atp1000InfosPath, 'r', 'latin-1'),
		#csv_handler.CsvHandler().read_csv(self.atp500GermanyInfosPath, 'r', 'latin-1'),
		#csv_handler.CsvHandler().read_csv(self.tourFinalsInfosPath, 'r', 'latin-1'),
		#csv_handler.CsvHandler().read_csv(self.wtaPremierGermanyInfosPath, 'r', 'latin-1'),
		#csv_handler.CsvHandler().read_csv(self.wtaPremierMandatoryAnd5InfosPath, 'r', 'latin-1')
		csv_handler.CsvHandler().read_csv(self.wtaPremierInfosPath, 'r', 'latin-1'),
		csv_handler.CsvHandler().read_csv(self.atp500InfosPath, 'r', 'latin-1')
		]

		matchResults = [
		#csv_handler.CsvHandler().read_csv(self.atp1000MatchResultsPath, 'r', 'latin-1'),
		#csv_handler.CsvHandler().read_csv(self.atp500GermanyMatchResultsPath, 'r', 'latin-1'),
		#csv_handler.CsvHandler().read_csv(self.tourFinalsMatchResultsPath, 'r', 'latin-1'),
		#csv_handler.CsvHandler().read_csv(self.wtaPremierGermanyMatchResultsPath, 'r', 'latin-1'),
		#csv_handler.CsvHandler().read_csv(self.wtaPremierMandatoryAnd5MatchResultsPath, 'r', 'latin-1')
		csv_handler.CsvHandler().read_csv(self.wtaPremierMatchResultsPath, 'r', 'latin-1'),
		csv_handler.CsvHandler().read_csv(self.atp500MatchResultsPath, 'r', 'latin-1')
		]

		return {'matchInfos': matchInfos, 'matchResults': matchResults}

	def synchronize_competitons(self):
		"""Synchronizes running match_ids in match infos and match_results of different competitions.
		"""
		csvData = self.return_csv_data()

		oldMatches = 0
		allMatchInfos = []
		allMatchResults = []
		for i in range(len(csvData['matchInfos'])):
			infos = csvData['matchInfos'][i]
			results = csvData['matchResults'][i]

			for info in infos:
				info.append(int(info[0]) + oldMatches)
				allMatchInfos.append(info)
			for result in results:
				result.append(int(result[0]) + oldMatches)
				allMatchResults.append(result)

			oldMatches += len(infos)

		return {'csvMatchInfosRows': allMatchInfos, 'csvMatchResultsRows': allMatchResults}

	def write_csvs(self, outputPathMatchResults, outputPathMatchInfos):
		"""Writes one csv document containing match_results and another containing match infos.
		"""
		matchesData = self.synchronize_competitons()
		csv_handler.CsvHandler().create_csv(matchesData['csvMatchResultsRows'], outputPathMatchResults)
		csv_handler.CsvHandler().create_csv(matchesData['csvMatchInfosRows'], outputPathMatchInfos)
		return {'outputPathMatchResults': outputPathMatchResults, 'outputPathMatchInfos': outputPathMatchInfos}

if __name__ == '__main__':
	CompetitionsSynchronizer().write_csvs('../data/tennisMatchResults.csv', '../data/tennisMatchInfos.csv')
