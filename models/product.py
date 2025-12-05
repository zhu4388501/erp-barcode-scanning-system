from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from . import Base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    product_code = Column(String, unique=True, index=True, nullable=False, comment="商品编码")
    barcode = Column(String, unique=True, index=True, nullable=False, comment="条形码/二维码")
    name = Column(String, nullable=False, comment="商品名称")
    specification = Column(String, comment="规格")
    unit = Column(String, nullable=False, comment="单位")
    min_stock = Column(Integer, default=0, comment="最低库存")
    max_stock = Column(Integer, default=99999, comment="最高库存")
    category = Column(String, comment="分类")
    brand = Column(String, comment="品牌")
    create_time = Column(DateTime, default=datetime.now, comment="创建时间")
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")