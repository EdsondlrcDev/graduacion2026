#Lista de invitados con 3 claves para su uso posterior en df
#y posteriortransformacion a df

#===========================================================
# LIBRERIRAS
#===========================================================
import pandas as pd
#===========================================================
# PROCESO
#===========================================================

#invitados actuales
invitados={
    "Cecilia":{
        "Persona": "Cecilia",
        "Posicion": "Madre de Monterrey",
        "Extra": "Divorciada, no sabe tomar, actualmente juntada."
    },
    "Edgar padre":{
        "Persona":"Edgar Joel",
        "Posicion": "Papá de Torreón",
        "Extra":"Divorciado, tiene mucho awante tomando, actualmente juntado."
    },
    "Pedro":{
        "Persona":"Pedro",
        "Posicion": "Padrastro Monterrey",
        "Extra":"Le gusta jugar billar y la cerveza, actualmente juntado con Cecilia."
    },
    "Fanny":{
        "Persona":"Estefanny o Estefania, no recuerdo bien",
        "Posicion": "Madrastra Torreón",
        "Extra":"Parece Mala onda, pero es peor y sabe hacer postres bien ricardos."
    },
    "Edgar Joel":{
        "Persona":"Edgar Joel",
        "Posicion": "Hermana mayor",
        "Extra":"Le salen bien las gorditas de harina."
    },
    "Paola":{
        "Persona":"Paola Itzel",
        "Posicion": "Hermano menor",
        "Extra":"No se confundan, originalmente era Paul hasta su transición."
    },
    "Sergio":{
        "Persona":"Sergio",
        "Posicion": "Wey de Paola, cuñis",
        "Extra":"No sabe sobre el sexo original de Pao."
    },
    "Adrian":{
        "Persona":"Adriana",
        "Posicion": "hermanastra, hija de Pedro ",
        "Extra":"Tiene aguante medio, sabe bailar cumbias y aveces pone para las cheves."
    },
    "Andrea":{
        "Persona":"Pillos, Andy, en última instancia 'Andrea'",
        "Posicion": "Pillos",
        "Extra":"Siempre está sobria, ya me cayó mal por eso y cree que es de España tío."
    },
    "Andres":{
        "Persona":"Andres",
        "Posicion": "Vato de Pillos",
        "Extra":"Fui a un palnorte con el, creo que estuvo bien."
    },
    "Alejandra":{
        "Persona":"Maria Alejandra (diganle doña Mary)",
        "Posicion": "Bicho",
        "Extra":"Es un peligro para la sociedad, no la miren a los ojos y nunca le presten 20 pesos."
    },
    "Alan":{
        "Persona":"Don Alan",
        "Posicion": "Prometido de Maria",
        "Extra":"Se ve tranqui, no lo conozco mucho pero aguanta a Alejandra y eso ya es un logro."
    },
    "Brenda":{
        "Persona":"Brandy",
        "Posicion": "Casi Ex de primaria (en mi imaginación), traficante de labubus fake, comadre",
        "Extra":"No lo se bro le gusta grabar y asi, hace 6 años que no la veo, deberia golpearla por eso."
    },
    "Wey de Brenda":{
        "Persona":"No sé su nombre, LOL",
        "Posicion": "Pololo de Brenda",
        "Extra":"Actualmente investigado por complicidad en evasión fiscal."
    },
    "Leonardo":{
        "Persona":"Hector Leonardo (Pendejin para los compas)",
        "Posicion": "Naco, mi dos pa todo",
        "Extra":"Parece que solo piensa con la cabeza de abajo, pero derepe tiene sus momentos y no deja morir como aveces lo hacen Pillos, Ale y Brenda."
    }
}
def obtener_df_invitados():
    return pd.DataFrame.from_dict(
        invitados,
        orient="index"
    )[["Persona", "Posicion", "Extra"]]