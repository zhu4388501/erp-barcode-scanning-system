from fastapi import APIRouter
from .product import router as product_router
from .scan import router as scan_router
from .stock import router as stock_router
from .offline import router as offline_router
from .backup import router as backup_router
from .statistics import router as statistics_router

# 创建主路由
router = APIRouter()

# 包含各个模块的路由
router.include_router(product_router, prefix="/products", tags=["product"])
router.include_router(scan_router, prefix="/scan", tags=["scan"])
router.include_router(stock_router, prefix="/stock", tags=["stock"])
router.include_router(offline_router, prefix="/offline", tags=["offline"])
router.include_router(backup_router, prefix="/backup", tags=["backup"])
router.include_router(statistics_router, prefix="/statistics", tags=["statistics"])
