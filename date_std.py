from datetime import datetime as dt
import time


my_date = dt.fromtimestamp(1647892012)
print(my_date)

now = dt.now()
print(now)
print(f"Текущее время {now:%d.%m.%Y %H:%M}")
