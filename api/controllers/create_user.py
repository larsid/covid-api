from api.exceptions import BadRequestException
from api.helpers import (
    bad_request, created, error, internal_server_error, validate_required_params
)
from api.infra import UsersRepository
from api.models import AddUserModel
from api.protocols import Controller, HttpRequest, HttpResponse



class CreateUserController(Controller):
    def __init__(self, repository: UsersRepository) -> None:
        self.repository = repository
    
    def handle(self, request: HttpRequest) -> HttpResponse:
        required_params = ['name', 'temperature', 'heart_rate', 'blood_pressure', 'respiratory_rate']
        
        try:
            validate_required_params(request, required_params)

            name = str(request.body['name'])

            if(self.repository.get_user_by_name(name) is not None):
                raise Exception(f'User {name} already exists')

            user = self.repository.add_user(AddUserModel(**request.body))
          
            return created({'data': user.to_dict})
        
        except BadRequestException as ex:
            return bad_request(error(f'{ex}'))
        except Exception as ex:
            return internal_server_error(error(f'{ex}'))