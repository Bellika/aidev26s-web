from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection URL
# Format: mysql+pymysql://username:password@host:port/database
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/aidev_web"

# Create the database engine
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Set to False in production to disable SQL logging
    pool_pre_ping=True,  # Verify connections before using them
    pool_recycle=3600  # Recycle connections after 1 hour
)

# Create a SessionLocal class for database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for our models
Base = declarative_base()


def get_db():
    """
    Dependency function that provides a database session.
    Yields a database session and ensures it's closed after use.

    Usage in routes:
        @router.get("/")
        async def some_route(db: Session = Depends(get_db)):
            # Use db here
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """
    Initialize the database by creating all tables.
    This should be called when the application starts.
    """
    from models.user import User  # Import models here to avoid circular imports
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")
