from datetime import datetime

now = datetime.now()

unix_time = now.timestamp()

unix_time_comma = "{:,}".format(round(unix_time, 4))

unix_time_scientific_notation = ("{:e}").format(unix_time)

print(f"Seconds since January 1, 1970: {unix_time_comma} or {unix_time_scientific_notation} in scientific notation")

print(now.strftime("%b %d %Y"))