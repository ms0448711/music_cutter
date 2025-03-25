from pydantic import BaseModel, Field

class Segment(BaseModel):
    title:str = Field(description="The name for this segment")
    start_time:int = Field(...,description="The star time of the segment.")
    end_time:int = Field(...,description="The end time of the segment.")