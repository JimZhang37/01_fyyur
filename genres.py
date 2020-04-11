
from enum import Enum
from wtforms.validators import ValidationError

class Genres(Enum):
    Alternative = 'Alternative'
    Blues = 'Blues'
    Classical = 'Classical'
    Country = 'Country'
    Electronic = 'Electronic'
    Folk = 'Folk'
    Funk = 'Funk'
    Hip_Hop = 'Hip-Hop'
    Heavy_Metal = 'Heavy Metal'
    Instrumental = 'Instrumental'
    Jazz = 'Jazz'
    Musical_Theatre = 'Musical Theatre'
    Pop = 'Pop'
    Punk = 'Punk'
    R_B = 'R&B'
    Reggae = 'Reggae'
    Rock_n_Roll = 'Rock n Roll'
    Soul = 'Soul'
    Other = 'Other'

    @classmethod
    def choice(cls):
        return [(choice.value, choice.value) for choice in cls]
    @classmethod
    def a(cls, form, field):
        # x = [e.value for e in cls]
        # print(x)
        for i in field.data:
            # print(i)
            if i not in [e.value for e in cls]:
                raise ValidationError(f'{i} is not in the enum')
