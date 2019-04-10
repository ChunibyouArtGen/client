import sys
sys.path.append("/usr/local/lib/python3.5/site-packages")

import krita

from .widgets import CelestiaPrimeExtension
import asyncio


krita_instance = krita.Krita.instance()
krita_instance.addExtension(CelestiaPrimeExtension(krita_instance))