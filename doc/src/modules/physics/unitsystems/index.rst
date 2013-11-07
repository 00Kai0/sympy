============
Unit systems
============

This module integrates unit systems into sympy, letting user choose which
system to use when doing his computations and providing utilities to display
and convert units.

Unit systems are composed of units and constants, which are themselves
described from dimensions and numbers, and possibly a prefix. Quantities are
defined by their unit and their numerical value, with respect to the current
system.

The main advantage of this implementation over the old unit module is that it
divides the units in unit systems, so that the user can decide which units
to use, instead of having all in the name space. Moreover it allows a better
control over the dimensions and conversions.

Ideas and future developments can be found on the `Github wiki
<https://github.com/sympy/sympy/wiki/Unit-systems>`_.

.. toctree::
    :maxdepth: 2

    philosophy.rst
    dimensions.rst
    prefixes.rst
