#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import csv_handler

class DifferentRoundsAndSeasonsCollector():
	"""Collects all different rounds (depending on seasons and competitions).
	"""

	def __init__(self):
		self.matchesPath = '../data/allGrandSlamMatches.csv'
		self.hsSeasonTopicIdsPath = '../data/hs-data/hs-tennis-season-topics.csv'
		self.hsCompetitons = [{'name':'Australian Open', 'gender':'-W-', 'hs-competiton_id':'980'}, \
								{'name':'Australian Open', 'gender':'-M-', 'hs-competiton_id':'858'}, \
								{'name':'French Open', 'gender':'-W-', 'hs-competiton_id':'1019'}, \
								{'name':'Roland Garros', 'gender':'-M-', 'hs-competiton_id':'907'}, \
								{'name':'US Open', 'gender':'-W-', 'hs-competiton_id':'590'}, \
								{'name':'US Open', 'gender':'-M-', 'hs-competiton_id':'589'}, \
								{'name':'Wimbledon', 'gender':'-W-', 'hs-competiton_id':'1027'}, \
								{'name':'Wimbledon', 'gender':'-M-', 'hs-competiton_id':'919'}]
		self.yearRow = 0
		self.toureyNameRow = 1
		self.roundMarkerRow = 29

	def append_round_season_competition(self, roundSeasonCompetitions, match, yearRow, toureyNameRow, roundMarkerRow):
		"""Appends a round (depending on season and competition) if it is not present.
		"""
		itemsToCheck = [match[toureyNameRow], match[yearRow], match[roundMarkerRow]]
		if itemsToCheck not in roundSeasonCompetitions:
			roundSeasonCompetitions.append(itemsToCheck)
		return roundSeasonCompetitions

	def return_round_seasons_competitions(self):
		"""Collect all different rounds (depending on seasons and competitions) from matchesPath.
		"""
		roundSeasonCompetitions = []
		matches = csv_handler.CsvHandler().read_csv(self.matchesPath, 'r', 'latin-1')
		for match in matches:
			roundSeasonCompetitions = self.append_round_season_competition(roundSeasonCompetitions, match, self.yearRow, self.toureyNameRow, self.roundMarkerRow)
		roundSeasonCompetitions.sort(key = lambda round: round[0])
		return roundSeasonCompetitions

	def synchronize_with_season_topic_id(self):
		"""Synchronizes all rounds (depending on seasons and competitions) with the depending hs-season_topic_id.
		"""
		hsSeasonTopics = csv_handler.CsvHandler().read_csv(self.hsSeasonTopicIdsPath, 'r', 'latin-1')
		roundSeasonCompetitions = self.return_round_seasons_competitions()
		for roundSeasonCompetition in roundSeasonCompetitions:
			for hsSeasonTopic in hsSeasonTopics:
				if '-W-' not in roundSeasonCompetition[1] and 'ATP' in hsSeasonTopic[2] and roundSeasonCompetition[1].split('-')[0] in hsSeasonTopic[2]:
					roundSeasonCompetition.append(hsSeasonTopic[0].split('"')[1])
				elif '-W-' in roundSeasonCompetition[1] and 'WTA' in hsSeasonTopic[2] and roundSeasonCompetition[1].split('-')[0] in hsSeasonTopic[2]:
					roundSeasonCompetition.append(hsSeasonTopic[0].split('"')[1])
			if len(roundSeasonCompetition) == 3:
				roundSeasonCompetition.append('0')
		return roundSeasonCompetitions

	def synchronize_with_competiton_id(self):
		"""Synchronizes all rounds (depending on seasons and competitions) with the depending hs-competiton_id.
		"""
		roundSeasonCompetitions = self.synchronize_with_season_topic_id()
		for roundSeasonCompetition in roundSeasonCompetitions:
			for competiton in self.hsCompetitons:
				if '-W-' not in roundSeasonCompetition[1] and roundSeasonCompetition[0] == competiton['name'] and competiton['gender'] == '-M-':
					roundSeasonCompetition.append(competiton['hs-competiton_id'])
				elif '-W-' in roundSeasonCompetition[1] and roundSeasonCompetition[0] == competiton['name'] and competiton['gender'] == '-W-':
					roundSeasonCompetition.append(competiton['hs-competiton_id'])
		return roundSeasonCompetitions

	def write_csv(self, outputPath):
		"""Writes one csv document containing all different rounds (depending on seasons and competitions).
		"""
		synchronizedRoundSeasonCompetitions = self.synchronize_with_competiton_id()
		csv_handler.CsvHandler().create_csv(synchronizedRoundSeasonCompetitions, outputPath)
		return outputPath

if __name__ == '__main__':
	DifferentRoundsAndSeasonsCollector().write_csv('../data/allDifferentGrandSlamRounds.csv')
