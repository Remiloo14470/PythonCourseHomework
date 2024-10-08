import inspect
from pprint import pprint


def introspection_info(obj):

    info = {}

    info['type'] = type(obj).__name__

    all_attributes = dir(obj)

    attributes = [attr for attr in all_attributes if not callable(getattr(obj, attr))]
    methods = [method for method in all_attributes if callable(getattr(obj, method))]

    info['attributes'] = attributes
    info['methods'] = methods

    info['module'] = obj.__module__ if hasattr(obj, '__module__') else 'No module found'

    info['doc'] = obj.__doc__ if hasattr(obj, '__doc__') else 'No documentation available'

    return info


number_info = introspection_info(42)
print(number_info)
