from fastapi import FastAPI
from app.routes import router
from middleware.secret_key_middleware import check_secret_key
from middleware.logging_middleware import LoggingMiddleware
from fastapi.middleware import Middleware

app = FastAPI()

app.middleware("http")(check_secret_key)
app.add_middleware(LoggingMiddleware)

app.include_router(router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Inventory API"}
