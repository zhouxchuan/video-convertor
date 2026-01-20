# -*- coding: utf-8 -*-

from datetime import datetime,timedelta

def seconds_to_time(seconds):
    time_delta = timedelta(seconds=float(seconds))
    hrs, remainder = divmod(time_delta.seconds, 3600)
    mins, secs = divmod(remainder, 60)
    return f"{hrs:02d}:{mins:02d}:{secs:02d}"

def timestr_to_seconds(time_str):
    try:
        datetime.strptime(time_str, '%H:%M:%S.%f')
        h,m,s=time_str.strip().split(":")
        td = timedelta(hours=float(h), minutes=float(m),seconds=float(s))
        return td.total_seconds()
    except ValueError:
        return -1

def convert_bytes(size):
    value = float(size)
    for x in ["bps","k","M","G","T"]:
        if value < 1024.0:
            return "%3.1f %s" % (value,x)
        value /=1024.0
    return value

def get_now_timestamp(format):
    now = datetime.now()
    return now.strftime(format)

def is_empty_string(s):
    if s.strip() == None or s.strip() == "":
        return True
    else:
        return False