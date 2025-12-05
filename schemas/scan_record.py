from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ScanRecordBase(BaseModel):
    barcode: str = Field(..., description="商品条形码/二维码")
    scan_type: str = Field(..., pattern="^(in|out)$", description="扫描类型：in-入库，out-出库")
    quantity: int = Field(..., gt=0, description="数量")
    operator: str = Field(..., description="操作人")
    order_no: Optional[str] = Field(None, description="订单号")
    supplier: Optional[str] = Field(None, description="供应商/客户")
    unit_price: Optional[float] = Field(None, description="单价")

class ScanRecordCreate(ScanRecordBase):
    is_offline: bool = Field(default=False, description="是否离线操作")

class ScanRecordResponse(BaseModel):
    id: int
    product_id: int
    scan_barcode: str
    product_code: str
    product_name: str
    barcode: str
    scan_type: str
    quantity: int
    operator: str
    order_no: Optional[str]
    supplier: Optional[str]
    unit_price: Optional[float]
    is_offline: bool
    sync_status: str
    scan_time: datetime
    create_time: datetime
    
    class Config:
        from_attributes = True