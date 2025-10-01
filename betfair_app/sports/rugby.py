from betfair_app.utils import get_today_start_end

def get_rugby_event_type_id():
    return "5"

def list_rugby_matches_today(client, max_results=50):
    dr = get_today_start_end()
    return client.betting.list_market_catalogue(
        filter={
            "eventTypeIds": [get_rugby_event_type_id()],
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
