from pydantic import BaseModel

class ReviewBase(BaseModel):
    name: str
    rating: int
    comment: str

class ReviewCreate(ReviewBase):
    pass

class ReviewOut(ReviewBase):
    id: int

    class Config:
        from_attributes  = True
