from datetime import datetime
from zoneinfo import ZoneInfo

tz_vn = ZoneInfo("Asia/Ho_Chi_Minh")
now_vn = datetime.now(tz_vn)
print(now_vn.strftime("%Y-%m-%d %H:%M:%S"))

dt = datetime(2025, 11, 15, 3, 1, 5, tzinfo=tz_vn)
print(dt.strftime("%Y-%m-%d %H:%M:%S"))

diff = now_vn - dt
print(diff.total_seconds())