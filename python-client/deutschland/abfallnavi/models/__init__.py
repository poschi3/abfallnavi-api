# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.abfallnavi.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.abfallnavi.model.abholung import Abholung
from deutschland.abfallnavi.model.bezirk import Bezirk
from deutschland.abfallnavi.model.fraktion import Fraktion
from deutschland.abfallnavi.model.hausnummer import Hausnummer
from deutschland.abfallnavi.model.ort import Ort
from deutschland.abfallnavi.model.ort2 import Ort2
from deutschland.abfallnavi.model.ort_inner import OrtInner
from deutschland.abfallnavi.model.region import Region
from deutschland.abfallnavi.model.strasse import Strasse
