"""
This is a basic doctest demonstrating that the package and pydra can both be successfully
imported.

>>> import pydra.engine
>>> import pydra.tasks.CHANGEME
"""
try:
    from ._version import __version__
except ImportError:
    pass
