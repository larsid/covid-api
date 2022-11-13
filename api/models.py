from typing import Any, Dict


class UserModel:
    def __init__(self, 
        id: int,
        name: str, 
        temperature: float, 
        heart_rate: int, 
        blood_pressure: int, 
        respiratory_rate: int
    ):
        self.id               = id
        self.name             = name
        self.temperature      = temperature
        self.heart_rate       = heart_rate
        self.blood_pressure   = blood_pressure
        self.respiratory_rate = respiratory_rate


    def update(self, user: Dict[str, Any]):
        self.temperature      = user['temperature']
        self.heart_rate       = user['heart_rate']
        self.blood_pressure   = user['blood_pressure']
        self.respiratory_rate = user['respiratory_rate']
    
    @property
    def score(self) -> int:
        score = 0
        if(self.temperature      < 35.0  or self.temperature > 37.5):    score += 1
        if(self.heart_rate       < 60    or self.heart_rate > 100):      score += 2
        if(self.blood_pressure   < 80    or self.blood_pressure > 130):  score += 1
        if(self.respiratory_rate < 12    or self.respiratory_rate > 20): score += 2
        return score

    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id':               self.id,               
            'name':             self.name,       
            'temperature':      self.temperature, 
            'heart_rate':       self.heart_rate,    
            'blood_pressure':   self.blood_pressure,
            'respiratory_rate': self.respiratory_rate,
            'score':            self.score
        }

    def __eq__(self, obj: object) -> bool:
        if(not isinstance(obj, UserModel)):
            return False
        return self.id == obj.id

    def __repr__(self)->str:
        return f'UserModel(name={self.name})'



class AddUserModel:
    def __init__(self, 
        name: str, 
        temperature: float, 
        heart_rate: int, 
        blood_pressure: int, 
        respiratory_rate: int
    ):
        self.name             = name
        self.temperature      = temperature
        self.heart_rate       = heart_rate
        self.blood_pressure   = blood_pressure
        self.respiratory_rate = respiratory_rate

    @property
    def to_dict(self) -> Dict[str, Any]:
        return {       
            'name':             self.name,       
            'temperature':      self.temperature, 
            'heart_rate':       self.heart_rate,    
            'blood_pressure':   self.blood_pressure,
            'respiratory_rate': self.respiratory_rate
        }
