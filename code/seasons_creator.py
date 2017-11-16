#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# mechanize only works in python2

import csv_handler
import admin_handler

class SeasonsCreator():
	"""Creates Seasons.
	"""

	def __init__(self):
		self.roundsPath = '../data/allDifferentGrandSlamRounds.csv'
		self.seasonUrlAppendix = '/admin/season.php?sport_id=5&season_id=&k=2&competition_id='

	def return_new_season_id(self, br, year):
		"""Returns the new season_id by year.
		"""
		for link in br.links():
			if '+' in link.text and year in link.text:
				hsSeasonId = link.url.split('season_id=')[1]
		return hsSeasonId

	def import_season(self, row, adminUrl):
		"""Imports a new season and returns the season_id.
		"""
		importUrl = adminUrl + self.seasonUrlAppendix + row[4]
		br = admin_handler.AdminHandler().return_gs_admin_content(importUrl)
		br.form = list(br.forms())[0]
		year = row[7]

		br.form.find_control('req[name]').value = year
		br.form.find_control('req[start_day]').value = row[5].split('-')[0].split('.')[0]
		br.form.find_control('req[start_month]').value = row[5].split('-')[0].split('.')[1]
		br.form.find_control('req[end_day]').value = row[5].split('-')[1].split('.')[0]
		br.form.find_control('req[end_month]').value = row[5].split('-')[1].split('.')[1]

		if len(row[5].split('-')[0].split('.')) == 2:
			br.form.find_control('req[start_year]').value = row[5].split('-')[0].split('.')[2]
			br.form.find_control('req[end_year]').value = row[5].split('-')[1].split('.')[2]
		else:
			br.form.find_control('req[start_year]').value = year
			br.form.find_control('req[end_year]').value = year

		for item in br.form.find_control('req[topic_id]').items:
			if row[3] == item.name:
				item.selected = True

		br.submit()
		seasonId = self.return_new_season_id(br, year)
		br.close()
		return seasonId

	def import_seasons(self, target):
		"""Imports all new seasons and returns a list containing all rounds with season_ids.
		"""
		adminUrl = admin_handler.AdminHandler().return_admin_url(target)
		rounds = csv_handler.CsvHandler().read_csv(self.roundsPath, 'r', 'latin-1', ',', '|', '2')
		currentSeasonId = '0'
		for i in range(len(rounds)):
			if rounds[i][7] != rounds[i-1][7]:
				seasonId = self.import_season(rounds[i], adminUrl)
				currentSeasonId = seasonId
			rounds[i].append(currentSeasonId)
		return rounds

	def write_csv(self, target, outputPath):
		"""Writes one csv document containing all different rounds (containing season_ids).
		"""
		roundsWithSeasonIds = self.import_seasons(target)
		csv_handler.CsvHandler().create_csv(roundsWithSeasonIds, outputPath)
		return outputPath

if __name__ == '__main__':
	SeasonsCreator().write_csv('ergebnisDienst', '../data/allRoundsWithSeasonIds.csv')
