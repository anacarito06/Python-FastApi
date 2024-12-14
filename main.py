from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

class Carro(BaseModel):
    id: str
    marca: str
    modelo: int
    
carros = [
    Carro(id="1", marca="Mazda", modelo=1983),
     Carro(id="2", marca="Honda", modelo=1993),
    
]

# Base de datos simulada (lista de usuarios)
class Usuario(BaseModel):
    id: int
    nombre: str
    email: str

app = FastAPI()


usuarios = [
    Usuario(id="1", nombre="Jennifer Gonzales", email="jenniferg@gmail.com"),
     Usuario(id="2", nombre="Pedro Jimenez", email="pjimenez@gmail.com"),
]


@app.get("/")
async def home():
    return 

@app.get("/carros", response_model=List[Carro])
async def get_carros():
    return carros


@app.post("/carros", status_code=201)
async def get_carros(carro: Carro):
    carros.append(carro)
    return {"message": "Nuevo carro creado"}

@app.delete("/carros/{id}")
async def update_carro(id: str, carro: Carro):
    for index, c in enumerate(carros):
        if c.id == id:
            carros[index] = carro
            return { "message": "Carro actualizado"}
        raise HTTPException(status_code=404, detail="Carro no encontrado")
    
# Ruta para obtener todos los usuarios

@app.get("/")
async def home():
    return 

@app.get("/usuarios", response_model=List[Usuario])
def get_usuarios():
    return usuarios

# Ruta para agregar un nuevo usuario
@app.post("/usuarios", response_model=Usuario)
def create_usuario(usuario: Usuario):
    usuarios.append(usuario.dict())
    return usuario

# Ruta para obtener un usuario por ID
@app.get("/usuarios/{usuario_id}", response_model=Usuario)
def get_usuario(usuario_id: int):
    usuario = next((u for u in usuarios if u['id'] == usuario_id), None)
    if usuario:
        return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

