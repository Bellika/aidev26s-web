from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    """
    Base schema for User containing common fields.
    """
    username: str = Field(..., min_length=3, max_length=50, description="User's username")

    @field_validator('username')
    @classmethod
    def username_must_be_alphanumeric(cls, v: str) -> str:
        """Validates that username contains only letters, numbers, and underscores"""
        if not v.replace('_', '').isalnum():
            raise ValueError('Username can only contain letters, numbers, and underscores')
        return v.strip()


class UserCreate(UserBase):
    """
    Schema for creating a new user.
    Requires username and password.
    """
    password: str = Field(..., min_length=6, description="User's password (minimum 6 characters)")

    @field_validator('password')
    @classmethod
    def password_must_be_strong(cls, v: str) -> str:
        """Simple validation that the password has at least 6 characters"""
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters long')
        return v


class UserUpdate(BaseModel):
    """
    Schema for updating a user.
    All fields are optional so you can update only what you want.
    """
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    password: Optional[str] = Field(None, min_length=6)

    @field_validator('username')
    @classmethod
    def username_must_be_alphanumeric(cls, v: Optional[str]) -> Optional[str]:
        """Validates that username contains only letters, numbers, and underscores"""
        if v is not None and not v.replace('_', '').isalnum():
            raise ValueError('Username can only contain letters, numbers, and underscores')
        return v.strip() if v else v


class UserResponse(UserBase):
    """
    Schema for API response when returning a user.
    Contains all fields except password (for security reasons).
    """
    id: int = Field(..., description="User's unique ID")
    created_at: datetime = Field(..., description="When the user was created")
    updated_at: datetime = Field(..., description="When the user was last updated")

    class Config:
        """Pydantic configuration to work with SQLAlchemy models"""
        from_attributes = True  # Allows Pydantic to work with ORM models
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "john_doe",
                "created_at": "2024-01-15T10:30:00",
                "updated_at": "2024-01-15T10:30:00"
            }
        }


class UserInDB(UserResponse):
    """
    Schema for how users are stored in the database.
    Contains hashed password.
    """
    password: str = Field(..., description="User's hashed password")
