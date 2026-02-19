from pydantic import BaseModel, Field
from typing import List, Dict

class AdData(BaseModel):
    impressions: int = Field(..., description="Total ad impressions")
    clicks: int = Field(..., description="Total clicks")
    conversions: int = Field(..., description="Total conversions")
    spend: float = Field(..., description="Total spend in USD")
    platform: str = Field(..., description="Ad platform name")

class TargetAudience(BaseModel):
    industry: str = Field(..., description="Industry type")
    budget: float = Field(..., description="Monthly budget in USD")
    audience_type: str = Field(..., description="Target audience type")

class BudgetAllocation(BaseModel):
    total_budget: float = Field(..., description="Total monthly budget")
    channels: List[Dict[str, float]] = Field(..., description="Current channel allocations")
    performance_data: Dict[str, Dict[str, float]] = Field(..., description="Performance metrics per channel")
