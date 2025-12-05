from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .product import Product
from .scan_record import ScanRecord
from .offline_operation import OfflineOperation
from .backup_record import BackupRecord