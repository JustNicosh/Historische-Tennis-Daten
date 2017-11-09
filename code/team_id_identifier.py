#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

import csv_handler

class TeamIdIdentifier():
	"""Identifies depending team_id for each profile.
	"""

	def __init__(self):
		self.sourcePath = '../data/allProfilesWithCompetitions.csv'
		self.hsTeamsPath = '../data/hs-data/hs-table-team.csv'
		self.hsTeamIdRow = 0
		self.hsTeamNameRow = 1
		self.hsSportIdRow = 10

	def return_sports_specific_teams(self, hsTeams, sportId, hsTeamNameRow, hsSportIdRow):
		"""Returns only columns with the right sport_id and without a double marker.
		"""
		sportsSpecificTeams = []
		for row in hsTeams:
			if row[hsSportIdRow].replace('"', '') == sportId and '/' not in row[hsTeamNameRow]:
				sportsSpecificTeams.append(row)
		return sportsSpecificTeams

	def return_profiles_and_teams(self):
		"""Returns source profiles, hs-teams and hs-matches from given csvs.
		"""
		profiles = csv_handler.CsvHandler().read_csv(self.sourcePath, 'r', 'latin-1')
		hsAllTeams = csv_handler.CsvHandler().read_csv(self.hsTeamsPath, 'r', 'latin-1')
		hsTeams = self.return_sports_specific_teams(hsAllTeams, '5', self.hsTeamNameRow, self.hsSportIdRow)
		return {'profiles': profiles, 'hsTeams': hsTeams}

	def identify_id(self, profile, hsItems, hsTeamNameRow, hsTeamIdRow):
		"""Returns an id for a given profile.
		"""
		for item in hsItems:
			if profile[1] in item[hsTeamNameRow] and profile[2] in item[hsTeamNameRow]:
				return item[hsTeamIdRow]
			elif profile[1].replace('ae', 'ä') in item[hsTeamNameRow] and profile[2].replace('ae', 'ä') in item[hsTeamNameRow]:
				return item[hsTeamIdRow]
			elif profile[1].replace('oe', 'ö') in item[hsTeamNameRow] and profile[2].replace('oe', 'ö') in item[hsTeamNameRow]:
				return item[hsTeamIdRow]
			elif profile[1].replace('ue', 'ü') in item[hsTeamNameRow] and profile[2].replace('ue', 'ü') in item[hsTeamNameRow]:
				return item[hsTeamIdRow]
		return '0'

	def return_profiles_with_team_id(self):
		"""Returns a list containing all player profiles with team_ids.
		"""
		csvOutput = self.return_profiles_and_teams()
		profiles = csvOutput['profiles']
		hsTeams = csvOutput['hsTeams']
		for profile in profiles:
			teamId = self.identify_id(profile, hsTeams, self.hsTeamNameRow, self.hsTeamIdRow)
			profile.append(teamId.replace('"', ''))
		return profiles

	def write_csv(self, outputPath):
		"""Writes one csv document containing all player profiles with team_ids.
		"""
		profilesWithTeamIdsList = self.return_profiles_with_team_id()
		csv_handler.CsvHandler().create_csv(profilesWithTeamIdsList, outputPath)
		return outputPath

if __name__ == '__main__':
	TeamIdIdentifier().write_csv('../data/allProfilesWithTeamIds.csv')
