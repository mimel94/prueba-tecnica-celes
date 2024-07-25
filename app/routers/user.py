from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from app.controllers.user import UserController
from app.schemas.user import Token
from app.utils.token_generator import TokenGenerator
from settings.base import FAKE_USER_DB

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = UserController.authenticate(db=FAKE_USER_DB,
                                       username=form_data.username,
                                       password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = TokenGenerator.generate_token({"username": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

