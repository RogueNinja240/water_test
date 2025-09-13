from pydantic import BaseModel, Field

class Water(BaseModel):
    ph: float = Field(..., ge=0, le=14, description="pH value between 0 and 14")
    Hardness: float = Field(..., ge=0, description="Hardness must be non-negative")
    Solids: float = Field(..., ge=0, description="Solids must be non-negative")
    Chloramines: float = Field(..., ge=0, description="Chloramines must be non-negative")
    Sulfate: float = Field(..., ge=0, description="Sulfate must be non-negative")
    Conductivity: float = Field(..., ge=0, description="Conductivity must be non-negative")
    Organic_carbon: float = Field(..., ge=0, description="Organic carbon must be non-negative")
    Trihalomethanes: float = Field(..., ge=0, description="Trihalomethanes must be non-negative")
    Turbidity: float = Field(..., ge=0, description="Turbidity must be non-negative")
