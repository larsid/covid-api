from api.exceptions import NotFound
from api.helpers import error, internal_server_error, not_found, success
from api.infra import UsersRepository
from api.protocols import Controller, HttpRequest, HttpResponse


class RemoveUserController(Controller):
    def __init__(self, id: int, repository: UsersRepository) -> None:
        self.id = id
        self.repository = repository
    
    def handle(self, request: HttpRequest) -> HttpResponse:
        try:
            if(self.repository.get_user_by_id(self.id) is None):
                raise NotFound('User not found')

            self.repository.remove_user(self.id)
            return success({'data': f'User {self.id} deleted'})
            
        except NotFound as ex:
            return not_found(error(f'{ex}'))
        except Exception as ex:
            return internal_server_error(error(f'{ex}'))
