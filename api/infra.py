from threading import Lock
from typing import Dict, List

from api.models import AddUserModel, UserModel 

class UsersRepository:
    def __init__(self) -> None:
        self.lock = Lock()
        self.tables: Dict[str, List[UserModel]] = {
            'users': []
        }
    
    def _next_id(self, table: str) -> int:
        data = self.tables[table]
        if(not data):
            return 0
        return data[-1].id + 1


    def add_user(self, model: AddUserModel) -> UserModel:
        with self.lock:
            id = self._next_id('users')
            user = UserModel(id, **model.to_dict)
            self.tables['users'].append(user)
            return user
        

    def update_user(self, model: UserModel):
        with self.lock:
            for user in self.tables['users']:
                if(user.id == model.id):
                    user.update(model.to_dict)

    
    def get_users(self) -> List[UserModel]:
        with self.lock:
            return self.tables['users']

    
    def get_user_by_id(self, id: int) -> 'UserModel | None':
        with self.lock:
            for user in self.tables['users']:
                if(user.id == id):
                    return user
            return None
    

    def get_user_by_name(self, name: str) -> 'UserModel | None':
        with self.lock:
            for user in self.tables['users']:
                if(user.name == name):
                    return user
            return None


    def remove_user(self, id: int):
        with self.lock:
            for user in self.tables['users'].copy():
                if(user.id == id):
                    self.tables['users'].remove(user)
    
