from fastapi.routing import APIRouter
from fastapi import Depends, HTTPException, Response
from typing import Annotated


google = APIRouter()

from api.auth.dependency import auth_by_google
from api.auth.database.shemas import GoogleOIDCModel


@google.get("/")
async def index(data: Annotated[dict, Depends(auth_by_google)]) -> GoogleOIDCModel:
    model = GoogleOIDCModel(
        name=data['given_name'],
        surname=data['family_name'],
        email=data['email'],
        picture_uri=data['picture']
    )
    return model

