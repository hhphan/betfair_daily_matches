# Betfair Daily Matches – Quick Start Guide

## Project Overview

**Betfair Daily Matches** is a modular Python application that connects to the Betfair Exchange API to:

- Fetch and display **today’s** sports markets (Football, Tennis, Cricket, Rugby)
- Query markets for a **custom date range**
- Filter by **market type** (e.g., Match Odds, Over/Under)
- Restrict to **specific countries**
- Show **live (in-play)** markets
- Search for matches by **team/player name**
- List today’s **competitions** per sport

It features:
- An **interactive CLI** (`main.py`) with menu-driven options
- A **clean package** (`betfair_app/`) encapsulating config, client, utilities, query logic, and sport modules
- **Pytest**-based test suite under `tests/`
- Easy extensibility: add new sports or market filters by creating new modules

Follow the sections below to set up, run, and extend the application.

## Project Structure

```
betfair_daily_matches/
├── main.py
├── requirements.txt
├── README.md
├── betfair_app/
│   ├── __init__.py
│   ├── config.py
│   ├── client.py
│   ├── utils.py
│   ├── query.py
│   └── sports/
│       ├── football.py
│       ├── tennis.py
│       ├── cricket.py
│       └── rugby.py
└── tests/
    ├── __init__.py
    ├── test_config.py
    ├── test_query.py
    ├── test_sports_football.py
    ├── test_sports_tennis.py
    └── test_utils.py
```

## 1. Create a Python Virtual Environment

In the project root (`betfair_daily_matches/`), run:

```bash
python3 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

## 2. Install Dependencies

Upgrade pip and install required packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 3. Set Environment Variables

Configure your Betfair credentials and SSL certificate directory. Add the following lines to your shell profile (`~/.bashrc`, `~/.profile`, etc.):

```bash
export BF_USERNAME="your.betfair.username"
export BF_PASSWORD="yourBetfairPassword"
export BF_APP_KEY="YourAppKeyHere"
export BF_CERT_DIR="/path/to/your/certificates"
```

Reload your shell:

```bash
source ~/.bashrc
```

## 4. Verify SSL Certificates

Ensure your certificate directory contains both `.crt` and `.key` files and that the key file has secure permissions:

```bash
ls $BF_CERT_DIR
chmod 600 $BF_CERT_DIR/*.key
```

## 5. Run the Application

Launch the interactive command-line interface:

```bash
python main.py
```

You will see a menu with options:

1. All matches today (all sports)
2. Football matches today
3. Tennis matches today
4. Cricket matches today
5. Rugby matches today
6. Custom date range
7. View competitions today
8. Search matches by team/player name
9. Exit

Enter the number for the desired action and follow the prompts.

## 6. Exit and Deactivate

When finished, choose **Exit** from the menu or press `Ctrl+C`. Then deactivate the virtual environment:

```bash
deactivate
```

## 7. Testing with pytest

A test suite using **pytest** is included under `tests/` — 10 tests across 5 files.

### Test coverage

| File | Tests | What it covers |
|---|---|---|
| `test_config.py` | 2 | Missing env vars raise `ValueError`; all vars present returns `True` |
| `test_query.py` | 2 | `list_matches_today` with a dummy client; invalid sport raises `ValueError` |
| `test_sports_football.py` | 1 | `get_football_event_type_id()` returns `"1"` |
| `test_sports_tennis.py` | 1 | `get_tennis_event_type_id()` returns `"2"` |
| `test_utils.py` | 4 | Date range ISO format, custom offset, valid/invalid time formatting |

### Running tests

```bash
# Run all 10 tests (quiet)
pytest --maxfail=1 --disable-warnings -q

# Verbose output
pytest -v

# Run a single test file
pytest tests/test_utils.py -v

# Run a single test by name
pytest tests/test_config.py::test_missing_env -v
```

Ensure all tests pass before deploying or extending the application.

---
This completes the setup and usage instructions for the Betfair Daily Matches application.