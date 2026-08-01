from fastapi import FastAPI
from fastapi import Request
import uvicorn

app = FastAPI(
    title="Swiggy Order Service",
    description=(
        "internal API for managing orders"
        "Handle creation, tracking of delivery systems"
    ),
    version="1.2.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
def read_root():
    """Root endpoint - Health check"""
    # FastAPI converts this dict into JSON
    return {
        "message": "Welcome to swiggy Order service",
        "status": "healthy"
    }

@app.get("/about")
def about():
    """Returns API metadata"""
    return {
        "service":"order-service",
        "team":"backend platform",
        "region":"ap-south-1",
        "version":"1.2.2"
    }
@app.get("/orders")
def list_orders():
    """List recent orders"""

    return {
        "orders" : [
            {"id" : 1, "item" : "Butter Chicken", "status":"delivered"},
            {"id" : 2, "item" : "Masala Dosa", "status":"preparing"},
            {"id" : 3, "item" : "Paneer Tikka", "status":"delivered"},
        ]
    }

@app.get("/orders/status")
def order_status():
    """Get order status"""
    return {
        "total_today":2_340_23,
        "top_city":"Bengaluru"
    }


@app.post("/orders/active",
          summary="Get active orders",
          description=(
              "Return all orders that are currently being prepared" 
              "or are out for delivery"),
              tags=["orders"],
              response_description="List of active orders",
              deprecated=False

          )
def get_active_orders(request: Request):
    """Get active orders"""
    return {
        "active_orders": [
            {"id": 1, "item": "Butter Chicken", "status":"preparing"},
            {"id": 2, "item": "Masala Dosa", "status":"out for delivery"},
        ]
    }

@app.get("/restaurants",tags=["Restaurants"])
def list_retro():
    """List all restaurants"""
    return {
        "restaurants": [
            {"id": 1, "name": "Biryani House", "rating":4.5},
            {"id": 2, "name": "Dosa Corner", "rating":4.2},
            {"id": 3, "name": "Paneer Palace", "rating":4.8},
        ]
    }