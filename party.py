from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import PoolMeta

__all__ = ['Party']
class Party(metaclass=PoolMeta):
    __name__ = 'party.party'

    nit = fields.Char('NIT', size=20)
    tipo_documento = fields.Selection([
        ('cc', 'Cédula de Ciudadanía'),
        ('nit', 'NIT'),
        ('ce', 'Cédula de Extranjería'),
        ], 'Tipo de Documento'
