from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from . import Base

class OfflineOperation(Base):
    __tablename__ = "offline_operations"
    
    id = Column(Integer, primary_key=True, index=True)
    operation_data = Column(Text, nullable=False, comment="离线操作数据")
    operation_type = Column(String, nullable=False, comment="操作类型：scan_in, scan_out, product_create")
    sync_status = Column(String, default="pending", comment="同步状态：pending-待同步，completed-已同步，failed-同步失败")
    create_time = Column(DateTime, default=datetime.now, comment="创建时间")
    sync_time = Column(DateTime, nullable=True, comment="同步时间")