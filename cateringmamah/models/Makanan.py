from odoo import api, fields, models


class Barang(models.Model):
    _name = 'cateringmamah.makanan'
    _description = 'New Description'

    name = fields.Char(string='Name')
    harga_beli = fields.Integer(string='Harga Modal', required=True)
    harga_jual = fields.Integer(string='Harga Jual', required=True)
    # Perubahannya ada di sini
    kelompokmakanan_id = fields.Many2one(comodel_name='cateringmamah.kelompokmakanan',
                                        string='Kelompok Makanan',
                                        ondelete='cascade')

    supplier_id = fields.Many2many(comodel_name='cateringmamah.supplier', string='Supplier')
    stok = fields.Integer(string='Stok')