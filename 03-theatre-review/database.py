from sqlmodel import Session, SQLModel, create_engine


DATABASE_URL = "sqlite:///theatre.db"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    """Create the database and tables if they don't exist."""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Get a new database session per request"""
    with Session(engine) as session:        
        yield session       

        
