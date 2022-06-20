import json
import redis


def get_dicts_from_redis():
    """This function returns a list of tuples. The first element of the tuple will be the topic, the second will be the
     dictionary with all the values.
     @:returns list of tuples."""
    r = redis.StrictRedis(host='localhost')
    keys = r.keys('*')  # get all keys available at the moment
    values = list()
    for key in keys:
        # we need to understand the topic
        redis_value = r.get(key).decode(encoding='utf-8')
        if "bank_name" in redis_value:  # it's a bank
            topic = "bank"
        elif "broker_name" in redis_value:
            topic = "broker"
        else:
            topic = "questura"

        redis_value = json.loads(redis_value)  # should be a list of dicts
        for key, el in redis_value.items():
            values.append((topic, el))
    return values
