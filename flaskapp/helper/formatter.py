from pydantic import BaseModel
from typing import Optional

class ResponseModel(BaseModel):
  code: int = 200
  message : str = 'ok'
  data: Optional[dict]

