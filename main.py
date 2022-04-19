from importlib import reload
from importlib.resources import path
from platform import platform
from random import sample
from fastapi import FastAPI , Depends, HTTPException, Request, Response, status
from pydantic import BaseModel
import uvicorn
import crud , database ,schemas 
from sqlalchemy.orm import Session


app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally: 
        db.close()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = database.SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response






#chemin creation de plat
@app.post("/create/flat/")
def create_flat( flat:schemas.creation_plat, db: Session = Depends(get_db)):
    message = crud.add_flat(db,flat)
    return message

#chemin récupération de tout les plats
@app.get("/Get/plats")
def all_flat(db: Session = Depends(get_db)):
    return crud.get_flats(db)

#chemin récupération  plat particulier
@app.get("/Get/plat/{id_plat}")
def flatById(id_plat:int,db: Session = Depends(get_db)):
    return crud.get_flatsById(db,id_plat)


#chemin update prix d'un plat
@app.put("/uptade/plat/price/{id_plat}/{val}")
def update_flatprice(id_plat:int,val:int,db: Session = Depends(get_db)):
    plat = crud.update_flatprice(db,id_plat,val)
    if plat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not existing flat")
    return plat

#chemin update titre d'un plat
@app.put("/uptade/plat/title/{id_plat}/{val}")
def update_flattitle(id_plat:int,val:str,db: Session = Depends(get_db)):
    plat = crud.update_flattitle(db,id_plat,val)
    if plat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not existing flat")
    return plat

#chemin update état de livraison d'un plat 1=vrai 0=FAUX
@app.put("/uptade/plat/livrable/{id_plat}/{val}")
def update_flatlivrable(id_plat:int,val:int,db: Session = Depends(get_db)):
    plat = crud.update_flatlivrable(db,id_plat,val)
    if plat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not existing flat")
    return plat


#chemin pour supprimer un plat
@app.put("/delete/plat/{ticket_id}")
def delete_plat(id_plat:int,db: Session = Depends(get_db)):
    plat = crud.delete_plat(db,id_plat)
    if plat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not existing flat ")
    return plat







if __name__ == "__main__" :
    uvicorn.run(app,host="127.0.0.1",port = 5000)