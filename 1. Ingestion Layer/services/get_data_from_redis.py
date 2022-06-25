import json
import redis


def get_dicts_from_redis():
    """This function returns a list of tuples. The first element of the tuple will be the topic, the second will be the
     dictionary with all the values. The tuple also has a third element, which is the redis key corresponding to the record piece.
     @:returns a tuple of lists. the first element is a list of tuples, the second a list of keys"""
    r = redis.StrictRedis(host='redis')
    keys = r.keys('*(*)*')  # get all keys available that has name(kind).format
    values = list()
    if not keys:
        return False, False
    for key in keys:
        # we need to understand the topic
        redis_value = r.get(key).decode(encoding='utf-8')
        if b"(Questura)" in key:  # it's a bank
            topic = "questura"
        elif b"(Broker)" in key:
            topic = "broker"
        elif b"(Bank)" in key:
            topic = "bank"
        else:
            topic = "statement"

        redis_value = json.loads(redis_value)  # should be a list of dicts
        for k, el in redis_value.items():
            values.append((topic, el, key))
    return values, keys

