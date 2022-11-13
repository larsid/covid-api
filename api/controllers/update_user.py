from api.exceptions import BadRequest, NotFound
from api.helpers import (
    bad_request, error, internal_server_error, not_found, success, validate_required_params
)
from api.infra import UsersRepository
from api.models import UserModel
from api.protocols import Controller, HttpRequest, HttpResponse



class UpdateUserController(Controller):
    def __init__(self, id: int, repository: UsersRepository) -> None:
        self.id = id
        self.repository = repository
    
    def handle(self, request: HttpRequest) -> HttpResponse:
        required_params = ['name', 'temperature', 'heart_rate', 'blood_pressure', 'respiratory_rate']
        
        try:
            validate_required_params(request, required_params)

            if(self.repository.get_user_by_id(self.id) is None):
                raise NotFound('User not found')
            
            user = UserModel(id=self.id, **request.body)
            self.repository.update_user(user)
            return success({'data': 'User updated'})
        
        except BadRequest as ex:
            return bad_request(error(f'{ex}'))
        except NotFound as ex:
            return not_found(error(f'{ex}'))
        except Exception as ex:
            return internal_server_error(error(f'{ex}'))