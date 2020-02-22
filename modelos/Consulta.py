from odoo import models, fields, api

class Consulta(models.Model):
	_name = 'vet.consultas'
	nombreClinica = fields.Char('Clinica',required=True,default="Clinica colon")
	cliente = fields.Many2one('vet.clientes', 'Cliente')
	mascota = fields.Many2one('vet.mascotas', 'Mascota')
	fecha = fields.Date('Fecha', required=True)
	descripcion = fields.Text('Descripcion', required=True)
	total = fields.Float('Total', required=True)
	totalIva = fields.Float(string='Total IVA', compute='calculoTotal')


	@api.one
	@api.depends('total')
	def calculoTotal(self):
		self.totalIva = (self.total * 1.21)