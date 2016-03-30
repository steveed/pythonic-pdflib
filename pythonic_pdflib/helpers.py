from .options import BaseOption
import collections

import sys

__all__ = ['to_optlist', 'default']

if sys.version_info[0] == 2:
    string_types = basestring,
    def iteritems(d):
        return d.iteritems()
else:
    string_types = str,
    def iteritems(d):
        return d.items()

def to_optlist(options=None):
    """
    Convert a dict of options to a PDFlib optlist string.
    """
    if not options:
        return ''
    elif isinstance(options, string_types):
        return options
    elif isinstance(options, dict):
        return " ".join(optlist_value(key, value) for key, value in iteritems(options))
    elif isinstance(options, collections.Iterable):
        return " ".join("{%s}" % to_optlist(option) for option in options)
    else:
        raise AttributeError("Unknown class '%s' for options attribute." % options.__class__)

def optlist_value(key, value):
    if isinstance(value, BaseOption):
        if value.use == BaseOption.USE_VALUE:
            return str(value)
        elif value.use == BaseOption.USE_KEY:
            return str(key)
        else:
            return "%s=%s" % (key, value)
    elif value is None:
        return key
    elif value is True:
        return "%s=true" % key
    elif value is False:
        return "%s=false" % key
    elif isinstance(value, string_types):
        return "%s=%s" % (key, value)
    elif isinstance(value, collections.Iterable):
        return "%s={%s}" % (key, " ".join("%s" % v for v in value))
    else:
        return "%s=%s" % (key, value)

def default(value, default=None):
    if value is None:
        return default
    return value
