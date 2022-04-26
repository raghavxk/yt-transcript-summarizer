from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware

from routers import api

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# routers
app.include_router(api.router)