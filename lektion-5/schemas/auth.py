from pydantic import BaseModel


class LoginRequest(BaseModel):
    """
    Schema for login request.
    User provides username and password.
    """
    username: str
    password: str


class TokenResponse(BaseModel):
    """
    Schema for token response.
    Returns message about token being set in cookie.
    """
    message: str
    user_id: int
    username: str


class CurrentUser(BaseModel):
    """
    Schema for current authenticated user info.
    """
    user_id: int
    username: str
