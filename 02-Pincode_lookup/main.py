from fastapi import FastAPI

app = FastAPI(
    title="Pincode lookup API",
    description="Auto fill city and state from Indian pincodes during checkout",
)

@app.get('/')
def root():
    return {"message": "Welcome to Pincode lookup API"}