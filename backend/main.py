
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/forecast")
def get_forecast():
    return JSONResponse({
        "item": "Red Hoodie",
        "forecast": 42.3,
        "alert": "Spike expected from cold weather + viral trend."
    })
