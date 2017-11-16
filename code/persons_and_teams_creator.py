#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# mechanize only works in python2

import csv_handler
import admin_handler

class PersonsAndTeamsCreator():
	"""Creates Persons and Teams.
	"""

	def __init__(self):
		self.profilesPath = '../data/allProfilesWithSeasonIds.csv'
		self.blankPersonUrlAppendix = '/admin/person.php?sport_id=5&k=2&person_id='

	def return_profile_data(self, profile):
		"""Returns information of a player profile.
		"""
		csvPreName = profile[1]
		csvLastName = profile[2]
		csvBirthDate = profile[4]
		csvCountry = profile[5]
		csvGender = profile[6]
		csvSeasonIds = profile[8]

		birthDay = csvBirthDate[-2:]
		birthMonth = csvBirthDate[4:6]
		birthYear = csvBirthDate[0:4]

		return {'preName': csvPreName, 'lastName': csvLastName, 'country': csvCountry, 'gender': csvGender, 'birthDay': birthDay, 'birthMonth': birthMonth, 'birthYear': birthYear, 'seasonIds': csvSeasonIds}

	def create_new_person(self, profile, adminUrl):
		"""Creates a new person and returns the person_id and all depending season_ids.
		"""
		profileData = self.return_profile_data(profile)
		importUrl = adminUrl + self.blankPersonUrlAppendix
		br = admin_handler.AdminHandler().return_gs_admin_content(importUrl)
		br.form = list(br.forms())[0]

		br.form.find_control('req[firstname]').value = profileData['preName']
		br.form.find_control('req[surname]').value = profileData['lastName']
		br.form.find_control('req[fullname]').value = profileData['preName'] + ' ' + profileData['lastName']
		br.form.find_control('req[birthday_day]').value = profileData['birthDay']
		br.form.find_control('req[birthday_month]').value = profileData['birthMonth']
		br.form.find_control('req[birthday_year]').value = profileData['birthYear']

		if profileData['gender'] == 'atp':
			br.form.find_control('req[gender]').items[0].selected = True
		elif profileData['gender'] == 'wta':
			br.form.find_control('req[gender]').items[1].selected = True

		for item in br.form.find_control('req[rel_country_ids][]').items:
			if '- ' + profileData['country'] + ' -' in item.get_labels()[0].text:
				item.selected = True

		response = br.submit()
		personId = response.read().split('Person ID ')[1].split(' ')[0]
		br.close()

		return {'personId': personId, 'seasonIds': profileData['seasonIds']}

	def create_new_person_and_team(self, profile, target):
		"""dev
		"""
		adminUrl = admin_handler.AdminHandler().return_admin_url(target)
		teamId = 'xyz'
		personData = self.create_new_person(profile, adminUrl)
		personId = personData['personId']
		seasonIds = personData['seasonIds']
		return teamId

	def add_seasons(self):
		"""dev
		"""
		return None

	def return_all_profiles_with_team_ids(self, target):
		"""Returns a list with all profiles containing team_ids.
		"""
		profiles = csv_handler.CsvHandler().read_csv(self.profilesPath, 'r', 'latin-1', ',', '|', '2')
		for profile in profiles:
			if profile[7] == '0':
				teamId = self.create_new_person_and_team(profile, target)
				profile[7] = teamId
			self.add_seasons()
			break
		return profiles


	def write_csv(self, target):
		"""dev
		"""
		profiles = self.return_all_profiles_with_team_ids(target)



if __name__ == '__main__':
	PersonsAndTeamsCreator().write_csv('', '')
