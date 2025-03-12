from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, expenses
from database import engine
import uvicorn

app = FastAPI(title="Asynchronous Expense Tracker API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router)
app.include_router(expenses.router)

@app.get("/health")
def health_check():
    return {"status": "OK"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
