from api.helpers import error, internal_server_error, success
from api.infra import UsersRepository
from api.protocols import Controller, HttpRequest, HttpResponse


class GetAllUsersController(Controller):
    def __init__(self, repository: UsersRepository) -> None:
        self.repository = repository
    
    def handle(self, request: HttpRequest) -> HttpResponse:
        try:
            users = [model.to_dict for model in self.repository.get_users()]

            return success({'data': users})
        except Exception as ex:
            return internal_server_error(error(f'{ex}'))