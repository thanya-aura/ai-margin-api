from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.forecast_router import router as forecast_router

app = FastAPI(
    title="AI Margin API",
    description="API for forecast adjustment using GPT",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(forecast_router, prefix="/forecast", tags=["Forecast"])

@app.get("/")
def root():
    return {"status": "API is running", "message": "Welcome to the AI Margin API"}
