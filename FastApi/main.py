
from fastapi import FastAPI 
from ulid import ULID
from pydantic import BaseModel


app = FastAPI()

#para registrar um metodo http é preciso cadastrar um caminho(rota)

esportes = [
    {   'id': str(ULID()),
        'Nome':'Vôlei',
        'Tipo': "Fermino",
        "Coletivo": True
    },
    {   'id': str(ULID()),
        'Nome':'Skat',
        'Tipo': "Fermino",
        "Coletivo": False
    }
]

#adiciona novos esportes
class Esporte(BaseModel):
    nome : str
    tipo : str
    coletivo : bool




#rota de esportes cadastrados
@app.get('/esportes')
def esporte_list():
    
    return esportes

@app.get("/esportes/{id}")
def esporte_detalhes(id:str):
    # buscar na lista e retornar
    for esporte in esportes:
        if esporte['id'] == id:
            
            return esporte
    
    return {}

@app.delete("/esporte/{id}")
def esporte_deletar(id:str):
    for esporte in esportes:
        if esporte['id'] == id:
            esportes.remove(esporte)
            return {} 
    
    return {}



#Faz referencia a classe esporte criada com o intuito de adicionar novos esportes.
@app.post('/esporte')
def esporte_novo(esporte:Esporte):
    esportes.append({

        'id': str(ULID()),
        'Nome':esporte.nome,
        'Tipo': esporte.tipo,
        "Coletivo": esporte.coletivo
    })


@app.put("/esportes/{id}")
def esporte_atualizar(esporte:Esporte,id:str):
        for indice, e in enumerate(esportes):
            if e['id'] == id:
                esportes[indice] = {
                
                'id': str(ULID()),
                'Nome':esporte.nome,
                'Tipo': esporte.tipo,
                "Coletivo": esporte.coletivo}

                return esportes[indice]





@app.get("/home")
def home():
    return "Bem Vindos aos jogos de 2024"





