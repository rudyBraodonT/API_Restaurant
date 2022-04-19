from enum import Enum
from xmlrpc.client import Boolean
from numpy import integer
from sqlalchemy import Column , Integer , String, TIMESTAMP, null

import database




class creationPlat(database.Base):
    __tablename__ = "plats"

    idplats = Column(Integer, primary_key=True, index=True)
    titre = Column(String)
    prix = Column(Integer)
    livrable = Column(Integer)
    date_creation = Column(String)


class plat(creationPlat):
    idusers = Column(Integer)
    supprime=Column(Integer)

class creationMenu(database.Base):
    __tablename__ = "menus"

    idmenus = Column(Integer, primary_key=True, index=True)
    idplats = Column(Integer)
    idboissons = Column(Integer)
    date_sorti = Column(String)
    intitule= Column(String)


class menu(creationMenu):
    idusers = Column(Integer)
    

class commande(database.Base):
    __tablename__ = "commandes"

    idcommandes = Column(Integer, primary_key=True, index=True)
    idplats = Column(Integer)
    jour_livraison = Column(String)
    jour_livraison = Column(String)
    jour_livraison = Column(String)
    num_client= Column(String)

class boissons(database.Base):
    __tablename__ = "boissons"

    idboissons = Column(Integer, primary_key=True, index=True)
    prix = Column(Integer)
    libelle = Column(String)
    categorie = Column(String)
    