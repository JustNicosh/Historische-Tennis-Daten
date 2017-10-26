#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

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

	def dev(self):
		print(self.return_matches_csv_paths())

		#csvFile = open(str, 'rb')
		#reader = csv.reader(csvFile, delimiter=',', quotechar='|')
			


if __name__ == '__main__':
	ProfileHandler().dev()
