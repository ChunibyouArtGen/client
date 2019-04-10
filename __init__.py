import krita

from .widgets import CelestiaPrimeExtension
import asyncio

krita_instance = krita.Krita.instance()
krita_instance.addExtension(CelestiaPrimeExtension(krita_instance))