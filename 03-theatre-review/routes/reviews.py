from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select, func
from models import Review, ReviewCreate, ReviewRead, ReviewUpdate

router = APIRouter(prefix="/review", tags=["reviews"])

@router.post("/", response_model=ReviewRead, status_code=201)
def create_review(review: ReviewCreate, session: Session):
    """Create a new review."""
    review_data = review.model_dump()
    new_review = Review(**review_data)
    session.add(new_review)
    session.commit()
    session.refresh(new_review)
    return new_review

@router.get("/", response_model=list[ReviewRead])
def read_reviews(session: Session):
    """Retrieve all reviews."""
    reviews = session.exec(select(Review)).all()
    return reviews  

@router.get("/{review_id}", response_model=ReviewRead)
def read_review(review_id: int, session: Session):
    """Retrieve a review by its ID."""
    review = session.get(Review, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

@