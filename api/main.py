from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import config
from api.routers import routers

app = FastAPI(
    title="LLM Chatbot Demo",
    swagger_ui_parameters={
        "persistAuthorization": True,
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers, prefix="/api")
