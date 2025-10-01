from betfair_app.sports.tennis import get_tennis_event_type_id

def test_tt_id():
    assert get_tennis_event_type_id() == "2"
