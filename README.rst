closurepr: debuggable closures
==============================

Provides a super lightweight and magical wrapper around functions
that return functions, to make functional programming in Python more
friendly:

.. code-block:: python

    >>> from closurepr import rich_repr
    >>> @rich_repr
        def adder(a):
            return lambda b: a+b

    >>> adder(1)
    '<function adder(1) at 0x...>'

You don't strictly need it. But you want it.

Previous literature:
--------------------

 - http://stackoverflow.com/questions/32284395/should-extra-layers-be-added-just-to-support-repr/32285982
 - https://bugs.python.org/issue24056
