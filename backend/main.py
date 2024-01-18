from fastapi import FastAPI
from backend.routers import router

app = FastAPI(
    title="HackujStat V5",
    docs_url="/docs",
    redoc_url=None,   
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(router.router)