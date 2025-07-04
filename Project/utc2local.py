# auxiliary to check timestamps in cache
from datetime import datetime
import pytz

utc_time = datetime.fromisoformat("2025-07-03T23:24:19.357156+00:00")
local_time = utc_time.astimezone()  # auto-converts to local time

print(local_time)
