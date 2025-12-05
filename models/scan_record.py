from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float
from datetime import datetime
from . import Base

class ScanRecord(Base):
    __tablename__ = "scan_records"
    
    id = Column(Integer, primary_key=True, index=True)
    scan_barcode = Column(String, nullable=False, index=True, comment="扫描的条码/二维码")
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True, comment="商品ID")
    scan_type = Column(String, nullable=False, comment="扫描类型：in-入库，out-出库")
    quantity = Column(Integer, nullable=False, comment="数量")
    operator = Column(String, nullable=False, comment="操作人")
    order_no = Column(String, comment="订单号")
    supplier = Column(String, comment="供应商/客户")
    unit_price = Column(Float, comment="单价")
    is_offline = Column(Boolean, default=False, comment="是否离线操作")
    sync_status = Column(String, default="completed", comment="同步状态：pending-待同步，completed-已同步，failed-同步失败")
    scan_time = Column(DateTime, default=datetime.now, comment="扫描时间")
    create_time = Column(DateTime, default=datetime.now, comment="创建时间")