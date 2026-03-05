from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    """
    Base schema for User containing common fields.
    This is used as a base for other schemas.
    """
    name: str = Field(..., min_length=2, max_length=50, description="User's name")
    email: EmailStr = Field(..., description="User's email address")
    age: Optional[int] = Field(None, ge=0, le=150, description="User's age")

    @field_validator('name')
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        """Validates that the name is not just whitespace"""
        if not v.strip():
            raise ValueError('Name cannot be empty or only whitespace')
        return v.strip()


class UserCreate(UserBase):
    """
    Schema for creating a new user.
    Inherits all fields from UserBase but requires a password.
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
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, ge=0, le=150)
    password: Optional[str] = Field(None, min_length=6)


class UserResponse(UserBase):
    """
    Schema for API response when returning a user.
    Contains all fields except password (for security reasons).
    """
    id: int = Field(..., description="User's unique ID")
    created_at: datetime = Field(..., description="When the user was created")

    class Config:
        """Pydantic configuration"""
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Anna Andersson",
                "email": "anna@example.com",
                "age": 25,
                "created_at": "2024-01-15T10:30:00"
            }
        }


class UserInDB(UserResponse):
    """
    Schema for how users are stored in the database/JSON file.
    Contains password (should be hashed in a real app).
    """
    password: str = Field(..., description="User's password (should be hashed in production)")
