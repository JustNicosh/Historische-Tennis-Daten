#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

import csv_handler

class ProfilesAndSeasonIdsSynchronizer():
	"""Synchronizes all different player profiles and season_ids.
	"""

	def __init__(self):
		self.profilesPath = '../data/allProfilesWithTeamIds.csv'
		self.seasonsPath = '../data/allRoundsWithRoundIds.csv'

	def return_profiles_and_seasons(self):
		"""Returns all seasons and all profiles from given csvs.
		"""
		profiles = csv_handler.CsvHandler().read_csv(self.profilesPath, 'r', 'latin-1')
		seasons = csv_handler.CsvHandler().read_csv(self.seasonsPath, 'r', 'latin-1')
		return {'profiles': profiles, 'seasons': seasons}

	def return_season_ids(self, profileSeasons, seasons):
		"""Returns a string containing different season_ids.
		"""
		seasonIdsString = ''
		for profileSeason in profileSeasons:
			year = profileSeason.split('_')[0]
			tourney = profileSeason.split('_')[1]
			for season in seasons:
				if season[0] == tourney and season[7] == year:
					seasonIdsString += season[9] + '_'
					break
		seasonIdsString = seasonIdsString[:-1]
		return seasonIdsString

	def return_profiles_with_season_ids(self):
		"""Returns a list containing all profiles with season_ids.
		"""
		data = self.return_profiles_and_seasons()
		profiles = data['profiles']
		seasons = data['seasons']
		for profile in profiles:
			profileSeasons = profile[7].split('++')
			seasonIds = self.return_season_ids(profileSeasons, seasons)
			del profile[7]
			profile.append(seasonIds)
		return profiles

	def write_csv(self, outputPath):
		"""Writes one csv document containing all player profiles with season_ids.
		"""
		profilesWithSeasonIds = self.return_profiles_with_season_ids()
		csv_handler.CsvHandler().create_csv(profilesWithSeasonIds, outputPath)
		return outputPath

if __name__ == '__main__':
	ProfilesAndSeasonIdsSynchronizer().write_csv('../data/allProfilesWithSeasonIds.csv')
