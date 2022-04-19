
from pydantic import BaseModel



class creation_plat(BaseModel):
    idplats = int   
    titre = str
    prix = int
    livrable = int
    idusers =int
    date_creation = str


class plat(creation_plat):
    suppime=int


class creation_menu(BaseModel):
    idmenus = int
    idplats = int
    idboissons = int
    date_sorti = str
    intitule= str


class menu(creation_menu):
    idusers = str

class commande(BaseModel):
    idcommandes = int
    idplats = int
    jour_livraison = str
    jour_livraison = str
    jour_livraison = str
    num_client= str

class boissons(BaseModel):
    idboissons = int
    prix = int
    libelle = str
    categorie = str




