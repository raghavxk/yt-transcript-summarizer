from pydantic import BaseModel

class SummaryResponseSchema(BaseModel):
    videoid : str
    summary : str
