import unittest
import sys
sys.path.insert(1, "..")
import datetime
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers


class test_DcgsPythonHelpers(unittest.TestCase):

    def setUp(self):
        self.dcgsHelpers = DcgsPythonHelpers()

    def test_getHashDateFromDate(self):
        datetime_test = datetime.datetime(2017, 11, 28, 23, 55, 59)
        expected_result = '20171128-23h55m59s'
        returned_result = self.dcgsHelpers.getHashDateFromDate(datetime_test)
        self.assertEqual(expected_result, returned_result)
