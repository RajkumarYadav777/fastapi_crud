

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated=True)

# generate password hash
def get_password_hash(password:str) -> str:
    return pwd_context.hash(password)

# verify password

def verify_password(password:str, hashed_password:str) -> bool:

    return pwd_context.verify(password, hashed_password)
