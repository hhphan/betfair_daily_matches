import pytest
from betfair_app.query import list_matches_today, get_matches_by_date_range

class DummyMarket:
    def __init__(self, name):
        self.event = type('E', (), {'name': name})
        self.market_name = "M"
        self.market_id = "X"
        self.market_start_time = None
        self.runners = []

class DummyClient:
    def __init__(self):
        self.betting = self
    def list_market_catalogue(self, filter, max_results, market_projection):
        return [DummyMarket("Test")]

def test_list_f():
    c = DummyClient()
    m = list_matches_today(c, "football", max_results=1)
    assert m[0].event.name == "Test"

def test_invalid():
    with pytest.raises(ValueError):
        get_matches_by_date_range(DummyClient(), "bad", 0)
