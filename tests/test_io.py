"""io unit tests."""
from pathlib import Path
import pytest

from raynbow import io

data_root = Path(__file__).parent / 'io_files'


def test_read_oceanoptics_functions():
    # file, has 2048 pixels
    p = data_root / 'valid_sample_oceanoptics.txt'
    data = io.read_oceanoptics(p)

    # returns dict with wvl, value keys
    assert 'wvl' in data
    assert 'values' in data

    # data is of the proper length
    assert len(data['wvl'] == 2048)
    assert len(data['values'] == 2048)

    # data begins and ends with correct values
    assert data['wvl'][0] == 178.179
    assert data['values'][0] == 556.52

    assert data['wvl'][-1] == 871.906
    assert data['values'][-1] == 84.35


def test_read_oceanoptics_raises_for_invalid():
    p = data_root / 'invalid_sample_oceanoptics.txt'
    with pytest.raises(IOError):
        io.read_oceanoptics(p)
