from trytond.pool import Pool
from . import party

def register():
    Pool.register(
        party.Party,
        module='party_co', type_='model'
    )
