from fastapi import FastAPI
from .routers import scan_router, auth_router, report_router

app = FastAPI(title="Vulnerability Scanner")

app.include_router(scan_router.router)
app.include_router(auth_router.router)
app.include_router(report_router.router)

@app.get("/")
def root():
    return {"status": "scanner running"}