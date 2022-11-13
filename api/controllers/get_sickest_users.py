from typing import Any, Dict, List
from api.helpers import error, internal_server_error, success
from api.infra import UsersRepository
from api.protocols import Controller, HttpRequest, HttpResponse



class GetSickestUsersController(Controller):
    def __init__(self, limit: int, repository: UsersRepository) -> None:
        self.limit = limit
        self.repository = repository
    
    def calculate_score(self) -> List[Dict[str, Any]]:
        users = [user.to_dict for user in self.repository.get_users()]
        return sorted(users, key=lambda user: user['score'], reverse=True)


    def handle(self, request: HttpRequest) -> HttpResponse:
        try:
            
            users = self.calculate_score()
            if(self.limit <= 0):
                return success({'data': users})
            return success({'data': users[0:self.limit]})

        except Exception as ex:
            return internal_server_error(error(f'{ex}'))