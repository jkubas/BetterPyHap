import os

from betterpyhap.accessory import Accessory, Bridge

ROOT = os.path.abspath(os.path.dirname(__file__))
RESOURCE_DIR = os.path.join(ROOT, "resources")

CHARACTERISTICS_FILE = os.path.join(RESOURCE_DIR, "characteristics.json")
SERVICES_FILE = os.path.join(RESOURCE_DIR, "services.json")

# Flag if QR Code dependencies are installed.
# Installation with `pip install HAP-python[QRCode]`.
SUPPORT_QR_CODE = False
try:
    import base36
    import pyqrcode

    SUPPORT_QR_CODE = True
except ImportError:
    pass

# Define what gets imported when someone imports `betterpyhap`
__all__ = {"Accessory", "Bridge", "loader", "accessory_driver"}
