import random

POKENEAS = [
    {
        "id": 1,
        "nombre": "CrisValencia",
        "altura": 0.2,
        "habilidad": "Daña oidos con su voz",
        "imagen": "https://pokenea-imagenes-sdeossag.s3.us-east-1.amazonaws.com/crisva.jpg",
        "frase": "Te busco y no te encuentro, estoy buscando respuesta",
    },
    {
        "id": 2,
        "nombre": "WestCOL",
        "altura": 1.4,
        "habilidad": "Te tira cualquier groseria y te mata",
        "imagen": "https://pokenea-imagenes-sdeossag.s3.us-east-1.amazonaws.com/west.jpg",
        "frase": "EL que creo Honda tiene una frase que ojala se la graben que eso les va a servir para la vida.",
    },
    {
        "id": 3,
        "nombre": "AlejaUrrea",
        "altura": 0.4,
        "habilidad": "Te hace reir hasta que se te caen los dientes",
        "imagen": "https://pokenea-imagenes-sdeossag.s3.us-east-1.amazonaws.com/alejaurrea.jpg",
        "frase": "No entiendo como hay mujeres que tienen mozo, como hacen para aguantarse dos hombres",
    },
    {
        "id": 4,
        "nombre": "Maluma",
        "altura": 1.5,
        "habilidad": "",
        "imagen": "https://pokenea-imagenes-sdeossag.s3.us-east-1.amazonaws.com/maluma.jpg",
        "frase": "La humildad prevalece la fucking magia crece",
    },
    {
        "id": 5,
        "nombre": "Blessd",
        "altura": 1.2,
        "habilidad": "Te secuestra y te amenaza con cortarte la lengua",
        "imagen": "https://pokenea-imagenes-sdeossag.s3.us-east-1.amazonaws.com/blessd.jpg",
        "frase": "El Leon de Juda pillen en google que es Leon de Juda",
    },
    {
        "id": 6,
        "nombre": "AlfredoMorelos",
        "altura": 1.3,
        "habilidad": "El Bufalo te mata de un golazo",
        "imagen": "https://pokenea-imagenes-sdeossag.s3.us-east-1.amazonaws.com/morelos.jpg",
        "frase": "Digale que nos vemos alla en Medellin a ver si tiene las guevas de decirlo otra vez",
    },
    {
        "id": 7,
        "nombre": "KrisR",
        "altura": 0.9,
        "habilidad": "Esa valija te mata",
        "imagen": "https://pokenea-imagenes-sdeossag.s3.us-east-1.amazonaws.com/krisr.jpg",
        "frase": "Las valijas usan Django los cachorros usan Flask",
    },
    {
        "id": 8,
        "nombre": "MatiasSanchez",
        "altura": 0.7,
        "habilidad": "Te tira tunel y te hace gol",
        "imagen": "https://pokenea-imagenes-sdeossag.s3.us-east-1.amazonaws.com/matisanchez.jpg",
        "frase": "Matias Sanchez 11 años 🤙🤙",
    },
    {
        "id": 9,
        "nombre": "Luigi21Plus",
        "altura": 0.6,
        "habilidad": "El boquisucio, el patan, te pone un tema y te toca perrear suavecito hasta tan abajo que llegas al infierno",
        "imagen": "https://pokenea-imagenes-sdeossag.s3.us-east-1.amazonaws.com/luigi21plus.jpg",
        "frase": "Tú te meneas de una manera demasiao muy violenta que al bellaquear tienta",
    },

    
]

def get_random_pokenea():
    return random.choice(POKENEAS)
