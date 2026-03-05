from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.user import UserCreate, UserResponse, UserUpdate
from utils.json_handler import JSONDatabase

# Create a router for user endpoints
router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# Initialize the database
db = JSONDatabase("users.json")


@router.get("/", response_model=List[UserResponse])
async def get_all_users():
    """
    Fetches all users.

    Returns:
        List of all users (without passwords)
    """
    users = db.get_all_users()
    print(f"Fetched {len(users)} users from database")
    return users


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """
    Fetches a specific user by ID.

    Args:
        user_id: ID of the user to fetch

    Returns:
        The user (without password)

    Raises:
        HTTPException: 404 if the user is not found
    """
    user = db.get_user_by_id(user_id)
    if not user:
        print(f"User with ID {user_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )

    print(f"Fetched user: {user.name} (ID: {user.id})")
    return user


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """
    Creates a new user.

    Args:
        user: UserCreate schema with user data

    Returns:
        The newly created user (without password)

    Raises:
        HTTPException: 400 if the email already exists
    """
    # Check if the email already exists
    existing_user = db.get_user_by_email(user.email)
    if existing_user:
        print(f"Attempted to create user with existing email: {user.email}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"A user with email {user.email} already exists"
        )

    # Create the user
    new_user = db.create_user(user)
    print(f"Created new user: {new_user.name} (ID: {new_user.id})")
    return new_user


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_update: UserUpdate):
    """
    Updates a user.

    Args:
        user_id: ID of the user to update
        user_update: UserUpdate schema with fields to update

    Returns:
        The updated user (without password)

    Raises:
        HTTPException: 404 if the user is not found
        HTTPException: 400 if the email is already used by another user
    """
    # Check if the user exists
    existing_user = db.get_user_by_id(user_id)
    if not existing_user:
        print(f"User with ID {user_id} not found for update")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )

    # If email is being updated, check that it's not already in use
    if user_update.email:
        email_user = db.get_user_by_email(user_update.email)
        if email_user and email_user.id != user_id:
            print(f"Attempted to update to existing email: {user_update.email}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Email {user_update.email} is already used by another user"
            )

    # Update the user
    update_data = user_update.model_dump(exclude_unset=True)
    updated_user = db.update_user(user_id, update_data)

    print(f"Updated user: {updated_user.name} (ID: {updated_user.id})")
    return updated_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    """
    Deletes a user.

    Args:
        user_id: ID of the user to delete

    Raises:
        HTTPException: 404 if the user is not found
    """
    success = db.delete_user(user_id)
    if not success:
        print(f"User with ID {user_id} not found for deletion")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )

    print(f"Deleted user with ID: {user_id}")
    return None
