import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session



app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Football(BaseModel):
    player_name: str = Field(min_length=1)
    team: str = Field(min_length=1)
    num_player: int = Field(gt=1, lt=100)
    goals: int = Field(gt=1, lt=100)
    assist: int = Field(gt=1, lt=100)
    transfer_market: int = Field(gt=1, lt=10000000000)

footballs = []


@app.get("/")
def read_playres(db: Session = Depends(get_db)):
    return db.query(models.footballs).all()


@app.post("/")
def crate_playres(football: Football, db: Session = Depends(get_db)):
    football_model = models.footballs()
    football_model.player_name = football.player_name
    football_model.team = football.team
    football_model.num_player = football.num_player
    football_model.goals = football.goals
    football_model.assist = football.assist
    football_model.transfer_market = football.transfer_market
    db.add(football_model)
    db.commit()
    db.refresh(football_model)
    return football

@app.put("/{playre_id}")
def update_player(playre_id: int, football: Football, db: Session = Depends(get_db)):

    football_model = db.query(models.footballs).filter(models.footballs.id == playre_id).first()

    if football_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {playre_id} does not exist"
        )

    for field, value in football.dict(exclude={"id"}).items():
        setattr(football_model, field, value)

    db.commit()
    db.refresh(football_model)
    return football_model


@app.delete("/{playre_id}")
def delet_player(playre_id: int, db: Session = Depends(get_db)):

    football_model = db.query(models.footballs).filter(models.footballs.id == playre_id).first()

    if football_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {playre_id} does not exist"
        )
    db.query(models.footballs).filter(models.footballs.id == playre_id).delete()
    db.commit()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
