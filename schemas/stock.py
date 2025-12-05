from pydantic import BaseModel, Field
from typing import Optional

class StockQueryResponse(BaseModel):
    product_id: int
    product_code: str
    product_name: str
    barcode: str
    specification: Optional[str]
    unit: str
    category: Optional[str]
    brand: Optional[str]
    total_stock_in: int
    total_stock_out: int
    current_stock: int
    min_stock: int
    max_stock: int
    is_alert: bool = Field(default=False, description="是否需要预警")