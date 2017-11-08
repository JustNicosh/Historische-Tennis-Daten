#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import different_rounds_and_seasons_collector
import os
import unittest
import csv_handler

class TestDifferentRoundsAndSeasonsCollector(unittest.TestCase):
	"""Unittests for the class DifferentRoundsAndSeasonsCollector.
	"""

	def test_append_round_season_competition(self):
		"""Does the function append all different rounds (depending on seasons and competitions)?
        """
		# Test data:
		roundSeasonCompetitions = []
		matches = [['1968-560','US Open','Grass','96','G','19680829','001','100087','4','','John Newcombe','R','183','AUS','24.2683093771','','','110066','','','Allen Quay','R','','USA','','','','6-1 6-3 6-3','5','R128'], \
		['1968-560','US Open','Grass','96','G','19680829','002','100023','','','Ramanathan Krishnan','R','','IND','31.3839835729','','','109966','','','Warren Jacques','R','','AUS','30.4722792608','','','14-12 2-6 6-0 6-4','5','R128'], \
		['1968-560','US Open','Grass','96','G','19680829','003','109816','','','E Victor Seixas','R','185','USA','44.9993155373','','','100127','','','Tom Gorman','R','180','USA','21.6947296372','','','8-6 6-4 6-3','5','F']]
		self.assertEqual(len(different_rounds_and_seasons_collector.DifferentRoundsAndSeasonsCollector().append_round_season_competition(roundSeasonCompetitions, matches[0], 0, 1, 29)), 1)
		self.assertEqual(len(different_rounds_and_seasons_collector.DifferentRoundsAndSeasonsCollector().append_round_season_competition(roundSeasonCompetitions, matches[1], 0, 1, 29)), 1)
		self.assertEqual(len(different_rounds_and_seasons_collector.DifferentRoundsAndSeasonsCollector().append_round_season_competition(roundSeasonCompetitions, matches[2], 0, 1, 29)), 2)

	def test_return_round_seasons_competitions(self):
		"""Does the function return a list containing all different rounds (depending on seasons and competitions) (known data -> 2634)?
		"""
		self.assertEqual(len(different_rounds_and_seasons_collector.DifferentRoundsAndSeasonsCollector().return_round_seasons_competitions()), 2634)

	def test_synchronize_with_season_topic_id(self):
		"""Does the function synchronize all different rounds (depending on seasons and competitions) with season_topic_ids (known data -> 2634 and 4)?
		"""
		outputToCheck = different_rounds_and_seasons_collector.DifferentRoundsAndSeasonsCollector().synchronize_with_season_topic_id()
		self.assertEqual(len(outputToCheck), 2634)
		self.assertEqual(len(outputToCheck[0]), 4)
		self.assertEqual(len(outputToCheck[1000]), 4)

	def test_synchronize_with_competiton_id(self):
		"""Does the function synchronize all different rounds (depending on seasons and competitions) with competition_ids (known data -> 2634 and 5)?
		"""
		outputToCheck = different_rounds_and_seasons_collector.DifferentRoundsAndSeasonsCollector().synchronize_with_competiton_id()
		self.assertEqual(len(outputToCheck), 2634)
		self.assertEqual(len(outputToCheck[0]), 5)
		self.assertEqual(len(outputToCheck[1000]), 5)

	def test_synchronize_with_tourney_dates(self):
		"""Does the function synchronize all different rounds (depending on seasons and competitions) with tourney dates (known data -> 2634 and 6)?
		"""
		outputToCheck = different_rounds_and_seasons_collector.DifferentRoundsAndSeasonsCollector().synchronize_with_tourney_dates()
		self.assertEqual(len(outputToCheck), 2634)
		self.assertEqual(len(outputToCheck[0]), 6)
		self.assertEqual(len(outputToCheck[1000]), 6)

	def test_append_year_and_gender(self):
		"""Does the function append year and gender for each round (depending on season and competition) (known data -> 2634 and 7)?
		"""
		outputToCheck = different_rounds_and_seasons_collector.DifferentRoundsAndSeasonsCollector().append_year_and_gender()
		self.assertEqual(len(outputToCheck), 2634)
		self.assertEqual(len(outputToCheck[0]), 7)
		self.assertEqual(len(outputToCheck[1000]), 7)

	def test_consider_only_specific_years(self):
		"""Does the function only return rounds (depending on seasons and competitions) with specific years (known data -> 2193)?
		"""
		outputToCheck = different_rounds_and_seasons_collector.DifferentRoundsAndSeasonsCollector().consider_only_specific_years()
		self.assertEqual(len(outputToCheck), 2193)

	def test_write_csv(self):
		"""Do we write one csv file with different rounds (known data -> 2193)?
        """
		path = different_rounds_and_seasons_collector.DifferentRoundsAndSeasonsCollector().write_csv('../data/test_allDifferentGrandSlamRounds.csv')
		csvContent = csv_handler.CsvHandler().read_csv(path, 'r', 'latin-1')
		os.remove('../data/test_allDifferentGrandSlamRounds.csv')
		self.assertEqual(len(csvContent), 2193)

if __name__ == '__main__':
	os.system('radon cc -a different_rounds_and_seasons_collector.py')
	print('')
	unittest.main()
