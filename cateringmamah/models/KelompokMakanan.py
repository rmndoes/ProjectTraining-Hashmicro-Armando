from odoo import api, fields, models


class KelompokMakanan(models.Model):
    _name = 'cateringmamah.kelompokmakanan'
    _description = 'New Description'

    name = fields.Selection([
        ('lauk pauk', 'Lauk Pauk'),
        ('desert', 'Desert'),
        ('minuman', 'Minuman')
    ], string='Nama Kelompok')

    kode_kelompok = fields.Char(string='Kode Kelompok')

    name = fields.Char(string='Nama Kelompok Makanan')
    kode_kelompok = fields.Char(string='Kode Kelompok Makanan')
    kode_rak = fields.Char(string='Kode Rak')

    makanan_ids = fields.One2many(comodel_name='cateringmamah.makanan',
                                inverse_name='kelompokmakanan_id',
                                string='Daftar Makanan')
    jml_item = fields.Char(compute='_compute_jml_item', string='Jml Item')

    @api.depends('makanan_ids')
    def _compute_jml_item(self):
        for record in self:
            a = self.env['cateringmamah.makanan'].search([('kelompokmakanan_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_item = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar isi')