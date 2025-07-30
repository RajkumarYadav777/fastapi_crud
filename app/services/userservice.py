
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from app.schemas.userschema import UserCreate, UserUpdate, UserRead
from app.services.userservice.utils.user_security import get_password_hash
from app.services.userservice.user_crud  import UserCRUD
from app.models.user import User


class UserService:
    def __init__(self, db:Session):
        self.db = db
        self.crud = UserCRUD(db)

    
    # create user service
    def user_create(self, user_in:UserCreate) -> UserRead:

        # user existence
        existing_user = self.crud.get_user_by_email(user_in.email)
        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        
        # hash the password
        hashed_passwod = get_password_hash(user_in.password)

        # process data to store in db
        

        # save to db
        user = self.crud.create(user_in, hashed_passwod)

        return UserRead.model_validate(user)
    

    # read services
    def get_user_by_pk(self, user_id:int) -> UserRead:
        # get the user by id
        user = self.crud.get_user_by_id(user_id)
        # check specific user exist 
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                detail='user not found')
        return UserRead.model_validate(user) 

    
    def get_user_by_email(self, email:str) -> UserRead:
        user = self.crud.get_user_by_email(email)

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail='user not found')
        return UserRead.model_validate(user)

    # get all the user

    def get_all_users(self, skip:int=0, limit:int=100) -> List[UserRead]:
        users = self.crud.get_all(skip=skip, limit=limit)

        return [UserRead.model_validate(user) for user in users]

    
    # update service
    def user_update(self, user_id:int, user_in:UserUpdate) -> UserRead:

        # get the user
        user = self.crud.get_user_by_id(user_id)

        if not user:
            raise HTTPException(status_cod=status.HTTP_404_NOT_FOUND, detail='user not found')
        
        # transform request schema in to native python
        update_data = user_in.model_dump(exclude_unset=True)

        # check if password in the update data
       
        if "password" in update_data:
            update_data["password"] = get_password_hash(update_data["password"])

        # call the update method from crud
        update_user = self.crud.update(user=user, update_data=update_data)

        # return response schema by validate
        return UserRead.model_validate(update_user)
    

    # delete user
    def user_delete(self, user_id:int) -> None:

        user = self.crud.get_user_by_id(user_id)

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not found')

        #  call the delete crud
        self.crud.delete(user)
