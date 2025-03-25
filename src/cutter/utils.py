import re

def time_str_to_sec(time_str:str):
    match=re.search(r"(?P<hour>[\d]+):(?P<min>[\d]+):(?P<sec>[\d]+)",time_str)
    match_m=re.search(r"(?P<min>[\d]+):(?P<sec>[\d]+)",time_str)
    if match:
        return int(match.group('hour'))*60*60 + int( match.group('min'))*60 + int(match.group('sec'))
    elif match_m:
        return int( match_m.group('min'))*60 + int(match_m.group('sec'))
    else:
        return 0