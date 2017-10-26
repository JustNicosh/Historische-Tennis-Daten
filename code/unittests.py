#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import unittest
import profiles

class TestProfileHandler(unittest.TestCase):
    """Unittests for the class ProfileHandler.
    """

    def test_return_matches_csv_paths_for_single_gender(self):
        """Do both genders return strings?
        """
        self.assertGreater(len(profiles.ProfileHandler().return_matches_csv_paths_for_single_gender({'source': '/tennis_atp-master/', 'id': 'atp'})), 0)
        self.assertGreater(len(profiles.ProfileHandler().return_matches_csv_paths_for_single_gender({'source': '/tennis_wta-master/', 'id': 'wta'})), 0)


    def test_return_matches_csv_paths(self):
        """Do we get the sum of strings in comparison to both genders?
        """
        self.assertEqual(len(profiles.ProfileHandler().return_matches_csv_paths()), len(profiles.ProfileHandler().return_matches_csv_paths_for_single_gender({'source': '/tennis_wta-master/', 'id': 'wta'})) + len(profiles.ProfileHandler().return_matches_csv_paths_for_single_gender({'source': '/tennis_atp-master/', 'id': 'atp'})))

if __name__ == '__main__':
	unittest.main()
