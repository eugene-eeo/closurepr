closurepr: debuggable closures
==============================

Provides super lightweight wrappers around functions that return
functions, to make functional programming in Python more friendly:

.. code-block:: python

    >>> from closurepr import rich_repr
    >>> @rich_repr
        def adder(a):
            return lambda b: a+b

    >>> adder(1)
    '<function adder(1) at 0x...>'

You don't strictly need it. But you want it.
