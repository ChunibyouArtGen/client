import krita
import sys
sys.path.append("/usr/local/lib/python3.5/site-packages")
sys.path.append("/usr/lib/python3.5/site-packages/")
sys.path.append("/usr/lib64/python3.5/site-packages/")

from sync.client import Client, ClientComputedImage, ClientLayerImage

from .extensions import ClientExtension
import asyncio

krita_instance = krita.Krita.instance()
krita_instance.addExtension(ClientExtension(krita_instance))

c = Client()
c.start_thread()
