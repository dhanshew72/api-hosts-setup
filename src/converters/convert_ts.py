from datetime import datetime


def convert_utc_ts(ts):
    """
    Helper function to convert string representation of UTC timestamps to a datetime format
    :param ts: string utc timestamp
    :return: datetime timestamp
    """
    return datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ")
