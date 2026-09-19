from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_db_and_tables, get_session
from routes.reviews import 

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Perform any startup tasks here
    create_db_and_tables()
    print("Database and tables created successfully.")
    print("Starting up the Theatre Review API...")
    yield
    # Perform any shutdown tasks here
    #Clean up resources, close connections, etc.
    print("Shutting down the Theatre Review API...")


app = FastAPI(
title="Theatre Review API",
description="An API for managing theatre reviews",
lifespan = lifespan
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Theatre Review API!"}

def main():
    print("Hello from 03-theatre-review!")


if __name__ == "__main__":
    main()
