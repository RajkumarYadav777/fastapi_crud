# user rpoute file

from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional

from app.schemas.userschema import UserCreate, UserRead, UserUpdate
from app.models.user import User
from app.services.userservice import user_service
