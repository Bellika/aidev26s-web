from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from config.database import Base


class User(Base):
    """
    SQLAlchemy model for the users table.
    This represents how data is stored in the MySQL database.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)  # Will store hashed passwords
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"
