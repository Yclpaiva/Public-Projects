from typing import Annotated
from pydantic import Field
from contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', examples=['CT Ironberg'], max_length=20)]
    endereco: Annotated[str, Field(description='Nome do endereço do CT', examples=['Rua matilda, 30'], max_length=60)]
    proprietario: Annotated[str, Field(description='Nome do proprietario do CT', examples=['Renato Cariani'], max_length=30)]

