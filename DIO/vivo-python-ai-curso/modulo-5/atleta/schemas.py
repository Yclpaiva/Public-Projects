from typing import Annotated
from pydantic import Field, PositiveFloat
from contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta",examples=['yuri'] ,max_length=100)]
    cpf: Annotated[str, Field(description="cpf do atleta",examples=[12345678900] ,max_length=11)]
    idade: Annotated[int, Field(description="idade do atleta",examples=[25])]
    peso: Annotated[PositiveFloat, Field(description="peso do atleta",examples=[80.5])]
    altura: Annotated[PositiveFloat, Field(description="altura do atleta",examples=[180.5])]
    sexo: Annotated[str, Field(description="sexo do atleta",examples=['M'] ,max_length=1)]




