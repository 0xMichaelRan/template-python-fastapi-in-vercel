from fastapi import FastAPI

from src.routes import root, hello

app = FastAPI()

# Include routers
app.include_router(root.router)
app.include_router(hello.router)
