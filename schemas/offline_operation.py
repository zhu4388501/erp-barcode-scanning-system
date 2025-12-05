from pydantic import BaseModel, Field
from typing import Dict

class OfflineOperationCreate(BaseModel):
    operation_data: Dict
    operation_type: str