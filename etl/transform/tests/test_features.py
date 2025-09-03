import unittest
from ..features import _GetFeatures
from ..clean import _CleanData


class Test_features(unittest.TestCase):

    def setUp(self) -> None:
        self._getFeatures = _GetFeatures()
        self._cleanData = _CleanData()


    def test_listDataFiles(self):

        files = self._getFeatures._list_data_files()
#        print(files)

    def test_selectCurrentFile(self):
        files = self._getFeatures._list_data_files()
        file = self._getFeatures._select_current_file(files)
        print(file)


if __name__ == "__main__":
    unittest.main(verbosity=1)