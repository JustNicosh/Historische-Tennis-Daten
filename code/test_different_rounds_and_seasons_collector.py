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

	def test_write_csv(self):
		"""Do we write one csv file with different rounds (known data -> 2312)?
        """
		path = different_rounds_and_seasons_collector.DifferentRoundsAndSeasonsCollector().write_csv('../data/test_allDifferentGrandSlamRounds.csv')
		csvContent = csv_handler.CsvHandler().read_csv(path, 'r', 'latin-1')
		os.remove('../data/test_allDifferentGrandSlamRounds.csv')
		self.assertEqual(len(csvContent), 2634)

if __name__ == '__main__':
	os.system('radon cc -a different_rounds_and_seasons_collector.py')
	print('')
	unittest.main()
