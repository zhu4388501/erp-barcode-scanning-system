from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    product_code: str = Field(..., description="商品编码")
    barcode: str = Field(..., description="条形码/二维码")
    name: str = Field(..., description="商品名称")
    specification: Optional[str] = Field(None, description="规格")
    unit: str = Field(..., description="单位")
    min_stock: int = Field(default=0, description="最低库存")
    max_stock: int = Field(default=99999, description="最高库存")
    category: Optional[str] = Field(None, description="分类")
    brand: Optional[str] = Field(None, description="品牌")

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    create_time: datetime
    update_time: datetime
    
    class Config:
        from_attributes = True