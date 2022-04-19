from datetime import date
import schemas , models
from sqlalchemy.orm import Session




#recupérer tout les plats

def get_flats(db:Session,skip:int = 0):
    return db.query(models.plat).filter(models.plat.supprime == 0).all()


#recupérer un plats particlier 
def get_flatsById(db:Session,id_plat:int,skip:int = 0):
    return db.query(models.plat).filter(models.plat.idplats == id_plat,models.plat.supprime == 0).first()

#ajouter un plat

def add_flat(db:Session,plat:schemas.creation_plat,):
    db_menu = models.creationPlat(titre=plat.titre, prix=plat.prix, livrable=plat.livrable,date_creation=date.today())
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu

#modifier le prix d'un plat

def update_flatprice(db:Session,id_plat:int,val:int):
    plat = db.query(models.plat).filter(models.plat.idplats == id_plat).first()
    plat.prix = val
    db.commit()
    db.refresh(plat)
    return plat


#modifier le titre d'un plat

def update_flattitle(db:Session,id_plat:int,val:str):
    plat = db.query(models.plat).filter(models.plat.idplats == id_plat).first()
    plat.titre = val
    db.commit()
    db.refresh(plat)
    return plat


#modifier l'état de livraison d'un plat
def update_flatlivrable(db:Session,id_plat:int,val:int):
    plat = db.query(models.plat).filter(models.plat.idplats == id_plat).first()
    plat.livrable = val
    db.commit()
    db.refresh(plat)
    return plat


#supprimer un plat
def delete_plat(db:Session,id_plat:int):
    plat = db.query(models.plat).filter(models.plat.idplats == id_plat).first()
    plat.supprime = 1
    db.commit()
    db.refresh(plat)
    return plat

