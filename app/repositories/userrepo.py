# user crud
# only db interactions no business logic

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Optional, List

from app.models.user import User
from app.schemas.userschema import UserCreate, UserUpdate

# inside each funcion db:Session dont have to provide because we use it inside __init__
#  the db will availbale for every requst in this class
# all methods share same init variables
class UserCRUD:
    def __init__(self, db:Session):
        self.db = db  

    
    # retrieve users
    def get_user_by_id(self, user_id:int) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()
    
    def get_user_by_email(self, email:str) -> Optional[User]:
        return self.db.query(User).filter(User.email==email).first()
    
    def get_all(self, skip :int = 0, limit: int = 100) -> List[User]:
        return self.db.query(User).offset(skip).limit(limit).all()
    

    # create user
    def create(self, user_in:UserCreate, hashed_password:str) -> User:

        user = User(
            name = user_in.name,
            email = user_in.email,
            password = hashed_password
        )

        self.db.add(user)

        try:
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError:
            self.db.rollback()
            raise
    

    # update the incoming data
    def update(self, user:User, user_in:UserUpdate) -> User:
        update_data = user_in.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(user, key, value)


        # add updated user to the db
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    # delete the user from db
    def delete(self, user:User) -> None:
        self.db.delete(user)
        self.db.commit()