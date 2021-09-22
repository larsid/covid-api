from app import db


class User(db.Model):
    __tablename__ = 'users'
    
    id               = db.Column(db.Integer, primary_key=True)
    name             = db.Column(db.String(20), index=True)
    temperature      = db.Column(db.Float)
    heart_rate       = db.Column(db.Integer)
    blood_pressure   = db.Column(db.Integer)
    respiratory_rate = db.Column(db.Integer)
    

    def __init__(self, name, temperature, heart_rate, blood_pressure, respiratory_rate):
        self.name             = name
        self.temperature      = temperature
        self.heart_rate       = heart_rate
        self.blood_pressure   = blood_pressure
        self.respiratory_rate = respiratory_rate

    def __repr__(self)->str:
        return f'<{self.name}>'
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


    def update(self, data:dict):
        self.name             = data['name']
        self.temperature      = data['temperature']
        self.heart_rate       = data['heart_rate']
        self.blood_pressure   = data['blood_pressure']
        self.respiratory_rate = data['respiratory_rate']
        db.session.add(self)
        db.session.commit()



    def json(self)->dict:
        return {
            'id':               self.id,
            'name':             self.name,
            'temperature':      self.temperature,
            'heart_rate':       self.heart_rate,
            'blood_pressure':   self.blood_pressure,
            'respiratory_rate': self.respiratory_rate
        }
    