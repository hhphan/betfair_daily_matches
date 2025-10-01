from datetime import datetime, timedelta

def get_today_start_end():
    today = datetime.utcnow().date()
    start = datetime.combine(today, datetime.min.time())
    end   = start + timedelta(days=1)
    return {
        "from": start.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "to":   end.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
    }

def get_custom_date_range(days_ahead=0):
    date  = datetime.utcnow().date() + timedelta(days=days_ahead)
    start = datetime.combine(date, datetime.min.time())
    end   = start + timedelta(days=1)
    return {
        "from": start.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "to":   end.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
    }

def format_match_time(iso_str):
    if not iso_str:
        return "TBD"
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.strftime("%H:%M")
    except:
        return "TBD"

def get_date_display(days_ahead=0):
    if days_ahead == 0:
        return "Today"
    if days_ahead == 1:
        return "Tomorrow"
    return (datetime.utcnow().date() + timedelta(days=days_ahead)).strftime("%Y-%m-%d")
