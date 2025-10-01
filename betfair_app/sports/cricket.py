from betfair_app.utils import get_today_start_end

def get_cricket_event_type_id():
    return "4"

def list_cricket_matches_today(client, max_results=50):
    dr = get_today_start_end()
    return client.betting.list_market_catalogue(
        filter={
            "eventTypeIds": [get_cricket_event_type_id()],
            "marketStartTime": dr,
            "marketTypeCodes": ["MATCH_ODDS"]
        },
        max_results=str(max_results),
        market_projection=[
            "COMPETITION",
            "EVENT",
            "RUNNER_DESCRIPTION",
            "MARKET_START_TIME"
        ]
    )
