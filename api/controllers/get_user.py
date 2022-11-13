from api.exceptions import NotFound
from api.helpers import error, internal_server_error, not_found, success
from api.infra import UsersRepository
from api.protocols import Controller, HttpRequest, HttpResponse


class GetUserByIDController(Controller):
    def __init__(self, id: int, repository: UsersRepository) -> None:
        self.id = id
        self.repository = repository
    
    def handle(self, request: HttpRequest) -> HttpResponse:
        try:
            user = self.repository.get_user_by_id(self.id)

            if(user is None):
                raise NotFound('User not found')

            return success({'data': user.to_dict})
            
        except NotFound as ex:
            return not_found(error(f'{ex}'))
        except Exception as ex:
            return internal_server_error(error(f'{ex}'))
