from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class ProductInput(BaseModel):
    product_name: str
    category: str
    target_market: str
    selling_points: List[str] = Field(default_factory=list)
    model_preference: str = "VEO"
    price_positioning: str = "mid-range"
    notes: Optional[str] = ""


class AgentResult(BaseModel):
    agent_name: str
    summary: str
    data: Dict[str, Any]
