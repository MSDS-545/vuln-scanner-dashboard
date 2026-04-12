from pydantic import BaseModel

class ScanResult(BaseModel):

    vulnerability: str
    severity: str
    line: int