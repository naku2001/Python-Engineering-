# Author: Perfect Makuwerere
# Date: 02/18/2026
# Description: Unit tests for pyramidArea.py using PyTest.

import pytest
import pyramidArea as pa

def test_calcBaseArea():
    assert pa.calcBaseArea(15) == 225

@pytest.mark.xfail(reason="Input should not be text")
def test_calcBaseAreaText():
    pa.calcBaseArea("5")

def test_calcSideAreaBetween():
    result = pa.calcSideArea(15, 5)
    assert 270.41 < result < 270.42

def test_calcSideAreaRound():
    result = pa.calcSideArea(10, 3)
    assert round(result, 2) == 116.62

@pytest.mark.skip(reason="Only prints text to the screen")
def test_prntSurfArea():
    pa.prntSurfArea(225, 270.41)