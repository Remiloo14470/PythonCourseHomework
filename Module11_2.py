import inspect
from pprint import pprint


def introspection_info(obj):
    methods = [m[0] for m in inspect.getmembers(obj, predicate=inspect.isfunction(obj))]
    keys_dict = ['type', 'attributes', 'methods', 'module']
    values_dict = [type(obj), dir(obj), methods, inspect.getmodule(introspection_info)]
    obj_dict = dict(zip(keys_dict, values_dict))
    return obj_dict


number_info = introspection_info(42)
pprint(number_info)