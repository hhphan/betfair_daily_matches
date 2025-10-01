import re
from datetime import datetime, timedelta
from betfair_app.utils import get_today_start_end, get_custom_date_range, format_match_time

def test_today_format():
    dr = get_today_start_end()
    assert re.match(r"\d{4}-\d{2}-\d{2}T00:00:00\.000Z", dr['from'])
    assert re.match(r"\d{4}-\d{2}-\d{2}T00:00:00\.000Z", dr['to'])

def test_custom_offset():
    dr = get_custom_date_range(1)
    assert dr['from'].startswith((datetime.utcnow().date()+timedelta(days=1)).strftime("%Y-%m-%d"))

def test_format_valid():
    assert format_match_time("2025-10-02T15:30:00.000Z") == "15:30"

def test_format_invalid():
    assert format_match_time(None) == "TBD"
    assert format_match_time("bad") == "TBD"
