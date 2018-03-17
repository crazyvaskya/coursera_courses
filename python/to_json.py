import json
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapper


@to_json
def f():
    return {
        'key': 'data'
    }


def main():
    print(f(), f.__name__)
