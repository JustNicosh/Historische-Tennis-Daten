#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import csv_handler

class ProfilesAndCompetitionsSynchronizer():
	"""Synchronizes all different player profiles and competitions.
	"""

	def __init__(self):
		self.profilesPath = '../data/allGrandSlamProfiles.csv'
		self.matchesPath = '../data/allGrandSlamMatches.csv'

	def return_profiles_and_matches(self):
		"""Returns all matches and all profiles from given csvs.
		"""
		profiles = csv_handler.CsvHandler().read_csv(self.profilesPath, 'r', 'latin-1')
		matches = csv_handler.CsvHandler().read_csv(self.matchesPath, 'r', 'latin-1')
		return {'profiles': profiles, 'matches': matches}

	def check_if_competition_is_present(self, match, competitions):
		"""Checks if competition is already present and appends it.
		"""
		competition = match[0].split('-')[0] + '_' + match[1]
		if competition not in competitions:
			competitions.append(competition)
		return competitions

	def return_all_competitions_for_one_profile(self, profile, matches):
		"""Returns all different competitions for one player.
		"""
		competitions = []
		for match in matches:
			if profile[0] in match and (profile[2] in match[10] or profile[2] in match[20]):
				competitions = self.check_if_competition_is_present(match, competitions)
		return competitions

	def return_profiles_with_competitons_list(self):
		"""Returns a list with all competitions by player profile.
		"""
		profilesAndMatches = self.return_profiles_and_matches()
		profiles = profilesAndMatches['profiles']
		matches = profilesAndMatches['matches']
		for profile in profiles:
			competitions = self.return_all_competitions_for_one_profile(profile, matches)
			profile.append('++'.join(competitions))
		return profiles

	def write_csv(self, outputPath):
		"""Writes one csv document containing all player profiles with competitions.
		"""
		profilesWithCompetitionsList = self.return_profiles_with_competitons_list()
		csv_handler.CsvHandler().create_csv(profilesWithCompetitionsList, outputPath)
		return outputPath

if __name__ == '__main__':
	ProfilesAndCompetitionsSynchronizer().write_csv('../data/allProfilesWithCompetitions.csv')
