from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from routes.users import router as users_router
from routes.auth import router as auth_router
from config.database import init_db, get_db

# Create the FastAPI application
app = FastAPI(
    title="User Management API with MySQL and JWT Auth",
    description="An API for managing users with MySQL database, SQLAlchemy models, password hashing, and JWT authentication",
    version="2.0.0"
)

# Initialize database tables on startup
@app.on_event("startup")
async def startup_event():
    """
    Run when the application starts.
    Creates database tables if they don't exist.
    """
    print("\n" + "="*60)
    print("🔧 Initializing database...")
    print("="*60)
    init_db()
    print("="*60 + "\n")


# Include routers
app.include_router(users_router)
app.include_router(auth_router)


@app.get("/")
async def root():
    """
    Root endpoint that displays information about the API.
    """
    return {
        "message": "Welcome to User Management API with MySQL and JWT Auth!",
        "version": "2.0.0",
        "description": "This is lesson 5 - FastAPI with MySQL database, CRUD, and JWT Authentication",
        "endpoints": {
            "/": "This page",
            "/users": "GET - Fetch all users",
            "/users/{id}": "GET - Fetch a specific user",
            "/users": "POST - Create a new user",
            "/users/{id}": "PUT - Update a user",
            "/users/{id}": "DELETE - Delete a user",
            "/auth/login": "POST - Login and get JWT token in HTTP-only cookie",
            "/auth/logout": "POST - Logout and clear cookie",
            "/auth/me": "GET - Get current user info (protected)",
            "/auth/secret": "GET - Access secret endpoint (protected)",
            "/docs": "Swagger UI - Interactive API documentation",
            "/redoc": "ReDoc - Alternative API documentation"
        },
        "learning_objectives": [
            "MySQL database integration",
            "SQLAlchemy ORM models",
            "Database configuration and connection management",
            "Password hashing with bcrypt",
            "Full CRUD operations with database",
            "Pydantic schemas for validation",
            "Dependency injection with FastAPI",
            "JWT authentication with HTTP-only cookies",
            "Protected routes with dependencies"
        ]
    }


@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    """
    Health check endpoint to verify the server and database are running.
    Performs an actual database query to verify connectivity.
    """
    try:
        # Execute a simple query to check database connectivity
        db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "message": "API is up and running!",
            "database": "connected"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "message": "Database connection failed",
            "database": "disconnected",
            "error": str(e)
        }


if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*70)
    print("🚀 Starting User Management API with MySQL and JWT Auth...")
    print("="*70)
    print("📚 Lesson 5: FastAPI with MySQL, CRUD, and JWT Authentication")
    print("="*70)
    print("📖 API Documentation:")
    print("   - Swagger UI: http://localhost:8000/docs")
    print("   - ReDoc:      http://localhost:8000/redoc")
    print("="*70)
    print("🔗 User Endpoints:")
    print("   - GET    /users       - Fetch all users")
    print("   - GET    /users/{id}  - Fetch a user")
    print("   - POST   /users       - Create new user")
    print("   - PUT    /users/{id}  - Update user")
    print("   - DELETE /users/{id}  - Delete user")
    print("="*70)
    print("🔐 Auth Endpoints:")
    print("   - POST   /auth/login  - Login (get JWT in HTTP-only cookie)")
    print("   - POST   /auth/logout - Logout (clear cookie)")
    print("   - GET    /auth/me     - Get current user (protected)")
    print("   - GET    /auth/secret - Access secret (protected)")
    print("="*70)
    print("✨ Features:")
    print("   - MySQL database with SQLAlchemy")
    print("   - Password hashing with bcrypt")
    print("   - JWT authentication with HTTP-only cookies")
    print("   - Protected routes")
    print("   - Full CRUD operations")
    print("="*70 + "\n")

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
