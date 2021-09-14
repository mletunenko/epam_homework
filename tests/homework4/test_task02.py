import unittest
import urllib.error
from unittest.mock import MagicMock, patch

from homework4.task02 import count_dots_on_i


# create a test class
class TestUrlopen(unittest.TestCase):
    # create a patch deco for urllib.request.urlopen()
    @patch('urllib.request.urlopen')
    def test_count_dots_positive_case_20(self, mock_urlopen):
        # create a mock
        response = MagicMock()
        # create mock methods
        response.read.return_value = b'aib' * 20

        # use a response as a mock
        mock_urlopen.return_value = response

        # call a tested func with mock
        result = count_dots_on_i('something')

        assert result == 20

    # create a patch deco for urllib.request.urlopen()
    @patch('urllib.request.urlopen')
    def test_count_dots_error(self, mock_urlopen):
        # create a mock
        response = MagicMock()
        # raise a Exception with side affect
        response.side_effect = Exception(urllib.error.URLError)

        # use a response as a mock
        mock_urlopen.return_value = response

        # call a tested func with mock
        result = count_dots_on_i('something')

        assert result == 0
