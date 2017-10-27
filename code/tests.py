#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import profiles
import os
import unittest

def test_cyclomatic_complexity(pyDoc):
    """Checks the cyclomatic complexity of all classes, functions and methods in a give python document.
    """
    os.system('radon cc -a ' + pyDoc)
    print('')

class TestProfileHandler(unittest.TestCase):
    """Unittests for the class ProfileHandler.
    """

    def test_return_matches_csv_paths_for_single_gender(self):
        """Do both genders return strings (known data -> 50)?
        """
        # Unknown data:
        #self.assertGreater(len(profiles.ProfileHandler().return_matches_csv_paths_for_single_gender({'source': '/tennis_atp-master/', 'id': 'atp'})), 0)
        #self.assertGreater(len(profiles.ProfileHandler().return_matches_csv_paths_for_single_gender({'source': '/tennis_wta-master/', 'id': 'wta'})), 0)
        # Known data:
        self.assertEqual(len(profiles.ProfileHandler().return_matches_csv_paths_for_single_gender({'source': '/tennis_atp-master/', 'id': 'atp'})), 50)
        self.assertEqual(len(profiles.ProfileHandler().return_matches_csv_paths_for_single_gender({'source': '/tennis_wta-master/', 'id': 'wta'})), 50)

    def test_return_matches_csv_paths(self):
        """Do we get the sum of strings in comparison to both genders?
        """
        self.assertEqual(len(profiles.ProfileHandler().return_matches_csv_paths()), len(profiles.ProfileHandler().return_matches_csv_paths_for_single_gender({'source': '/tennis_wta-master/', 'id': 'wta'})) + len(profiles.ProfileHandler().return_matches_csv_paths_for_single_gender({'source': '/tennis_atp-master/', 'id': 'atp'})))

    def test_return_csv_contents(self):
        """Do we get the sum of csv contents in comparison to both genders?
        """
        self.assertEqual(len(profiles.ProfileHandler().return_csv_contents()), len(profiles.ProfileHandler().return_matches_csv_paths_for_single_gender({'source': '/tennis_wta-master/', 'id': 'wta'})) + len(profiles.ProfileHandler().return_matches_csv_paths_for_single_gender({'source': '/tennis_atp-master/', 'id': 'atp'})))

    def test_append_absent_players(self):
        """Does the function append all absent players? Does the function only append absent players?
        """
        # Test data set:
        row1 = ['0','TURNIER_BLA','2','3','4','5','6','id_w_1','8','9','winner_1','11','12','13','14','15','16','id_l_1','18','19','loser_1']
        row2 = ['0','TURNIER_BLA','2','3','4','5','6','id_w_2','8','9','winner_2','11','12','13','14','15','16','id_l_2','18','19','loser_2']
        row3 = ['0','TURNIER_BLA','2','3','4','5','6','id_w_1','8','9','winner_1','11','12','13','14','15','16','id_l_3','18','19','loser_3']
        playerList = []
        self.assertEqual(len(profiles.ProfileHandler().append_absent_players(row1, 1, playerList, ['TURNIER_BLA'], 7, 10, 17, 20)), 2)
        self.assertEqual(len(profiles.ProfileHandler().append_absent_players(row2, 1, playerList, ['TURNIER_BLA'], 7, 10, 17, 20)), 4)
        self.assertEqual(len(profiles.ProfileHandler().append_absent_players(row3, 1, playerList, ['TURNIER_BLA'], 7, 10, 17, 20)), 5)

    def test_return_all_different_players(self):
        """Do we get a list of different persons (known data -> 3653)?
        """
        # Unknown data:
        #self.assertGreater(len(profiles.ProfileHandler().return_all_different_players()), 0)
        # Known data:
        self.assertEqual(len(profiles.ProfileHandler().return_all_different_players()), 3653)

    def test_append_gender(self):
        """Does the function appends the gender id?
        """
        # Test data:
        profileList = [['']]
        gender = {'id': 'atp'}
        self.assertEqual(profiles.ProfileHandler().append_gender(profileList, gender)[0][1], 'atp')

    def test_return_all_different_profiles(self):
        """Do we get a list of persons profiles (known data -> 73422)?
        """
        # Unknown data:
        #self.assertGreater(len(profiles.ProfileHandler().return_all_different_profiles()), 0)
        # Known data:
        self.assertEqual(len(profiles.ProfileHandler().return_all_different_profiles()), 73422)

    def test_identify_same_profile(self):
        """Does the function only match compossible data?
        """
        # Test data set:
        allProfiles = [['123', 'Cooler', 'Typ'], ['123', 'Netter', 'Typ']]
        gradSlamPlayer1 = {'id': '123', 'name': 'Cooler Typ'}
        gradSlamPlayer2 = {'id': '456', 'name': 'Netter Typ'}
        self.assertNotEqual(profiles.ProfileHandler().identify_same_profile(allProfiles, gradSlamPlayer1), None)
        self.assertEqual(profiles.ProfileHandler().identify_same_profile(allProfiles, gradSlamPlayer2), None)

    def test_return_all_grand_slam_profiles(self):
        """Do we get a list of all grand slam persons profiles (known data -> 3653)?
        """
        # Unknown data:
        #self.assertGreater(len(profiles.ProfileHandler().return_all_grand_slam_profiles()), 0)
        # Known data:
        self.assertEqual(len(profiles.ProfileHandler().return_all_grand_slam_profiles()), 3653)

if __name__ == '__main__':
    test_cyclomatic_complexity('csv_handler.py')
    test_cyclomatic_complexity('profiles.py')
    unittest.main()
