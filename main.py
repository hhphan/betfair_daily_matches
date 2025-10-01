#!/usr/bin/env python3

from betfair_app.client import BetfairClient
from betfair_app.query import (
    list_matches_today,
    list_all_matches_today,
    get_matches_by_date_range,
    get_competitions_today,
    search_matches_by_team_name,
)
from betfair_app.utils import format_match_time, get_date_display


def display_matches(matches, title="Matches"):
    print(f"\n=== {title} ===")
    if not matches:
        print("No matches found.")
        return

    for i, market in enumerate(matches, 1):
        sport = getattr(market, 'sport_type', 'Unknown')
        start_time = format_match_time(market.market_start_time)
        print(f"{i:2d}. [{sport}] {market.event.name}")
        if hasattr(market, 'competition') and market.competition:
            print(f"    Competition: {market.competition.name}")
        print(f"    Market: {market.market_name}")
        print(f"    Start Time: {start_time}")
        print(f"    Market ID: {market.market_id}")
        if hasattr(market, 'runners') and market.runners:
            runners = [r.runner_name for r in market.runners]
            print(f"    Runners: {' vs '.join(runners[:2])}")
        print()


def display_competitions(comps, sport_name):
    print(f"\n=== {sport_name.title()} Competitions Today ===")
    if not comps:
        print("No competitions found.")
        return

    for i, comp in enumerate(comps, 1):
        print(f"{i:2d}. {comp.competition.name}")
        print(f"    Region: {getattr(comp, 'competition_region', 'N/A')}")
        print(f"    Market Count: {comp.market_count}")
        print()


def interactive_menu():
    while True:
        print("\n" + "=" * 50)
        print("    BETFAIR DAILY MATCH QUERY TOOL")
        print("=" * 50)
        print("1. All matches today (all sports)")
        print("2. Football matches today")
        print("3. Tennis matches today")
        print("4. Custom date range")
        print("5. View competitions today")
        print("6. Search matches by team/player name")
        print("7. Exit")

        choice = input("\nSelect option (1-7): ").strip()
        if choice == "7":
            print("Goodbye!")
            break

        try:
            with BetfairClient() as client:
                handle_menu_choice(client, choice)
        except Exception as e:
            print(f"Error: {e}")
            print("Please check your credentials and try again.")


def handle_menu_choice(client, choice):
    if choice == "1":
        matches = list_all_matches_today(client, max_results=100)
        display_matches(matches, "All Matches Today")

    elif choice == "2":
        matches = list_matches_today(client, "football", max_results=50)
        display_matches(matches, "Football Matches Today")

    elif choice == "3":
        matches = list_matches_today(client, "tennis", max_results=50)
        display_matches(matches, "Tennis Matches Today")

    elif choice == "4":
        sport = input("Enter sport (football/tennis/cricket/rugby): ").strip().lower()
        days = int(input("Days ahead (0=today, 1=tomorrow): ").strip())
        matches = get_matches_by_date_range(client, sport, days, max_results=50)
        display_matches(matches, f"{sport.title()} Matches - {get_date_display(days)}")

    elif choice == "5":
        sport = input("Enter sport for competitions: ").strip().lower()
        comps = get_competitions_today(client, sport)
        display_competitions(comps, sport)

    elif choice == "6":
        team = input("Enter team/player name: ").strip()
        sport = input("Enter sport or press Enter for all: ").strip().lower() or None
        matches = search_matches_by_team_name(client, team, sport)
        display_matches(matches, f"Matches for '{team}'")

    else:
        print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    interactive_menu()
