from odoo import models, fields, api

class Mascota(models.Model):
	_name = 'vet.mascotas'
	idMascota = fields.Integer('ID', required=True)
	nombre = fields.Char('Nombre mascota', required=True)
	cliente = fields.Many2one('vet.clientes', 'Cliente')
	raza = fields.Char('Raza animal', required=True)
	edad = fields.Integer('Edad', required=True)

	def name_get(self):
		res=[]
		for record in self:
			name = record.nombre
			res.append((record.id, name))
		return res