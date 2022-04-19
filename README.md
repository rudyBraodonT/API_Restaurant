# API_Restaurant
HOST: http://127.0.0.1:5000

# rudyBraodonT 

cette api est permet de faire un CRUD  sur les entités MENU  PLAT COMMANDE BOISSON

#ETAT : NON TERMINER

##Liste de tout les plats(non supprimé)  [/Get/plats]

+ Response
{
    "date_creation": "2022-04-19",
    "titre": "koki",
    "prix": 500,
    "idusers": 1,
    "livrable": 1,
    "idplats": 1,
    "supprime": 0
  },
  
 ##liste des plats selon l'id [/Get/plat/{id_plat}]
 
+ Response
{
   "date_creation": "2022-04-19",
    "titre": "koki",
    "prix": 500,
    "idusers": 1,
    "livrable": 1,
    "idplats": 1,
    "supprime": 0
}

 ##creations d'un plat selon [/create/flat/]
 
 + Request (application/json)
 
{
  titre:string,
  prix: int,
  livrable:int
}
 
 + Response
{
   "date_creation": "2022-04-19",
    "titre": "koki",
    "prix": 500,
    "idusers": 1,
    "livrable": 1,
    "idplats": 1,
    "supprime": 0
}

##modifier le prix d'un plat [/uptade/plat/price/{id_plat}/{val}]

+require
id_plat
val

+ Response
{
   "date_creation": "2022-04-19",
    "titre": "koki",
    "prix": 500,
    "idusers": 1,
    "livrable": 1,
    "idplats": 1,
    "supprime": 0
}

##modifier le titre d'un plat [/uptade/plat/title/{id_plat}/{val}]
+require
id_plat
val

+ Response
{
   "date_creation": "2022-04-19",
    "titre": "koki",
    "prix": 500,
    "idusers": 1,
    "livrable": 1,
    "idplats": 1,
    "supprime": 0
}


##modifier l'état livrable d'un plat [/uptade/plat/livrable/{id_plat}/{val}]
+require
id_plat
val

+ Response
{
   "date_creation": "2022-04-19",
    "titre": "koki",
    "prix": 500,
    "idusers": 1,
    "livrable": 1,
    "idplats": 1,
    "supprime": 0
}


##supprimer un plat [/delete/plat/{ticket_id]
+require
id_plat

+ Response
{
   "date_creation": "2022-04-19",
    "titre": "koki",
    "prix": 500,
    "idusers": 1,
    "livrable": 1,
    "idplats": 1,
    "supprime": 1
}

