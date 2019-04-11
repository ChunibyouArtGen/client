import sys
sys.path.append("/usr/local/lib/python3.5/site-packages")
sys.path.append("/usr/lib/python3.5/site-packages/")
sys.path.append("/usr/lib64/python3.5/site-packages/")
import sync
import sync.images
import krita

from .widgets import CelestiaPrimeExtension
import asyncio


krita_instance = krita.Krita.instance()
krita_instance.addExtension(CelestiaPrimeExtension(krita_instance))
