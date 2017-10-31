#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import csv_handler

class TeamAndPersonIdIdentifier():
	"""Identifies depending team_id and person_id for each profile.
	"""

	def __init__(self):
		self.sourcePath = '../data/allProfilesWithCompetitions.csv'
		self.hsTeamsPath = '../data/hs-data/hs-table-team.csv'
		self.hsPersonsPath = '../data/hs-data/hs-table-person.csv'

	def return_profiles_teams_and_persons(self):
		"""Returns source profiles, hs-teams and hs-matches from given csvs.
		"""
		profiles = csv_handler.CsvHandler().read_csv(self.sourcePath, 'r', 'latin-1')
		hsTeams = csv_handler.CsvHandler().read_csv(self.hsTeamsPath, 'r', 'latin-1')
		hsPersons = csv_handler.CsvHandler().read_csv(self.hsPersonsPath, 'r', 'latin-1')
		return {'profiles': profiles, 'hsTeams': hsTeams, 'hsPersons': hsPersons}

	def identify_team_id(self, profile, hsTeams):
		"""Identifies a team_id for a given profile.
		"""
		for team in hsTeams:
			if profile[1] in team[1] and profile[2] in team[1] and not '/' in team[1]:
				return team[0]
		return None

	def identify_person_id(self, profile, hsPersons):
		"""Identifies a person_id for a given profile.
		"""
		for person in hsPersons:
			if profile[1] in person[1] and profile[2] in person[2]:
				return person[0]
		return None

	def dev(self):
		csvOutput = self.return_profiles_teams_and_persons()
		profiles = csvOutput['profiles']
		hsTeams = csvOutput['hsTeams']
		hsPersons = csvOutput['hsPersons']

		for profile in profiles:
			teamId = self.identify_team_id(profile, hsTeams)
			personId = self.identify_person_id(hsPersons)
			profile.append(teamId)
			profile.append(personId)

		return profiles



if __name__ == '__main__':
	TeamAndPersonIdIdentifier()
