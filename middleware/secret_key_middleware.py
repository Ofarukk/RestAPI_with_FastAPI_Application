from fastapi import Request
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEYS = os.getenv("SECRET_KEYS").split(",")

async def check_secret_key(request: Request, call_next):
    secret_key = request.headers.get("x-secret-key")
    
    if secret_key not in SECRET_KEYS:
        return JSONResponse(status_code=403, content={"detail": "Access Denied: Invalid Secret Key"})
    
    response = await call_next(request)
    return response
