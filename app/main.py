from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Finance Expense Tracker API",
    description="A REST API to manage personal expenses — built for SQE testing demo",
    version="1.0.0"
)

app.include_router(router)


@app.get("/", tags=["Health"])
def root():
    return {"status": "running", "message": "Finance Tracker API is live"}


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}
