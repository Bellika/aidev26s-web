import json
import os
from typing import List, Optional
from datetime import datetime
from schemas.user import UserInDB, UserCreate


class JSONDatabase:
    """
    A simple JSON-based "database" for storing users.
    In a real application, you would use a real database like PostgreSQL or MongoDB.
    """

    def __init__(self, file_path: str = "users.json"):
        """
        Initializes the database with a file path.

        Args:
            file_path: Path to the JSON file where users are stored
        """
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Creates the file if it doesn't exist"""
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)

    def _read_users(self) -> List[dict]:
        """Reads all users from the JSON file"""
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def _write_users(self, users: List[dict]):
        """Writes all users to the JSON file"""
        with open(self.file_path, 'w') as f:
            json.dump(users, f, indent=2, default=str)

    def get_all_users(self) -> List[UserInDB]:
        """
        Fetches all users.

        Returns:
            List of all users as UserInDB objects
        """
        users_data = self._read_users()
        return [UserInDB(**user) for user in users_data]

    def get_user_by_id(self, user_id: int) -> Optional[UserInDB]:
        """
        Fetches a specific user by ID.

        Args:
            user_id: ID of the user to fetch

        Returns:
            UserInDB object if the user is found, otherwise None
        """
        users = self._read_users()
        for user in users:
            if user.get('id') == user_id:
                return UserInDB(**user)
        return None

    def get_user_by_email(self, email: str) -> Optional[UserInDB]:
        """
        Fetches a user by email address.

        Args:
            email: Email address of the user

        Returns:
            UserInDB object if the user is found, otherwise None
        """
        users = self._read_users()
        for user in users:
            if user.get('email') == email:
                return UserInDB(**user)
        return None

    def create_user(self, user_data: UserCreate) -> UserInDB:
        """
        Creates a new user.

        Args:
            user_data: UserCreate schema with user data

        Returns:
            The newly created user as a UserInDB object
        """
        users = self._read_users()

        # Generate new ID
        new_id = max([u.get('id', 0) for u in users], default=0) + 1

        # Create new user with ID and timestamp
        new_user = UserInDB(
            id=new_id,
            name=user_data.name,
            email=user_data.email,
            age=user_data.age,
            password=user_data.password,  # In production: hash the password!
            created_at=datetime.now()
        )

        # Add to list and save
        users.append(new_user.model_dump())
        self._write_users(users)

        return new_user

    def update_user(self, user_id: int, update_data: dict) -> Optional[UserInDB]:
        """
        Updates a user.

        Args:
            user_id: ID of the user to update
            update_data: Dict with fields to update

        Returns:
            The updated user as a UserInDB object, or None if the user doesn't exist
        """
        users = self._read_users()

        for i, user in enumerate(users):
            if user.get('id') == user_id:
                # Only update fields that exist in update_data and are not None
                for key, value in update_data.items():
                    if value is not None:
                        user[key] = value

                users[i] = user
                self._write_users(users)
                return UserInDB(**user)

        return None

    def delete_user(self, user_id: int) -> bool:
        """
        Deletes a user.

        Args:
            user_id: ID of the user to delete

        Returns:
            True if the user was deleted, False if the user was not found
        """
        users = self._read_users()
        original_length = len(users)

        users = [u for u in users if u.get('id') != user_id]

        if len(users) < original_length:
            self._write_users(users)
            return True
        return False
