import datetime
import tzlocal
import pytz

def get_datetime_in_LA():
	utc_dt = datetime.datetime.now(datetime.timezone.utc)
	return utc_dt.astimezone(pytz.timezone('US/Pacific-New'))

def get_formatted_timestamp_in_LA():
	return get_datetime_in_LA().strftime('[%Y-%m-%d %H:%M:%S]')