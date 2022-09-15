from odoo import api, fields, models


class Supplier(models.Model):
    _name = 'cateringmamah.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Perushaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    makanan_id = fields.Many2many(comodel_name='cateringmamah.makanan', string='Makanan')