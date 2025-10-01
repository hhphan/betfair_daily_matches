from betfair_app.utils import get_today_start_end, get_custom_date_range

SPORT_EVENT_TYPE_IDS = {
    "football": "1",
    "tennis":   "2",
    "cricket":  "4",
    "rugby":    "5",
}

def list_matches(
    client, sport, market_types=None, countries=None,
    in_play=False, days_ahead=0, max_results=50
):
    etid = SPORT_EVENT_TYPE_IDS.get(sport)
    if not etid:
        raise ValueError(f"Unsupported sport: {sport}")
    dr  = None if in_play else get_custom_date_range(days_ahead)
    flt = {
        "eventTypeIds":    [etid],
        "marketTypeCodes": market_types or ["MATCH_ODDS"],
    }
    if countries:
        flt["marketCountries"] = countries
    if dr:
        flt["marketStartTime"] = dr
    if in_play:
        flt["inPlayOnly"] = True

    return client.betting.list_market_catalogue(
        filter=flt,
        max_results=str(max_results),
        market_projection=[
            "COMPETITION",
            "EVENT",
            "RUNNER_DESCRIPTION",
            "MARKET_START_TIME",
        ],
    )

def list_matches_today(client, sport, market_types=None, countries=None, max_results=50):
    return list_matches(client, sport, market_types, countries, False, 0, max_results)

def list_all_matches_today(client, max_results=100):
    allm = []
    half = max_results // len(SPORT_EVENT_TYPE_IDS)
    for sp in SPORT_EVENT_TYPE_IDS:
        try:
            ms = list_matches_today(client, sp, max_results=half)
            for m in ms:
                m.sport_type = sp.title()
            allm.extend(ms)
        except:
            pass
    return sorted(allm, key=lambda x: x.market_start_time or "")

def get_matches_by_date_range(client, sport, days_ahead, market_types=None, countries=None, max_results=50):
    return list_matches(client, sport, market_types, countries, False, days_ahead, max_results)

def get_competitions_today(client, sport):
    etid = SPORT_EVENT_TYPE_IDS.get(sport)
    if not etid:
        raise ValueError(f"Unsupported sport: {sport}")
    return client.betting.list_competitions(
        filter={"eventTypeIds":[etid], **get_today_start_end()}
    )

def search_matches_by_team_name(client, team_name, sport=None, max_results=100):
    results = []
    sports = [sport] if sport else SPORT_EVENT_TYPE_IDS.keys()
    for sp in sports:
        try:
            ms = list_matches_today(client, sp, max_results=max_results)
            for m in ms:
                if team_name.lower() in m.event.name.lower():
                    m.sport_type = sp.title()
                    results.append(m)
        except:
            pass
    return results
