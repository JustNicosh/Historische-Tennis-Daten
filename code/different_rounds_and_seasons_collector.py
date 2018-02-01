#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

import csv_handler

class DifferentRoundsAndSeasonsCollector():
	"""Collects all different rounds (depending on seasons and competitions)
	and synchronizes them with data (hs -> season-topic_ids and competition_ids; research -> tourney dates).
	"""

	def __init__(self):
		self.matchesPath = '../data/competitions/tour-data/atp-500-data/allMatches.csv'
		self.hsSeasonTopicIdsPath = '../data/hs-data/hs-tennis-season-topics.csv'
		self.researchTourneyDatesPath = '../data/research-data/tourney-dates.csv'
		self.sourceGenderFemaleMarker = '-W-'
		self.sourceGenderMaleMarker = '-M-'
		self.hsGenderFemaleMarker = 'WTA'
		self.hsGenderMaleMarker = 'ATP'
		self.hsCompetitons = [#{'name': 'Australian Open', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'980'}, \
								#{'name': 'Australian Open', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'858'}, \
								#{'name': 'French Open', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1019'}, \
								#{'name': 'Roland Garros', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'907'}, \
								#{'name': 'US Open', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'590'}, \
								#{'name': 'US Open', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'589'}, \
								#{'name': 'Wimbledon', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1027'}, \
								#{'name': 'Wimbledon', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'919'}, \
								#{'name': 'Masters Cup', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'965'}, \
								#{'name': 'Tour Finals', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'965'}, \
								#{'name': 'Masters', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'965'}, \
								#{'name': 'WTA Tour Championships', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'2701'}, \
								#{'name': 'Virginia Slims Championships', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'2701'}, \
								#{'name': 'Indian Wells', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'883'}, \
								#{'name': 'Indian Wells Masters', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'883'}, \
								#{'name': 'Key Biscayne', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'885'}, \
								#{'name': 'Miami Masters', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'885'}, \
								#{'name': 'Rome', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'896'}, \
								#{'name': 'Rome Masters', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'896'}, \
								#{'name': 'Monte Carlo', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'891'}, \
								#{'name': 'Monte Carlo Masters', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'891'}, \
								#{'name': 'Madrid Masters', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'657'}, \
								#{'name': 'Montreal / Toronto', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'939'}, \
								#{'name': 'Canada Masters', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'939'}, \
								#{'name': 'Cincinnati', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'941'}, \
								#{'name': 'Cincinnati Masters', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'941'}, \
								#{'name': 'Paris Indoor', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'661'}, \
								#{'name': 'Paris Masters', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'661'}, \
								#{'name': 'Hamburg', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'929'}, \
								#{'name': 'Hamburg Masters', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'929'}, \
								#{'name': 'Halle', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'913'}, \
								#{'name': 'Indian Wells', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'996'}, \
								#{'name': 'Miami Masters', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'998'}, \
								#{'name': 'Key Biscayne', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'998'}, \
								#{'name': 'Madrid', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1013'}, \
								#{'name': 'Beijing', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'665'}, \
								#{'name': 'Shanghai', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'665'}, \
								#{'name': 'Dubai Open', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'986'}, \
								#{'name': 'Rome', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1009'}, \
								#{'name': 'Perugia', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1009'}, \
								#{'name': 'Canadian Open', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1049'}, \
								#{'name': 'Cincinnati', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1047'}, \
								#{'name': 'Stuttgart', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'667'}, \
								#{'name': 'Filderstadt', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'667'}, \
								{'name': 'Rotterdam', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'870'}, \
								{'name': 'Acapulco', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'881'}, \
								{'name': 'Mexico City', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'881'}, \
								{'name': 'Dubai', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'879'}, \
								{'name': 'Barcelona', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'893'}, \
								{'name': "Queen's Club", 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'909'}, \
								{'name': 'Washington', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'937'}, \
								{'name': 'Beijing', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'649'}, \
								{'name': 'Tokyo', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'651'}, \
								{'name': 'Tokyo Indoor', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'651'}, \
								{'name': 'Tokyo Outdoor', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'651'}, \
								{'name': 'Vienna', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'654'}, \
								{'name': 'Basel', 'gender': self.sourceGenderMaleMarker, 'hs-competiton_id':'658'}, \
								{'name': 'Sydney', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'976'}, \
								{'name': 'Doha', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1845'}, \
								{'name': 'Charleston', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1002'}, \
								{'name': 'Hilton Head', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1002'}, \
								{'name': 'Birmingham', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1021'}, \
								{'name': 'Eastbourne', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1023'}, \
								{'name': 'Stanford', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1041'}, \
								{'name': 'Oakland', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1041'}, \
								{'name': 'San Francisco', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1041'}, \
								{'name': 'New Haven', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1051'}, \
								{'name': 'Atlanta', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1051'}, \
								{'name': 'Stratton Mountain', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1051'}, \
								{'name': 'San Antonio', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'1051'}, \
								{'name': 'Tokyo', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'663'}, \
								{'name': 'Moscow', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'670'}, \
								{'name': 'Kremlin Cup', 'gender': self.sourceGenderFemaleMarker, 'hs-competiton_id':'670'}]
		self.yearRow = 0
		self.toureyNameRow = 1
		self.roundMarkerRow = 29
		self.lastYear = 2010
		self.roundNames = [{'sourceName': 'R128', 'hsName': '1. Runde'}, \
								{'sourceName': 'R64', 'hsName': '2. Runde'}, \
								{'sourceName': 'R32', 'hsName': '3. Runde'}, \
								{'sourceName': 'R16', 'hsName': 'Achtelfinale'}, \
								{'sourceName': 'QF', 'hsName': 'Viertelfinale'}, \
								{'sourceName': 'SF', 'hsName': 'Halbfinale'}, \
								{'sourceName': 'F', 'hsName': 'Finale'}, \
								{'sourceName': 'RR', 'hsName': 'Gruppenphase'}]
		self.unknownRoundName = 'unbekannt'
		self.datesKnown = False


	def append_round_season_competition(self, roundSeasonCompetitions, match, yearRow, toureyNameRow, roundMarkerRow):
		"""Appends a round (depending on season and competition) if it is not present.
		"""
		itemsToCheck = [match[toureyNameRow], match[yearRow], match[roundMarkerRow]]
		if itemsToCheck not in roundSeasonCompetitions:
			roundSeasonCompetitions.append(itemsToCheck)
		return roundSeasonCompetitions

	def return_round_seasons_competitions(self):
		"""Collects all different rounds (depending on seasons and competitions) from matchesPath.
		"""
		roundSeasonCompetitions = []
		matches = csv_handler.CsvHandler().read_csv(self.matchesPath, 'r', 'latin-1')
		for match in matches:
			roundSeasonCompetitions = self.append_round_season_competition(roundSeasonCompetitions, match, self.yearRow, self.toureyNameRow, self.roundMarkerRow)
		roundSeasonCompetitions.sort(key = lambda round: round[0])
		return roundSeasonCompetitions

	def synchronize_with_season_topic_id(self):
		"""Synchronizes all rounds (depending on seasons and competitions) with the depending hs-season_topic_id from hs-data.
		"""
		hsSeasonTopics = csv_handler.CsvHandler().read_csv(self.hsSeasonTopicIdsPath, 'r', 'latin-1')
		roundSeasonCompetitions = self.return_round_seasons_competitions()
		for roundSeasonCompetition in roundSeasonCompetitions:
			for hsSeasonTopic in hsSeasonTopics:
				if self.sourceGenderFemaleMarker not in roundSeasonCompetition[1] and self.hsGenderMaleMarker in hsSeasonTopic[2] and roundSeasonCompetition[1].split('-')[0] in hsSeasonTopic[2]:
					roundSeasonCompetition.append(hsSeasonTopic[0].split('"')[1])
				elif self.sourceGenderFemaleMarker in roundSeasonCompetition[1] and self.hsGenderFemaleMarker in hsSeasonTopic[2] and roundSeasonCompetition[1].split('-')[0] in hsSeasonTopic[2]:
					roundSeasonCompetition.append(hsSeasonTopic[0].split('"')[1])
			if len(roundSeasonCompetition) == 3:
				roundSeasonCompetition.append('0')
		return roundSeasonCompetitions

	def synchronize_with_competiton_id(self):
		"""Synchronizes all rounds (depending on seasons and competitions) with the depending hs-competiton_id from hs-data.
		"""
		roundSeasonCompetitions = self.synchronize_with_season_topic_id()
		for roundSeasonCompetition in roundSeasonCompetitions:
			for competiton in self.hsCompetitons:
				if self.sourceGenderFemaleMarker not in roundSeasonCompetition[1] and roundSeasonCompetition[0] == competiton['name'] and competiton['gender'] == self.sourceGenderMaleMarker:
					roundSeasonCompetition.append(competiton['hs-competiton_id'])
				elif self.sourceGenderFemaleMarker in roundSeasonCompetition[1] and roundSeasonCompetition[0] == competiton['name'] and competiton['gender'] == self.sourceGenderFemaleMarker:
					roundSeasonCompetition.append(competiton['hs-competiton_id'])
		return roundSeasonCompetitions

	def synchronize_with_tourney_dates(self):
		"""Synchronizes all rounds (depending on seasons and competitions) with the tourney dates from research-data.
		"""
		roundSeasonCompetitions = self.synchronize_with_competiton_id()
		tourneyDates = csv_handler.CsvHandler().read_csv(self.researchTourneyDatesPath, 'r', 'latin-1')
		for roundSeasonCompetition in roundSeasonCompetitions:
			if self.datesKnown:
				for date in tourneyDates:
					if roundSeasonCompetition[0] == date[0] and roundSeasonCompetition[1].split('-')[0] == date[1]:
						roundSeasonCompetition.append(date[2])
			else:
				roundSeasonCompetition.append('00.00.0000-00.00.0000')
		return roundSeasonCompetitions

	def append_year_and_gender(self):
		"""Appends year and gender to each round (depending on season and competition).
		"""
		roundSeasonCompetitions = self.synchronize_with_tourney_dates()
		for roundSeasonCompetition in roundSeasonCompetitions:
			if self.sourceGenderFemaleMarker not in roundSeasonCompetition[1]:
				roundSeasonCompetition.append(self.hsGenderMaleMarker)
			elif self.sourceGenderFemaleMarker in roundSeasonCompetition[1]:
				roundSeasonCompetition.append(self.hsGenderFemaleMarker)
			roundSeasonCompetition.append(roundSeasonCompetition[1].split('-')[0])
			#del roundSeasonCompetition[1]
		return roundSeasonCompetitions

	def consider_only_specific_years(self):
		"""Considers only tourneys which took place in a given period of time.
		"""
		roundSeasonCompetitions = self.append_year_and_gender()
		onlySpecificRoundSeasonCompetitions = [roundSeasonCompetition for roundSeasonCompetition in roundSeasonCompetitions if int(roundSeasonCompetition[-1]) <= self.lastYear]
		return onlySpecificRoundSeasonCompetitions

	def return_renamed_rounds(self):
		"""Returns all rounds (depending on seasons and competitions) with hs names.
		"""
		roundSeasonCompetitions = self.consider_only_specific_years()
		for roundSeasonCompetition in roundSeasonCompetitions:
			for roundName in self.roundNames:
				if roundSeasonCompetition[2] == roundName['sourceName']:
					roundSeasonCompetition.append(roundName['hsName'])
			if len(roundSeasonCompetition) == 8:
				roundSeasonCompetition.append(self.unknownRoundName)
		return roundSeasonCompetitions

	def write_csv(self, outputPath):
		"""Writes one csv document containing all different rounds (depending on seasons and competitions).
		"""
		synchronizedRoundSeasonCompetitions = self.return_renamed_rounds()
		csv_handler.CsvHandler().create_csv(synchronizedRoundSeasonCompetitions, outputPath)
		return outputPath

if __name__ == '__main__':
	DifferentRoundsAndSeasonsCollector().write_csv('../data/competitions/tour-data/atp-500-data/allDifferentRounds.csv')
