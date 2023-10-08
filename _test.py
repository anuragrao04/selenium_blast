import pytest
from selenium_script import test_leaderboard_load

@pytest.mark.parametrize('i', range(2))
def test_concurrent(i):
   test_leaderboard_load()
