from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from . import Base

class BackupRecord(Base):
    __tablename__ = "backup_records"
    
    id = Column(Integer, primary_key=True, index=True)
    backup_file = Column(String, nullable=False, comment="备份文件名")
    backup_size = Column(Integer, comment="备份文件大小")
    backup_time = Column(DateTime, default=datetime.now, comment="备份时间")
    backup_by = Column(String, comment="备份人")
    is_valid = Column(Boolean, default=True, comment="是否有效")