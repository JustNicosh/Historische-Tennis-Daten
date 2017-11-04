#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import csv_handler

class TeamAndPersonIdIdentifier():
	"""Identifies depending team_id and person_id for each profile.
	"""

	def __init__(self):
		self.sourcePath = '../data/allProfilesWithCompetitions.csv'
		self.hsTeamsPath = '../data/hs-data/hs-table-team.csv'

	def return_sports_specific_teams(self, hsTeams, sportId):
		"""Returns only columns with the right sport_id and without a double marker.
		"""
		sportsSpecificTeams = []
		for row in hsTeams:
			if row[10][1] == sportId and '/' not in row[1]:
				sportsSpecificTeams.append(row)
		return sportsSpecificTeams

	def return_profiles_and_teams(self):
		"""Returns source profiles, hs-teams and hs-matches from given csvs.
		"""
		profiles = csv_handler.CsvHandler().read_csv(self.sourcePath, 'r', 'latin-1')
		hsAllTeams = csv_handler.CsvHandler().read_csv(self.hsTeamsPath, 'r', 'latin-1')
		hsTeams = self.return_sports_specific_teams(hsAllTeams, '5')
		return {'profiles': profiles, 'hsTeams': hsTeams}

	def identify_id(self, profile, hsItems, index):
		"""Identifies an id for a given profile.
		"""
		for item in hsItems:
			if profile[1] in item[index] and profile[2] in item[index]:
				return item[0]
			elif profile[1].replace('ae', 'ä') in item[index] and profile[2].replace('ae', 'ä') in item[index]:
				return item[0]
			elif profile[1].replace('oe', 'ö') in item[index] and profile[2].replace('oe', 'ö') in item[index]:
				return item[0]
			elif profile[1].replace('ue', 'ü') in item[index] and profile[2].replace('ue', 'ü') in item[index]:
				return item[0]
		return None

	def dev(self):
		csvOutput = self.return_profiles_and_teams()
		profiles = csvOutput['profiles']
		hsTeams = csvOutput['hsTeams']
		for profile in profiles:
			teamId = self.identify_id(profile, hsTeams, 1)
			profile.append(teamId)
		return profiles



if __name__ == '__main__':
	TeamAndPersonIdIdentifier().dev()
