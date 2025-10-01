from betfair_app.sports.football import get_football_event_type_id

def test_ft_id():
    assert get_football_event_type_id() == "1"
