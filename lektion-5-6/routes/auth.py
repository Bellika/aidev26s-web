from fastapi import APIRouter, HTTPException, status, Depends, Cookie, Response
from sqlalchemy.orm import Session
from typing import Optional
from schemas.auth import LoginRequest, TokenResponse, CurrentUser
from models.user import User
from config.database import get_db
from utils.password import verify_password
from utils.auth import create_access_token, decode_access_token

# Create a router for auth endpoints
router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)


@router.post("/login", response_model=TokenResponse)
async def login(login_data: LoginRequest, response: Response, db: Session = Depends(get_db)):
    """
    Login endpoint that authenticates a user and returns a JWT token as HTTP-only cookie.

    Args:
        login_data: LoginRequest with email (username) and password
        response: FastAPI Response to set cookie
        db: Database session (injected by FastAPI)

    Returns:
        TokenResponse with success message and user info

    Raises:
        HTTPException: 401 if credentials are invalid
    """
    # Find user by username
    user = db.query(User).filter(User.username == login_data.username).first()

    if not user:
        print(f"Login failed: User with username {login_data.username} not found")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    # Verify password
    if not verify_password(login_data.password, user.password):
        print(f"Login failed: Invalid password for {login_data.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    # Create JWT token
    token_data = {
        "user_id": user.id,
        "username": user.username
    }
    access_token = create_access_token(data=token_data)

    # Set HTTP-only cookie
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,  # Prevents JavaScript access
        max_age=1800,   # 30 minutes
        samesite="lax"  # CSRF protection
    )

    print(f"User {user.username} logged in successfully")

    return TokenResponse(
        message="Login successful! Token set as HTTP-only cookie",
        user_id=user.id,
        username=user.username
    )


@router.post("/logout")
async def logout(response: Response):
    """
    Logout endpoint that clears the JWT cookie.

    Args:
        response: FastAPI Response to clear cookie

    Returns:
        Success message
    """
    response.delete_cookie(key="access_token")
    print("User logged out successfully")
    return {"message": "Logged out successfully"}


def get_current_user(access_token: Optional[str] = Cookie(None)) -> CurrentUser:
    """
    Dependency to get the current authenticated user from the JWT cookie.

    Args:
        access_token: JWT token from HTTP-only cookie

    Returns:
        CurrentUser with user_id and email

    Raises:
        HTTPException: 401 if token is missing or invalid
    """
    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated. Please login first."
        )

    # Decode and verify token
    payload = decode_access_token(access_token)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token. Please login again."
        )

    return CurrentUser(
        user_id=payload.get("user_id"),
        username=payload.get("username")
    )


@router.get("/secret")
async def get_secret(current_user: CurrentUser = Depends(get_current_user)):
    """
    Protected endpoint that requires authentication.
    Returns a secret message only for authenticated users.

    Args:
        current_user: Current authenticated user (injected by dependency)

    Returns:
        Secret message with user info
    """
    print(f"User {current_user.username} accessed the secret endpoint")

    return {
        "message": "This is a secret message!",
        "secret": "The answer to life, the universe, and everything is 42",
        "user": {
            "user_id": current_user.user_id,
            "username": current_user.username
        },
        "note": "You can only see this because you are authenticated!"
    }


@router.get("/me", response_model=CurrentUser)
async def get_me(current_user: CurrentUser = Depends(get_current_user)):
    """
    Get current user information from the JWT token.

    Args:
        current_user: Current authenticated user (injected by dependency)

    Returns:
        Current user info
    """
    return current_user
