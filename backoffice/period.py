from datetime import datetime, timedelta

NOW = datetime.now()

# get the first and last day of the previous month
END = NOW.replace(day=1, hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
START = END.replace(day=1)
