from pydantic import BaseModel, Field
from typing import Optional

class BackupCreate(BaseModel):
    backup_by: Optional[str] = Field(None, description="备份人")