# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from deutschland.abfallnavi.api.abholpunkte_api import AbholpunkteApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from deutschland.abfallnavi.api.abholpunkte_api import AbholpunkteApi
from deutschland.abfallnavi.api.fraktionen_api import FraktionenApi
from deutschland.abfallnavi.api.termine_api import TermineApi
