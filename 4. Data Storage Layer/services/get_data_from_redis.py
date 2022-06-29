import json
import redis


def get_dicts_from_redis(table: str):
    """
     @:returns a tuple of lists. the first element is a list of dicts, the second a list of keys"""
    r = redis.StrictRedis(host='localhost')
    keys = r.keys('('+table+'-report-row)*')  # get all keys available for that table
    values = list()
    if not keys:
        print("No keys for that table")
        return False, False
    for key in keys:
        # we need to understand the topic
        redis_value = r.get(key).decode(encoding='utf-8')

        redis_value = json.loads(redis_value)  # should be a dict
        values.append(redis_value)
    return values, keys



