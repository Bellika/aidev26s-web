from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.user import UserCreate, UserResponse, UserUpdate
from models.user import User
from config.database import get_db
from utils.password import hash_password

# Create a router for user endpoints
router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/", response_model=List[UserResponse])
async def get_all_users(db: Session = Depends(get_db)):
    """
    Fetches all users from the database.

    Returns:
        List of all users (without passwords)
    """
    users = db.query(User).all()
    print(f"Fetched {len(users)} users from database")
    return users


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Fetches a specific user by ID.

    Args:
        user_id: ID of the user to fetch
        db: Database session (injected by FastAPI)

    Returns:
        The user (without password)

    Raises:
        HTTPException: 404 if the user is not found
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        print(f"User with ID {user_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )

    print(f"Fetched user: {user.username} (ID: {user.id})")
    return user


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Creates a new user.

    Args:
        user: UserCreate schema with user data
        db: Database session (injected by FastAPI)

    Returns:
        The newly created user (without password)

    Raises:
        HTTPException: 400 if the username already exists
    """
    # Check if the username already exists
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        print(f"Attempted to create user with existing username: {user.username}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"A user with username '{user.username}' already exists"
        )

    # Hash the password before storing
    hashed_password = hash_password(user.password)

    # Create the new user
    new_user = User(
        username=user.username,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    print(f"Created new user: {new_user.username} (ID: {new_user.id})")
    return new_user


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    """
    Updates a user.

    Args:
        user_id: ID of the user to update
        user_update: UserUpdate schema with fields to update
        db: Database session (injected by FastAPI)

    Returns:
        The updated user (without password)

    Raises:
        HTTPException: 404 if the user is not found
        HTTPException: 400 if the username is already used by another user
    """
    # Check if the user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        print(f"User with ID {user_id} not found for update")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )

    # If username is being updated, check that it's not already in use
    if user_update.username:
        existing_user = db.query(User).filter(
            User.username == user_update.username,
            User.id != user_id
        ).first()
        if existing_user:
            print(f"Attempted to update to existing username: {user_update.username}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Username '{user_update.username}' is already used by another user"
            )
        user.username = user_update.username

    # If password is being updated, hash it
    if user_update.password:
        user.password = hash_password(user_update.password)

    db.commit()
    db.refresh(user)

    print(f"Updated user: {user.username} (ID: {user.id})")
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Deletes a user.

    Args:
        user_id: ID of the user to delete
        db: Database session (injected by FastAPI)

    Raises:
        HTTPException: 404 if the user is not found
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        print(f"User with ID {user_id} not found for deletion")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )

    db.delete(user)
    db.commit()

    print(f"Deleted user: {user.username} (ID: {user_id})")
    return None
