#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

import profiles_and_matches_collector
import os
import unittest
import csv_handler

class TestProfilesAndMatchesCollector(unittest.TestCase):
    """Unittests for the class ProfilesAndMatchesCollector.
    """

    def test_return_matches_csv_paths_for_single_gender(self):
        """Do both genders return strings (known data -> 50)?
        """
        # Unknown data:
        #self.assertGreater(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_matches_csv_paths_for_single_gender({'source': '/tennis_atp-master/', 'id': 'atp'})), 0)
        #self.assertGreater(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_matches_csv_paths_for_single_gender({'source': '/tennis_wta-master/', 'id': 'wta'})), 0)
        # Known data:
        self.assertEqual(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_matches_csv_paths_for_single_gender({'source': '/tennis_atp-master/', 'id': 'atp'})), 50)
        self.assertEqual(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_matches_csv_paths_for_single_gender({'source': '/tennis_wta-master/', 'id': 'wta'})), 50)

    def test_return_matches_csv_paths(self):
        """Do we get the sum of strings in comparison to both genders?
        """
        self.assertEqual(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_matches_csv_paths()), len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_matches_csv_paths_for_single_gender({'source': '/tennis_wta-master/', 'id': 'wta'})) + len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_matches_csv_paths_for_single_gender({'source': '/tennis_atp-master/', 'id': 'atp'})))

    def test_return_csv_contents(self):
        """Do we get the sum of csv contents in comparison to both genders?
        """
        self.assertEqual(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_csv_contents()), len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_matches_csv_paths_for_single_gender({'source': '/tennis_wta-master/', 'id': 'wta'})) + len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_matches_csv_paths_for_single_gender({'source': '/tennis_atp-master/', 'id': 'atp'})))

    def test_append_absent_players(self):
        """Does the function append all absent players? Does the function only append absent players?
        """
        # Test data set:
        row1 = ['0','TURNIER_BLA','2','3','4','5','6','id_w_1','8','9','winner_1','11','12','13','14','15','16','id_l_1','18','19','loser_1']
        row2 = ['0','TURNIER_BLA','2','3','4','5','6','id_w_2','8','9','winner_2','11','12','13','14','15','16','id_l_2','18','19','loser_2']
        row3 = ['0','TURNIER_BLA','2','3','4','5','6','id_w_1','8','9','winner_1','11','12','13','14','15','16','id_l_3','18','19','loser_3']
        playerList = []
        self.assertEqual(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().append_absent_players(row1, 1, playerList, ['TURNIER_BLA'], 7, 10, 17, 20)), 2)
        self.assertEqual(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().append_absent_players(row2, 1, playerList, ['TURNIER_BLA'], 7, 10, 17, 20)), 4)
        self.assertEqual(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().append_absent_players(row3, 1, playerList, ['TURNIER_BLA'], 7, 10, 17, 20)), 5)

    def test_return_all_different_players_and_matches(self):
        """Do we get a list of different persons (known data -> 3781 and 44969)?
        """
        # Unknown data:
        #self.assertGreater(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_all_different_players_and_matches()['playerList']), 0)
        #self.assertGreater(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_all_different_players_and_matches()['matchesList']), 0)
        # Known data:
        self.assertEqual(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_all_different_players_and_matches()['playerList']), 3781)
        self.assertEqual(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_all_different_players_and_matches()['matchesList']), 44969)

    def test_append_gender(self):
        """Does the function appends the gender id?
        """
        # Test data:
        profileList = [['']]
        gender = {'id': 'atp'}
        self.assertEqual(profiles_and_matches_collector.ProfilesAndMatchesCollector().append_gender(profileList, gender)[0][1], 'atp')

    def test_return_all_different_profiles(self):
        """Do we get a list of persons profiles (known data -> 73422)?
        """
        # Unknown data:
        #self.assertGreater(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_all_different_profiles()), 0)
        # Known data:
        self.assertEqual(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_all_different_profiles()), 73422)

    def test_identify_same_profile(self):
        """Does the function only match compossible data (caution: same id can occur twice, male and female)?
        """
        # Test data set:
        allProfiles = [['123', 'Cooler', 'Typ'], ['123', 'Netter', 'Typ']]
        gradSlamPlayer1 = {'id': '123', 'name': 'Cooler Typ'}
        gradSlamPlayer2 = {'id': '123', 'name': 'Netter Typ'}
        gradSlamPlayer3 = {'id': '456', 'name': 'Netter Typ'}
        self.assertEqual(profiles_and_matches_collector.ProfilesAndMatchesCollector().identify_same_profile(allProfiles, gradSlamPlayer1)[1], 'Cooler')
        self.assertEqual(profiles_and_matches_collector.ProfilesAndMatchesCollector().identify_same_profile(allProfiles, gradSlamPlayer2)[1], 'Netter')
        self.assertEqual(profiles_and_matches_collector.ProfilesAndMatchesCollector().identify_same_profile(allProfiles, gradSlamPlayer3), None)

    def test_return_all_grand_slam_profiles_and_matches(self):
        """Do we get a list of all grand slam persons profiles and matches (known data -> 3781 and 44969)?
        """
        # Unknown data:
        #self.assertGreater(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_all_grand_slam_profiles_and_matches()['allGrandSlamProfiles']), 0)
        #self.assertGreater(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_all_grand_slam_profiles_and_matches()['allGrandSlamMatches']), 0)
        # Known data:
        self.assertEqual(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_all_grand_slam_profiles_and_matches()['allGrandSlamProfiles']), 3781)
        self.assertEqual(len(profiles_and_matches_collector.ProfilesAndMatchesCollector().return_all_grand_slam_profiles_and_matches()['allGrandSlamMatches']), 44969)

    def test_write_csvs(self):
        """Do we write one csv file with person profile rows and one with match rows (known data -> 3781 and 44969)?
        """
        paths = profiles_and_matches_collector.ProfilesAndMatchesCollector().write_csvs('../data/test_allGrandSlamdifferent.csv', '../data/test_allGrandSlamMatches.csv')
        csvContentProfiles = csv_handler.CsvHandler().read_csv(paths['outputPathProfiles'], 'r', 'latin-1')
        csvContentMatches = csv_handler.CsvHandler().read_csv(paths['outputPathMatches'], 'r', 'latin-1')
        os.remove('../data/test_allGrandSlamdifferent.csv')
        os.remove('../data/test_allGrandSlamMatches.csv')
        # Unknown data:
        #self.assertGreater(len(csvContentProfiles), 0)
        #self.assertGreater(len(csvContentMatches), 0)
        # Known data:
        self.assertEqual(len(csvContentProfiles), 3781)
        self.assertEqual(len(csvContentMatches), 44969)

if __name__ == '__main__':
    os.system('radon cc -a profiles_and_matches_collector.py')
    print('')
    unittest.main()
