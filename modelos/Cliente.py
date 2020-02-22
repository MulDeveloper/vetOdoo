from odoo import models, fields, api

class Cliente(models.Model):
	_name = 'vet.clientes'
	nombre = fields.Char('Nombre cliente', required=True)
	telefono = fields.Integer('Telefono', required=True)
	direccion = fields.Char('Direccion', required=True)
	nif = fields.Char('NIF', required=True)

	def name_get(self):
		res=[]
		for record in self:
			name = record.nombre
			res.append((record.id, name))
		return res