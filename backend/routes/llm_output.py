from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import LLMOutput
from schema import LLMOutputBase
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/llm_output/")
def create_llm_output(llm_output_data: LLMOutputBase, db: Session = Depends(get_db)):
    llm_output_dict = llm_output_data.dict()
    db_llm_output = LLMOutput(**llm_output_dict)
    db.add(db_llm_output)
    db.commit()
    db.refresh(db_llm_output)
    return db_llm_output

@router.get("/llm_output/{llm_output_id}")
def get_llm_output(llm_output_id: int, db: Session = Depends(get_db)):
    return db.query(LLMOutput).filter(LLMOutput.id == llm_output_id).first()

@router.get("/llm_outputs/")
def get_llm_outputs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(LLMOutput).offset(skip).limit(limit).all()

@router.put("/llm_output/{llm_output_id}")
def update_llm_output(llm_output_id: int, update_data: dict, db: Session = Depends(get_db)):
    db_llm_output = get_llm_output(llm_output_id, db)
    for key, value in update_data.items():
        setattr(db_llm_output, key, value)
    db.commit()
    db.refresh(db_llm_output)
    return db_llm_output

@router.delete("/llm_output/{llm_output_id}")
def delete_llm_output(llm_output_id: int, db: Session = Depends(get_db)):
    db_llm_output = get_llm_output(llm_output_id, db)
    db.delete(db_llm_output)
    db.commit()
    return db_llm_output