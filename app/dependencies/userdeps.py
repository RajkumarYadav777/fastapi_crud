from fastapi import Depends
from sqlalchemy.orm import Session
from app.services.userservice import UserService
from app.repositories.userrepo import UserCRUD
from app.dependencies.dbdeps import get_db

def get_user_service(db:Session = Depends(get_db)) -> UserService:
    repo = UserCRUD(db)
    return UserService(repo)

# here we are combining repo(crud) and servie as a single injectable dependency
# to work with routers
