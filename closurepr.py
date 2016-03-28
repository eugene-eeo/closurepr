import sys


IS_PY3 = sys.version_info[0] == 3


def format_funcname(name, args, kwargs):
    varargs = ','.join(repr(v) for v in args)
    kwdargs = ','.join('%s=%r' % (k, kwargs[k]) for k in kwargs)

    return '%s(%s%s)' % (name, varargs, kwdargs)


def rich_repr(fn):
    name = fn.__name__

    def wrapper(*args, **kwargs):
        closure = fn(*args, **kwargs)
        string = format_funcname(name, args, kwargs)
        if IS_PY3:
            closure.__qualname__ = string
        else:
            closure.func_name = string
        return closure
    return wrapper
