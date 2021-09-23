import urllib.error
from io import BytesIO
from unittest import mock
from unittest.mock import MagicMock, patch

import pytest

from homework4.task02 import count_dots_on_i


@patch('urllib.request.urlopen')
def test_count_dots_positive_case_20_1(mock_urlopen):
    response = MagicMock()
    response.read.return_value = b'aib' * 20
    mock_urlopen.return_value = response
    result = count_dots_on_i('something')

    assert result == 20


@patch('urllib.request.urlopen')
def test_count_dots_error_1(mock_urlopen):
    # response = MagicMock(side_effect=Exception(urllib.error.URLError))
    mock_urlopen.side_effect = urllib.error.URLError('f')

    with pytest.raises(ValueError):
        count_dots_on_i('foo')
