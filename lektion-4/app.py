from fastapi import FastAPI
from routes.users import router as users_router

# Create the FastAPI application
app = FastAPI(
    title="User Management API",
    description="An API for managing users with Pydantic validation",
    version="1.0.0"
)

# Include the user router
app.include_router(users_router)


@app.get("/")
async def root():
    """
    Root endpoint that displays information about the API.
    """
    return {
        "message": "Welcome to User Management API!",
        "version": "1.0.0",
        "description": "This is lesson 4 - FastAPI with structured code and Pydantic",
        "endpoints": {
            "/": "This page",
            "/users": "GET - Fetch all users",
            "/users/{id}": "GET - Fetch a specific user",
            "/users": "POST - Create a new user",
            "/users/{id}": "PUT - Update a user",
            "/users/{id}": "DELETE - Delete a user",
            "/docs": "Swagger UI - Interactive API documentation",
            "/redoc": "ReDoc - Alternative API documentation"
        },
        "learning_objectives": [
            "Structured project organization",
            "Pydantic for data validation",
            "Separate schemas, routes and utils",
            "CRUD operations",
            "JSON-based data storage"
        ]
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify the server is running.
    """
    return {"status": "healthy", "message": "API is up and running!"}


if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*60)
    print("🚀 Starting User Management API...")
    print("="*60)
    print("📚 Lesson 4: FastAPI with structured code and Pydantic")
    print("="*60)
    print("📖 API Documentation:")
    print("   - Swagger UI: http://localhost:8000/docs")
    print("   - ReDoc:      http://localhost:8000/redoc")
    print("="*60)
    print("🔗 Endpoints:")
    print("   - GET    /users       - Fetch all users")
    print("   - GET    /users/{id}  - Fetch a user")
    print("   - POST   /users       - Create new user")
    print("   - PUT    /users/{id}  - Update user")
    print("   - DELETE /users/{id}  - Delete user")
    print("="*60 + "\n")

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
