#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# mechanize only works in python2

import csv_handler
import admin_handler

class RoundsCreator():
	"""Creates Rounds.
	"""

	def __init__(self):
		self.roundsPath = '../data/competitions/wta-premier-mandatory-and-5-data/allRoundsWithSeasonIds.csv'
		self.roundUrlAppendixBeforeCompetitionId = '/admin/round.php?sport_id=5&competition_id='
		self.roundUrlAppendixBeforeSeasonId = '&round_id=&k=2&season_id='
		self.roundNamesAndOrders = [{'name': 'unbekannt', 'order': '1'}, \
									{'name': 'Gruppenphase', 'order': '1'}, \
									{'name': '1. Runde', 'order': '1'}, \
									{'name': '2. Runde', 'order': '2'}, \
									{'name': '3. Runde', 'order': '3'}, \
									{'name': 'Achtelfinale', 'order': '4'}, \
									{'name': 'Viertelfinale', 'order': '5'}, \
									{'name': 'Halbfinale', 'order': '6'}, \
									{'name': 'Finale', 'order': '7'}]

	def return_new_round_id(self, br, roundName):
		"""Returns the new round_id by year.
		"""
		for link in br.links():
			if '+' in link.text and roundName in link.text:
				hsRoundId = link.url.split('round_id=')[1].split('&matchday')[0]
				return hsRoundId
		return None

	def import_round(self, row, adminUrl):
		"""Imports a new round and returns the round_id.
		"""
		importUrl = adminUrl + self.roundUrlAppendixBeforeCompetitionId + row[4] + self.roundUrlAppendixBeforeSeasonId + row[9]
		print(importUrl)
		br = admin_handler.AdminHandler().return_gs_admin_content(importUrl)
		br.form = list(br.forms())[0]
		roundName = row[8]
		for nameAndOrder in self.roundNamesAndOrders:
			if roundName == nameAndOrder['name']:
				roundOrder = nameAndOrder['order']
		br.form.find_control('req[name]').value = roundName
		br.form.find_control('req[round_order]').value = roundOrder
		br.form.find_control('req[round_mode_id]').items[13].selected = True
		br.submit()
		roundId = self.return_new_round_id(br, roundName)
		br.close()
		return roundId

	def import_rounds(self, target):
		"""Imports all new rounds and returns a list containing all rounds with round_ids.
		"""
		adminUrl = admin_handler.AdminHandler().return_admin_url(target)
		rounds = csv_handler.CsvHandler().read_csv(self.roundsPath, 'r', 'latin-1', ',', '|', '2')
		for row in rounds:
			roundId = self.import_round(row, adminUrl)
			row.append(roundId)
		return rounds

	def write_csv(self, target, outputPath):
		"""Writes one csv document containing all different rounds (containing round_ids).
		"""
		roundsWithRoundIds = self.import_rounds(target)
		csv_handler.CsvHandler().create_csv(roundsWithRoundIds, outputPath)
		return outputPath

if __name__ == '__main__':
	RoundsCreator().write_csv('endstand', '../data/allRoundsWithRoundIds.csv')
