from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import JWTError, jwt
from dotenv import load_dotenv
import os
from .database import SessionLocal

load_dotenv()

SECRET_KEY = os.getenv('AUTH_SECRET_KEY')
ALGORITHM = os.getenv('AUTH_ALGORITHM')

# Cria e gerencia sessões de banco de dados que usa SQLAlchemy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Especifica que Session deve ser fornecido por meio de dependência
# Depends(get_db): Indica que a dependência deve ser resolvida. Obtem a sessão de banco de dados
db_dependency = Annotated[Session, Depends(get_db)]
# Permite gerenciar e aplicar algoritmos de hash de senhas
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
# Configura um esquema de autenticação baseado no padrão OAuth2
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
# Especifica que o token deve ser fornecido por meio de dependência
oauth2_bearer_dependency = Annotated[str, Depends(oauth2_bearer)]
# Função para obter o usuário atual com base no token fornecido
async def get_current_user(token: oauth2_bearer_dependency):
    try:
        # Decodifica o token JWT usando a chave secreta e o algoritmo especificados
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Extrai o nome de usuário e o ID do usuário do payload do token
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        # Verifica se o nome de usuário e o ID do usuário são válidos
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Usuário inválido!')
        # Retorna o nome de usuário e o ID do usuário como um dicionário
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Usuário inválido!')
# Especifica que o dicionário do usuário deve ser fornecido por meio de dependência
user_dependency = Annotated[dict, Depends(get_current_user)]




