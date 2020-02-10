from odoo import models, fields, api

class Cliente(models.Model):
	_name = 'vet.clientes'
	nombre = fields.Char('Nombre cliente', required=True)
	telefono = fields.Integer('Telefono', required=True)
	direccion = fields.Char('Direccion', required=True)
	nif = fields.Char('NIF', required=True)